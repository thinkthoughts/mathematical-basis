"""
tests/MB_0001_general_sweep.py

Verification for MB_0001 (Residue Conditioning Specifies a Primorial
Density Correction) and Theorem 1 of
papers/density-correction/paper.md (v3.1).

Source claim (verbatim, MB_0001_RESIDUE_CONDITIONING.yaml /
paper.md Theorem 1):
    For Pk the k-th primorial (squarefree), m a squarefree divisor
    of Pk with m > 1, and a any residue with gcd(a,m) = 1:
        C(m) = m / phi(m)
    is the exact limiting ratio of the true count |S(Pk,L,m,a)| to
    the naive predicted count (phi(Pk)/Pk)*(L/m), independent of
    which admissible a is chosen. The exact per-period count is
    phi(Pk/m).

This script sweeps m in {6, 10, 30}, every admissible a mod m, and
several L values, and reports whether the computed ratio matches
C(m) = m/phi(m) and whether the computed per-period count matches
phi(Pk/m), for every case -- not just one illustrative case.
"""
from math import gcd
from sympy import totient, primefactors


def naive_predicted(limit, primorial, m):
    density = totient(primorial) / primorial
    return density * (limit / m)


def refined_predicted(limit, primorial, m):
    m_primes = set(primefactors(m))
    dens = 1.0
    for p in primefactors(primorial):
        if p not in m_primes:
            dens *= (1 - 1.0 / p)
    return dens * (limit / m)


def count_residue(limit, primorial, m, a):
    c = 0
    n = a
    while n <= 0:
        n += m
    for n in range(n, limit + 1, m):
        if gcd(n, primorial) == 1:
            c += 1
    return c


def run():
    Pk = 210  # 2*3*5*7
    m_values = [6, 10, 30]
    L_values = [10**5, 10**6, 10**7]

    results = []
    all_match = True

    for m in m_values:
        if Pk % m != 0:
            continue
        phi_m = int(totient(m))
        C_m_predicted = m / phi_m
        Pk_over_m = Pk // m
        phi_Pk_over_m = int(totient(Pk_over_m))

        admissible_a = [a for a in range(1, m + 1) if gcd(a, m) == 1]

        # exact per-period count check (L = Pk)
        per_period_matches = []
        for a in admissible_a:
            exact_count = count_residue(Pk, Pk, m, a)
            match = (exact_count == phi_Pk_over_m)
            per_period_matches.append({
                "a": a, "exact_count": exact_count,
                "predicted_phi_Pk_over_m": phi_Pk_over_m,
                "match": match,
            })
            if not match:
                all_match = False

        # ratio convergence check: Theorem 1 gives a bounded remainder
        # R(s) <= ceil(s/m), shrinking relative to L as L grows -- so
        # convergence is only asserted at the largest tested L per (m,a).
        # Smaller L values are reported for transparency (and to show
        # the expected finite-size fluctuation) but do not gate the
        # claim's status.
        ratio_checks = []
        largest_L = max(L_values)
        for a in admissible_a:
            for L in L_values:
                actual = count_residue(L, Pk, m, a)
                naive = naive_predicted(L, Pk, m)
                ratio = actual / naive
                is_largest_L = (L == largest_L)
                close_enough = abs(ratio - C_m_predicted) < 1e-3
                ratio_checks.append({
                    "a": a, "L": L, "ratio": round(ratio, 6),
                    "C_m_predicted": C_m_predicted,
                    "within_tolerance": close_enough,
                    "gates_claim_status": is_largest_L,
                })
                if is_largest_L and not close_enough:
                    all_match = False

        results.append({
            "m": m,
            "phi_m": phi_m,
            "C_m_predicted": C_m_predicted,
            "phi_Pk_over_m": phi_Pk_over_m,
            "admissible_a": admissible_a,
            "per_period_matches": per_period_matches,
            "ratio_checks_summary": {
                "total_checked": len(ratio_checks),
                "converged_at_largest_L": all(
                    r["within_tolerance"] for r in ratio_checks if r["gates_claim_status"]
                ),
                "smallest_L_fluctuation_note": (
                    "Smaller L values may fall outside the 1e-3 tolerance due to "
                    "finite-size effects (bounded remainder term, Theorem 1); this "
                    "does not affect claim status, which is gated on the largest L only."
                ),
            },
        })

    summary = {
        "Pk": Pk,
        "m_values_tested": m_values,
        "L_values_tested": L_values,
        "all_predictions_confirmed": all_match,
        "claim_status": "supported" if all_match else "rejected",
    }

    return {"results": results, "summary": summary}


if __name__ == "__main__":
    import json
    print(json.dumps(run(), indent=2))
