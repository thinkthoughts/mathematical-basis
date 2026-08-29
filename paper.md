# Density Correction under Residue Conditioning in Primorial Systems

thinkthoughts — github.com/thinkthoughts

Draft v3.1 — supersedes Draft v3.0 (standardizes the refined-density identity, sharpens the label/reading/specification distinction, tightens Pi/π/Π to precise operational mappings, retitles). v1.1 (`paper/persist.pdf`) is retained as historical basis under `results/basis/`, with its original claims preserved verbatim there per the audit in `tests/basis/`.

## Abstract

Let Pk be the k-th primorial (squarefree, the product of the first k primes), let m be any squarefree divisor of Pk with m > 1, and let a be any integer with gcd(a, m) = 1. We show that the count

  S(Pk, L, m, a) = { n ≤ L : n ≡ a (mod m), gcd(n, Pk) = 1 }

departs from the naive independent-density prediction (φ(Pk)/Pk)·(L/m) by an exact, computable factor

  C(m) = m / φ(m),

independent of which admissible residue a is chosen, with an exact per-period count and a bounded remainder term. This generalizes and completes an earlier draft's numerically-motivated observation about the specific case m = 6, a = 5, which had reported an incorrect limiting constant of 24/25; the corrected case gives C(6) = 3. We also examine a weighted-vector construction previously labeled a correspondence to a 45° diagonal direction, find that the two objects do not even share the claimed reading, and use the discrepancy as a worked example of a three-level distinction: a shared label does not establish a shared reading, and even a shared reading would not, on its own, establish a shared specification.

## 1. Setup

Let Pk = p1 p2 ⋯ pk denote the k-th primorial (the product of the first k primes, p1=2, p2=3, …). Pk is squarefree by construction. Let m be a squarefree divisor of Pk with m > 1, and let a be an integer with gcd(a, m) = 1 — i.e., a names an admissible residue class modulo m. Define

  S(Pk, L, m, a) = { n ≤ L : n ≡ a (mod m), gcd(n, Pk) = 1 }.

The naive density heuristic treats the residue condition and the coprimality condition as independent: density 1/m from the residue class, times φ(Pk)/Pk from coprimality to all of Pk, giving

  |S(Pk, L, m, a)| ≈ (φ(Pk)/Pk) · (L/m).

This double-counts: since gcd(a, m) = 1, every n satisfying n ≡ a (mod m) is already coprime to every prime dividing m, so the φ(Pk)/Pk factor re-imposes a restriction the residue condition has already enforced for the primes dividing m.

## 2. The Density-Correction Theorem

**Theorem 1 (General form).** With Pk, m, a as above, and writing the exact per-period count and a bounded boundary term for general L:

For L = qPk + s with 0 ≤ s < Pk,

  |S(Pk, L, m, a)| = q · φ(Pk/m) + R(s),

where R(s) = |{ n ≤ s : n ≡ a (mod m), gcd(n, Pk) = 1 }| is the exact count within the partial final period, satisfying 0 ≤ R(s) ≤ ⌈s/m⌉.

The naive predicted count over the same range is (φ(Pk)/Pk)·(L/m). The ratio of exact count to naive predicted count converges, as L → ∞, to

  C(m) = m / φ(m),

independent of the specific admissible residue a chosen.

**Proof.** Since m | Pk and Pk is squarefree, m and Pk/m are coprime and squarefree, and Pk/m consists exactly of the prime factors of Pk not dividing m. Within one period [1, Pk], exactly Pk/m integers satisfy n ≡ a (mod m). By the Chinese Remainder Theorem, since m and Pk/m are coprime, the residue of n modulo Pk/m is independent of, and ranges uniformly over all values as, n ranges over its fixed class mod m within [1, Pk]. Hence exactly the fraction ∏_{p | Pk/m} (1 − 1/p) = φ(Pk/m)/(Pk/m) of these Pk/m values are additionally coprime to every prime dividing Pk/m. Since gcd(a, m) = 1, these values are already coprime to every prime dividing m. So the exact count per period is

  (Pk/m) · φ(Pk/m)/(Pk/m) = φ(Pk/m).

This count does not depend on the specific value of a beyond gcd(a, m) = 1, since the argument only used that n's residue mod m is fixed and coprime to m — establishing the claimed independence from a.

Using φ(Pk) = φ(m)·φ(Pk/m) (multiplicativity, valid since m and Pk/m are coprime), φ(Pk/m) = φ(Pk)/φ(m).

The naive predicted count per period is (φ(Pk)/Pk)·(Pk/m) = φ(Pk)/m.

The ratio is therefore

  [φ(Pk)/φ(m)] / [φ(Pk)/m] = m/φ(m) = C(m),

exact per period and independent of k. Periodicity with period Pk gives the general-L statement with bounded remainder as above. ∎

**Standardized refined-density identity.** Throughout this paper, the refined predicted count is written in the equivalent forms

  E_refined(L) = (L/m) · ∏_{p | Pk/m} (1 − 1/p) = L · φ(Pk/m)/Pk,

which are equal since (L/m)·φ(Pk/m)/(Pk/m) = L·φ(Pk/m)/Pk. Both forms are used interchangeably below; this identity is why they agree.

**Corollary 1 (m = 6 case).** For m = 6, a ∈ {1, 5} (the two residues mod 6 coprime to 6):

  C(6) = 6/φ(6) = 6/2 = 3.

This corrects the earlier draft's reported limiting constant of 24/25 for the case a = 5. Against the refined predicted count E_refined(L) = L·φ(Pk/6)/Pk (see the standardized identity above), the ratio is exactly 1.

**Corollary 2 (combined residue classes).** Since the per-period count φ(Pk/m) is independent of which admissible a is used, the same ratio C(m) holds for any union of admissible residue classes mod m — for instance n ≡ 1 or 5 (mod 6) together give the same ratio 3 as either individually, since both the exact and naive counts scale by the same factor (the number of residues unioned).

Both corollaries were verified numerically at Pk = 210 (m = 6, 10, 30; multiple values of a; L up to 10^7), matching the predicted C(m) to five decimal places or better in every case, and matching the exact per-period counts φ(Pk/m) precisely; see `tests/basis/test_persistent_constant.py`.

## 3. A Failed Correspondence as a Reading-Point Example

An earlier draft defined a weighted tuple (9, 4, 2, 3) with angles θ_k ∈ {0°, 60°, 120°, 180°} and

  V = Σ_{k=1}^{4} w_k e^{iθ_k} = 9 + 4e^{iπ/3} + 2e^{i2π/3} + 3e^{iπ} = 7 + 3√3 i,

reporting its reading as

  r_V = arg(V) ≈ 36.586776°.

The same draft separately noted that the point (1, 1) has reading

  r_D = arg(1 + i) = 45°,

and described the combination as a "9423 phase-lock representation," implying a correspondence between the two constructions. Since r_V ≠ r_D, no such correspondence holds under the stated construction. An exhaustive search over all 24 permutations of assigning the four weights to the four fixed angles confirms this is not an artifact of ordering: no permutation reaches exactly 45°, with the closest approaches at 43.898° and 46.102° (`tests/basis/test_9423_phase_lock.py`).

This is a useful example independent of whether the specific construction is later revived, because it isolates a three-level distinction:

  shared label  ⇏  shared reading  ⇏  shared specification.

The draft's own label, "9423 phase-lock representation," was shared across both objects by assertion — but the readings it named are not shared: r_V = 36.586776° ≠ r_D = 45°. That is the first level failing outright. The second level is a counterfactual worth stating separately: **even had r_V equaled r_D exactly, that alone would not establish a structural correspondence between V's construction and the point (1,1)** — no transformation, projection, or limiting operation connecting the two objects would thereby be specified. A shared label asserts a correspondence; a shared reading is, at most, evidence that two objects were run through procedures producing the same observable category; neither, on its own, specifies the correspondence itself.

Section 2 gives a cleaner instance of the same principle from this paper's own corrected mathematics. The single normalized ratio r(L, Pk) for m=6, a=5 has taken three different numerical values in the course of this paper's development:

  24/25  (originally reported, against no explicitly stated refined baseline)
  3      (against the naive predictor (φ(Pk)/Pk)·(L/6))
  1      (against the refined predictor φ(Pk/6)/Pk · L)

None of these numbers is meaningful without specifying which predictor produced it. The number alone is insufficient; the reading requires its producing specification to be stated alongside it.

## 4. Numerical Verification

At Pk = 210 = 2·3·5·7, m = 6, a = 5:

| L | actual | naive predicted | naive ratio | refined predicted | refined ratio |
|---|---|---|---|---|---|
| 10^5 | 11,428 | 3,809.52 | 2.99985 | 11,428.57 | 0.99995 |
| 10^6 | 114,285 | 38,095.24 | 2.99998 | 114,285.71 | 0.99999 |
| 10^7 | 1,142,856 | 380,952.38 | 3.00000 | 1,142,857.14 | 1.00000 |
| 10^8 | 11,428,571 | 3,809,523.81 | 3.00000 | 11,428,571.43 | 1.00000 |

Additional verification across m ∈ {6, 10, 30} and all admissible a mod m confirms C(m) = m/φ(m) exactly (C(6)=3, C(10)=2.5, C(30)=3.75), and confirms the exact per-period count φ(Pk/m) independent of a, at Pk = 210, L up to 10^7 (`tests/basis/test_persistent_constant.py`).

## 5. Conclusion

The density-correction factor C(m) = m/φ(m) is a general, exact, elementary consequence of conditioning a coprimality count on a residue class already coprime to the modulus — proved here via the Chinese Remainder Theorem and multiplicativity of φ, requiring no sieve-theoretic or analytic machinery. The m=6 case, C(6)=3, corrects an earlier draft's reported constant of 24/25. A separate weighted-vector construction claimed to correspond to a 45° diagonal direction does not, under exhaustive search, and is retained here as a worked example where a shared label fails to establish a shared reading, while the corrected density theorem shows why a numerical reading must be interpreted together with its producing specification.

## Appendix A: Verification Code

```python
from math import gcd
from sympy import totient, primefactors

def naive_predicted(limit, primorial, m):
    density = totient(primorial) / primorial
    return density * (limit / m)

def count_residue(limit, primorial, m, a):
    c = 0
    n = a
    while n <= 0:
        n += m
    for n in range(n, limit + 1, m):
        if gcd(n, primorial) == 1:
            c += 1
    return c

def refined_predicted(limit, primorial, m):
    # density = product over primes dividing Pk but NOT dividing m
    m_primes = set(primefactors(m))
    dens = 1.0
    for p in primefactors(primorial):
        if p not in m_primes:
            dens *= (1 - 1.0 / p)
    return dens * (limit / m)
```

(Full runnable versions, including the general (m,a) sweep and the permutation search for §3: `tests/basis/test_persistent_constant.py`, `tests/basis/test_9423_phase_lock.py`.)

## References

[1] G. H. Hardy and E. M. Wright, *An Introduction to the Theory of Numbers*, Oxford University Press. (Chinese Remainder Theorem, Euler's totient function and its multiplicativity.)

---

## Appendix B: Project Vocabulary (non-standard notation, not part of the theorem above)

The three operations below are project-specific specification vocabulary developed in connection with this result. They are not standard mathematical terminology and are stated separately from Theorem 1 so the theorem itself remains legible to a reader unfamiliar with the project.

- **Pi — expand.** m ↦ ℤ/mℤ: exposing the complete residue/state space for a given modulus, before any restriction is imposed on it.
- **π — extend.** Pk ↦ Pk+1 = pk+1 · Pk: adding another specification/constraint by extending the primorial by one further prime.
- **Π — resist.** ∏_{p | Pk/m} (1 − 1/p): the fraction of candidates remaining admissible under the divisibility constraints not already imposed by the residue condition — the quantity appearing directly in the proof of Theorem 1.

These give the progression Pi (expand) → π (extend) → Π (resist) → r (read), naming the roles already present in Theorem 1's proof.

These names are labels for roles already present in Theorem 1's proof; the proof itself does not depend on this vocabulary and holds independently of it.
