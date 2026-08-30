#!/usr/bin/env python3
"""
MB_0005 finite-dimensional computational reading for ellipsoid fitting.

Purpose
-------
Reproduce a Gaussian d=40 SDP realization around the asymptotic boundary
alpha_star(3) = 1/4, while preserving the distinction:

    asymptotic theorem != finite-dimensional computational reading

A solver-reported feasible matrix is counted SAT only after direct validation:
    max_i |x_i^T R x_i - 1| <= EQ_TOL
    lambda_min(R) >= -PSD_TOL

This executable does not verify Theorem 1.2.

Dependencies
------------
numpy
cvxpy
pyyaml  (optional; JSON fallback is used if unavailable)

Preferred solvers
-----------------
CLARABEL, then SCS fallback.

Usage
-----
python tests/MB_0005_ellipsoid_fitting_verification.py

Optional environment variables
------------------------------
MB0005_MODE=paper|quick
MB0005_SEED=<integer>
MB0005_OUTPUT_DIR=<path>
"""

from __future__ import annotations

import csv
import json
import os
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any

import numpy as np

try:
    import cvxpy as cp
except ImportError as exc:
    raise SystemExit(
        "cvxpy is required. Install cvxpy with CLARABEL and/or SCS, then rerun."
    ) from exc


D = 40
KAPPA = 3.0
ALPHA_STAR = 0.25
EQ_TOL = 1e-4
PSD_TOL = 1e-6
SEED = int(os.environ.get("MB0005_SEED", "260827372"))
MODE = os.environ.get("MB0005_MODE", "paper").strip().lower()
OUTPUT_DIR = Path(os.environ.get("MB0005_OUTPUT_DIR", "results/mb_0005_runtime"))

if MODE == "quick":
    ALPHAS = [0.20, 0.24, 0.25, 0.26, 0.30]
    TRIALS_PER_ALPHA = 2
else:
    ALPHAS = [0.10, 0.15, 0.20, 0.225, 0.24, 0.25, 0.26, 0.275, 0.30, 0.35, 0.40]
    TRIALS_PER_ALPHA = 8

SOLVER_ORDER = ("CLARABEL", "CVXOPT")


@dataclass
class TrialResult:
    alpha_requested: float
    n: int
    alpha_realized: float
    trial: int
    seed: int
    reading: str
    solver: str | None
    solver_status: str | None
    equality_residual: float | None
    min_eigenvalue: float | None
    note: str


def validate_candidate(X: np.ndarray, R_value: np.ndarray | None) -> tuple[bool, float | None, float | None]:
    if R_value is None:
        return False, None, None

    Rv = 0.5 * (R_value + R_value.T)
    vals = np.einsum("bi,ij,bj->b", X, Rv, X)
    residual = float(np.max(np.abs(vals - 1.0)))
    min_eig = float(np.linalg.eigvalsh(Rv).min())

    valid = residual <= EQ_TOL and min_eig >= -PSD_TOL
    return valid, residual, min_eig


def solve_instance(X: np.ndarray) -> tuple[str, str | None, str | None, float | None, float | None, str]:
    n, d = X.shape
    R = cp.Variable((d, d), symmetric=True)

    constraints = [R >> 0]
    constraints.extend(cp.quad_form(X[i], R) == 1 for i in range(n))
    problem = cp.Problem(cp.Minimize(0), constraints)

    installed = set(cp.installed_solvers())
    attempts: list[str] = []

    for solver in SOLVER_ORDER:
        if solver not in installed:
            attempts.append(f"{solver}: unavailable")
            continue

        try:
            kwargs: dict[str, Any] = {"solver": solver, "verbose": False}
            if solver == "SCS":
                kwargs.update({"eps": 1e-6, "max_iters": 200_000})

            problem.solve(**kwargs)
            status = problem.status
            attempts.append(f"{solver}: {status}")

            if status in (cp.OPTIMAL, cp.OPTIMAL_INACCURATE):
                valid, residual, min_eig = validate_candidate(X, R.value)
                if valid:
                    return (
                        "SAT",
                        solver,
                        status,
                        residual,
                        min_eig,
                        "solver candidate passed direct equality and PSD validation",
                    )

                # A candidate that fails direct validation is not counted SAT.
                # Retry with the next solver if available.
                if solver != SOLVER_ORDER[-1]:
                    continue
                return (
                    "UNRESOLVED",
                    solver,
                    status,
                    residual,
                    min_eig,
                    "solver reported feasible/inaccurate but returned matrix failed direct validation",
                )

            if status in (cp.INFEASIBLE, cp.INFEASIBLE_INACCURATE):
                return (
                    "UNSAT",
                    solver,
                    status,
                    None,
                    None,
                    "solver reported infeasible",
                )

        except Exception as exc:
            attempts.append(f"{solver}: error {type(exc).__name__}: {exc}")
            continue

    return (
        "UNRESOLVED",
        None,
        None,
        None,
        None,
        "; ".join(attempts) if attempts else "no supported solver available",
    )


def run() -> tuple[list[TrialResult], list[dict[str, Any]]]:
    rng = np.random.default_rng(SEED)
    rows: list[TrialResult] = []

    for alpha in ALPHAS:
        n = int(round(alpha * D * D))
        for trial in range(TRIALS_PER_ALPHA):
            trial_seed = int(rng.integers(0, 2**32 - 1))
            trial_rng = np.random.default_rng(trial_seed)
            X = trial_rng.normal(size=(n, D))

            reading, solver, status, residual, min_eig, note = solve_instance(X)
            rows.append(
                TrialResult(
                    alpha_requested=float(alpha),
                    n=n,
                    alpha_realized=n / (D * D),
                    trial=trial,
                    seed=trial_seed,
                    reading=reading,
                    solver=solver,
                    solver_status=status,
                    equality_residual=residual,
                    min_eigenvalue=min_eig,
                    note=note,
                )
            )
            print(
                f"alpha={alpha:.3f} n={n:4d} trial={trial+1}/{TRIALS_PER_ALPHA} "
                f"reading={reading}"
            )

    summary: list[dict[str, Any]] = []
    for alpha in ALPHAS:
        group = [r for r in rows if r.alpha_requested == float(alpha)]
        counts = {k: sum(r.reading == k for r in group) for k in ("SAT", "UNSAT", "UNRESOLVED")}
        resolved = counts["SAT"] + counts["UNSAT"]
        summary.append(
            {
                "alpha_requested": float(alpha),
                "n": group[0].n,
                "trials": len(group),
                **counts,
                "resolved": resolved,
                "fraction_sat_among_resolved": (counts["SAT"] / resolved) if resolved else None,
            }
        )

    return rows, summary


def write_outputs(rows: list[TrialResult], summary: list[dict[str, Any]]) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    trial_csv = OUTPUT_DIR / "MB_0005_trial_log.csv"
    with trial_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(asdict(rows[0]).keys()))
        writer.writeheader()
        writer.writerows(asdict(r) for r in rows)

    summary_csv = OUTPUT_DIR / "MB_0005_summary.csv"
    with summary_csv.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(summary[0].keys()))
        writer.writeheader()
        writer.writerows(summary)

    result = {
        "id": "MB_0005",
        "test": "finite_dimensional_gaussian_ellipsoid_fitting",
        "status": {
            "mathematical": "audited",
            "computational": "supported",
            "theorem_from_computation": "unsupported",
        },
        "specification": {
            "distribution": "standard Gaussian coordinates",
            "kappa": KAPPA,
            "alpha_star": ALPHA_STAR,
            "dimension": D,
            "predicted_transition_n": int(ALPHA_STAR * D * D),
            "equality_tolerance": EQ_TOL,
            "psd_tolerance": PSD_TOL,
        },
        "run": {
            "mode": MODE,
            "seed": SEED,
            "trials_per_alpha": TRIALS_PER_ALPHA,
            "alphas": ALPHAS,
        },
        "summary": summary,
        "interpretation": (
            "Finite-dimensional SDP readings are evaluated relative to the "
            "Gaussian asymptotic phase boundary alpha_star(3)=1/4. "
            "Agreement is computational support, not verification of Theorem 1.2."
        ),
    }

    result_path = OUTPUT_DIR / "MB_0005_ellipsoid_fitting_verification.json"
    result_path.write_text(json.dumps(result, indent=2), encoding="utf-8")

    print(f"\nWrote {trial_csv}")
    print(f"Wrote {summary_csv}")
    print(f"Wrote {result_path}")


if __name__ == "__main__":
    rows, summary = run()
    write_outputs(rows, summary)
