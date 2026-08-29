# sources/mb_0001/

## persist.pdf

Draft v1.1, dated March 11, 2026. thinkthoughts — github.com/thinkthoughts.

Preserved verbatim, unedited. This is the historical hypothesis source for `statements/MB_0001_RESIDUE_CONDITIONING.yaml`, not a verified result in its own right.

Its central claim — that a normalized residue-counting ratio r(L, Pk) converges to 24/25 for m=6, a=5 — did not reproduce when its own stated verification code (its Appendix A) was run. The true limit is C(6) = 3 against the naive predictor the paper itself defines, and 1 against its own Lemma 1's refined heuristic, which was correct but not carried through to the paper's stated conclusion.

sha256: `8faa1cc0d02b6498b7e41906d80ce67dcb51bfb982aed9e41e96b3d3a17cb046`

## Role

Motivating source only. `papers/density-correction/paper.md` generalizes past this document's specific case (m=6, a=5) to the full statement in `MB_0001_RESIDUE_CONDITIONING.yaml`; the audit that found the discrepancy is recorded in the residue-manifold-learning repository's `tests/basis/`, not duplicated here.
