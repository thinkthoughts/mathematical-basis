# MB_0005 Proof Audit: Ellipsoid Fitting Phase Boundary

## Purpose

This document audits the proof structure supporting MB_0005 without presenting the result as independently re-derived.

The mathematical status of MB_0005 is:

```yaml
mathematical: audited
computational: supported
provenance: audited
```

The source theorem is Koehler and Sohn, *Universality and sharp thresholds for ellipsoid fitting* (arXiv:2608.27372).

The statement artifact is:

```text
statements/MB_0005_ELLIPSOID_FITTING.yaml
```

The executable and result artifacts are built separately:

```text
tests/MB_0005_ellipsoid_fitting_verification.py
results/MB_0005_ellipsoid_fitting_verification.yaml
```

The executable is a finite-dimensional computational realization. It does not verify the asymptotic theorem.

---

## 1. Audited theorem object

Let

\[
x_1,\ldots,x_n\in\mathbb R^d
\]

be i.i.d. random vectors with independent coordinates satisfying the source assumptions, including mean zero, variance one, uniform subgaussian control, and common fourth moment

\[
\kappa=\mathbb E[x_{1j}^4]>1.
\]

Consider the asymptotic regime

\[
n,d\to\infty,
\qquad
\frac{n}{d^2}\to\alpha\in(0,\infty).
\]

The fitting problem asks for a positive-semidefinite matrix \(R\) such that

\[
x_i^\top R x_i=1
\qquad
\text{for every }i.
\]

The source theorem supplies an explicit phase boundary

\[
\alpha_\star(\kappa)
\]

that partitions the asymptotic parameter space.

For

\[
\alpha<\alpha_\star(\kappa),
\]

a positive-definite ellipsoid fit exists with probability tending to one.

For

\[
\alpha>\alpha_\star(\kappa),
\]

no positive-semidefinite exact fit exists with probability tending to one, and the optimal squared fitting error converges to a positive asymptotic value.

The equality region

\[
\alpha=\alpha_\star(\kappa)
\]

is retained as the phase boundary itself. MB_0005 does not attach an additional theorem conclusion to that region beyond what the audited source explicitly warrants.

---

## 2. Specification boundary

The source defines the phase boundary through the rescaled semicircle law \(\nu\).

For \(\omega<\sqrt 2\), define

\[
s(\omega)=\int (x-\omega)_+^2\,d\nu(x),
\]

and

\[
m(\omega)=\int (x-\omega)_+\,d\nu(x).
\]

Set

\[
E_\kappa(\omega)
=
s(\omega)
+
\frac{\kappa-3}{2}m(\omega)^2.
\]

Let \(\omega_\kappa\in[-\sqrt2,\sqrt2]\) solve

\[
\omega_\kappa
=
\frac{\kappa-3}{2}m(\omega_\kappa).
\]

Then

\[
\alpha_\star(\kappa)
=
E_\kappa(\omega_\kappa).
\]

For Gaussian coordinates,

\[
\kappa=3,
\qquad
\omega_\kappa=0,
\qquad
\alpha_\star(3)=\frac14.
\]

The role of \(\alpha_\star(\kappa)\) in MB_0005 is therefore not an exception set. It is a specification boundary that determines which of two theorem conclusions applies.

---

## 3. Proof architecture audited from the source

MB_0005 does not reproduce the 79-page argument. Instead, the proof is audited as a dependency structure.

The source proof can be read as four major layers:

### Layer A — Gaussian comparison problem

A Gaussian surrogate of the fitting problem is analyzed first. The central optimization problem is reduced to a tractable asymptotic variational form using the Convex Gaussian Min-Max Theorem (CGMT).

This layer identifies the candidate threshold \(\alpha_\star(\kappa)\) and the associated UNSAT error formula.

**Audit status:** source-dependent.

MB_0005 checks that the threshold object used in the statement matches the source definition and that the Gaussian specialization gives \(\alpha_\star(3)=1/4\). It does not independently re-prove the CGMT reduction.

### Layer B — Phase-boundary analysis

The resulting scalar/spectral variational problem is analyzed to establish the location and properties of \(\alpha_\star(\kappa)\), including its dependence on \(\kappa\).

This is the layer where the phase boundary becomes a mathematical object with its own definition and properties rather than merely a condition inside the theorem statement.

**Audit status:** source-dependent with formula-level checks.

MB_0005 independently checks algebraic specializations that are directly accessible from the stated formulas, especially the Gaussian case \(\kappa=3\).

### Layer C — Universality transfer

The source then transfers the Gaussian-model result to the broader independent-coordinate subgaussian setting.

This step uses a Lindeberg-type universality argument built around self-concordant barriers and matching low-order coordinate information.

The result is that the asymptotic phase boundary depends on the coordinate distribution through

\[
\kappa=\mathbb E[x_{1j}^4].
\]

**Audit status:** source-dependent.

MB_0005 does not independently reproduce the self-concordant-barrier/Lindeberg proof.

### Layer D — Exactification / anti-concentration

Approximate fitting and exact fitting require distinct arguments. The exact SAT result requires an anti-concentration step beyond concentration-style universality.

The source uses random-matrix anti-concentration machinery to pass from approximate control to exact fitting in the SAT regime.

This distinction is load-bearing: source assumptions sufficient for approximate control need not automatically imply exact fitting.

**Audit status:** source-dependent.

MB_0005 records this dependency explicitly rather than presenting exact fitting as a direct consequence of the numerical experiment or of the variational threshold alone.

---

## 4. Audited implication chain

The proof audit supports the following source-dependent implication chain:

```text
coordinate assumptions + asymptotic regime
                |
                v
Gaussian comparison / variational problem
                |
                v
explicit alpha_star(kappa)
                |
                v
universality transfer
                |
                v
SAT region / UNSAT region
                |
                +--> SAT exactification requires anti-concentration
                |
                +--> UNSAT regime yields positive asymptotic fitting error
```

The project audits this chain but does not replace any of its deep arrows with an independent first-principles proof.

---

## 5. What MB_0005 independently checks

MB_0005 can independently check several components without claiming to re-prove Theorem 1.2.

### 5.1 Statement consistency

The source assumptions, theorem directions, and phase-boundary definition are checked for internal consistency across the theorem statement, phase-boundary formulas, and numerical appendix.

### 5.2 Gaussian specialization

Setting

\[
\kappa=3
\]

removes the \((\kappa-3)/2\) term, giving

\[
\omega_\kappa=0
\]

and therefore

\[
\alpha_\star(3)=\frac14.
\]

This is a direct formula-level check.

### 5.3 Finite-dimensional computational realization

At a chosen dimension such as

\[
d=40,
\]

the Gaussian asymptotic boundary predicts the transition scale

\[
n\approx\alpha_\star d^2
=
\frac14(40)^2
=
400.
\]

An executable can sample Gaussian vectors and solve the corresponding semidefinite feasibility problem at several \(n\) values around this scale.

### 5.4 Direct solution validation

A solver-reported feasible result is accepted as a computational SAT reading only after checking the returned matrix directly.

For a candidate \(R\), the executable checks:

\[
\max_i |x_i^\top R x_i-1|
\]

and the minimum eigenvalue

\[
\lambda_{\min}(R).
\]

This separates:

```text
solver status
    ->
constraint validation
    ->
computational reading
```

A solver status alone is not treated as the reading.

---

## 6. What the executable does not verify

The executable does not verify:

- the high-probability asymptotic theorem as \(n,d\to\infty\);
- the CGMT reduction;
- the self-concordant-barrier universality argument;
- the random-matrix anti-concentration argument;
- universality across all distributions covered by the theorem;
- the exact critical behavior at \(\alpha=\alpha_\star(\kappa)\);
- the full UNSAT error formula throughout the asymptotic regime.

A finite-dimensional run is therefore classified as a computational reading relative to the asymptotic specification.

It is evidence of consistency with the theorem, not an independent proof of the theorem.

---

## 7. Scope distinctions preserved by the audit

### Domain constraints

These specify the random-vector model and asymptotic regime.

### Specification boundary

\[
\alpha_\star(\kappa)
\]

partitions parameter space into SAT and UNSAT regions.

### Excluded generalizations

These identify claims the source does not warrant, including unrestricted dependent-coordinate SAT claims and algorithmic-efficiency claims.

### Computational readings

These are finite-dimensional outcomes produced by an SDP and validated directly.

These roles remain distinct throughout MB_0005.

---

## 8. Verification classification

```yaml
verification:
  mathematical:
    status: audited
    meaning: >
      The source theorem, assumptions, formulas, and proof dependency structure
      were inspected for consistency. The deep proof machinery was not
      independently re-derived.
  computational:
    status: supported
    meaning: >
      A finite-dimensional SDP realization can be reproduced and its returned
      matrices directly checked against the quadratic equalities and PSD
      requirement.
  theorem_from_computation:
    status: unsupported
    meaning: >
      Finite-dimensional computational agreement is not treated as verification
      of the asymptotic high-probability theorem.
```

---

## 9. SG-3 architectural result

MB_0005 supplies a third structural role distinct from both domain constraints and theorem exceptions.

The role is:

```yaml
specification_boundary
```

Its defining behavior is:

```text
domain constraints:
    determine which objects and regimes are admissible

specification boundary:
    partitions admissible parameter space by conclusion

theorem exceptions:
    carve hypothesis-satisfying objects out of a conclusion

excluded generalizations:
    mark claims outside source-supported scope
```

For this specimen,

\[
\alpha_\star(\kappa)
\]

is therefore retained as a specimen-level `specification_boundary`.

Whether this field generalizes into the shared mathematical-basis schema remains an open architectural question until additional specimens exhibit the same role.

---

## 10. Proof-audit verdict

The source supports the MB_0005 statement at the level appropriate for an audited mathematical artifact.

The project has not independently re-derived the theorem and should not label it `proved`.

The finite-dimensional executable is appropriate as a computational realization because it tests a concrete reading predicted by the Gaussian specialization while preserving the distinction

\[
\text{asymptotic specification}
\neq
\text{finite computational reading}.
\]

**Proof status: audited.**

**Next artifact:** `tests/MB_0005_ellipsoid_fitting_verification.py`.
