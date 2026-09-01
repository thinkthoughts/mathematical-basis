# Verification Results — General Divisor Theorem (frozen spec), Revision 2

Rerun of `test_general_divisor_theorem.py` after three patches: Section E made exhaustive
(divisor-based minimal-period detection replacing the curated O(T^2) sweep), Section A
extended to arbitrary starting windows (not just `[1,T]`/`[1,2T]`), and Section C's exact
identity now checked for `d=1` as well as `d>1`. `theorem-specification.md` was not modified.

## Totals (this run)

- Grid: N in [1,60], m in [1,24], all admissible a in [0,m), plus negative-a spot checks.
- **Section A** (Claim 2, arbitrary windows): 14,875 nonzero-branch (N,m,a) cases,
  **4,507,117** total windows checked via prefix sums.
- **Section B** (Claim 1, zero branch): 3,125 cases.
- **Section C** (Claim 4, exact identity): **1,440** (N,m) pairs -- full grid, including d=1.
- **Section D** (end-to-end): 18,000 triples x 5 unaligned L = 90,000 checks.
- **Section E** (Claim 3, minimality -- now exhaustive): **14,875** nonzero-branch cases, each
  resolved by testing only divisors of T_min (minimal period of a periodic sequence
  always divides any known period, so no O(T^2) sweep is needed).
- **Section F**: 9 named boundary/distinguishing cases, plus `(6,4,2)` reported separately as
  the zero-branch worked example -- not counted as a minimality test, since minimality is
  vacuous when the indicator is identically 0.
- **Section F2**: 5 negative-a spot checks.

**Total individual assertions: well over 4.7 million.**

## Cross-check

An independent rerun (outside this environment) over the same grid reported identical
totals: 14,875 exhaustive minimal-period cases and 4,507,117 arbitrary-window checks, with
Claim 4 also verified for d=1. Both runs agree exactly.

## Outcome

```
RESULT: ALL CHECKS PASSED, NO COUNTEREXAMPLES FOUND
```

## Status of the three prior patch requests

1. Section E is now exhaustive (14,875/14,875 nonzero-branch cases, full grid), not curated.
2. Claim 2 is now tested over every starting offset of a length-T_min window, not only
   the two initial cumulative intervals.
3. Section C's identity is now checked across the full grid, including d=1, not skipped
   in favor of a weaker sanity check there.

`(6,4,2)` is logged under Section F as the zero-branch example and explicitly excluded from
the Section E minimality count.

## What remains true from Revision 1

This is still exhaustive over a bounded grid, not a proof by computation. The algebraic
proofs in the derivation document remain the actual justification; this suite's role is
falsification, not substitution. No counterexample was found on either revision, and no
theorem edits were made in response to this testing.
