# RO_B — Mathematical Basis: the pipeline, walked through via MB_0001

## The pipeline

```
source provenance  →  leading specification  →  executable verification  →  result
sources/mb_0001/      statements/MB_0001_...     tests/MB_0001_...          results/MB_0001_...
persist.pdf            .yaml                      .py                        .yaml
```

Each stage is a separate artifact, in a separate directory. None of them is allowed to stand in for another:

- A source is preserved as originally written, even where it's wrong. `sources/mb_0001/persist.pdf` still says r(L,Pk) → 24/25. That line is not corrected in place — it's audited, and the audit lives elsewhere.
- A statement is the general claim, stated once, independent of any specific run of a script. `statements/MB_0001_RESIDUE_CONDITIONING.yaml` states C(m) = m/φ(m) for general m; it does not itself contain a computed number.
- A verification is code, not prose. `tests/MB_0001_general_sweep.py` is run, not summarized from memory.
- A result is what that code actually printed, on a specific run. `results/MB_0001_general_sweep.yaml` is that printout, timestamped and attributable to a specific execution of the test file above it — not a restatement of what the result was expected to be.

## How MB_0001 moved through the pipeline

1. `sources/mb_0001/persist.pdf` (v1.1) claimed a specific numerical constant, 24/25, for a specific case (m=6, a=5), based on a numerical table that did not reproduce under its own stated verification code.
2. Auditing that source (`tests/basis/` in the residue-manifold-learning repo) found the true limit was 3 against the paper's own naive predictor, and that the paper's own Lemma 1 already contained the correction, unapplied.
3. Generalizing past the single case (m=6, a=5) produced a stronger, more general leading specification: C(m) = m/φ(m) for any squarefree m dividing a primorial Pk, independent of which admissible residue a is chosen. That generalization is `statements/MB_0001_RESIDUE_CONDITIONING.yaml`.
4. The generalization was not accepted on the strength of the m=6 case alone. `tests/MB_0001_general_sweep.py` was written to check it across m ∈ {6,10,30} and every admissible residue for each, and was run before the statement was finalized, not after.
5. `results/MB_0001_general_sweep.yaml` records that run's actual output, including the one place a naively-set tolerance produced a false negative (m=30, a=1, smallest L) — kept in the result rather than silently corrected, because the fix to the test's tolerance logic is itself part of the provenance of why the claim is trusted.

## What this pipeline is for

Not process for its own sake. `sources/mb_0001/persist.pdf`'s original 45° claim about the 9423 construction (§3 of the paper) went through the same audit process and did not survive it — the pipeline is only useful if it's equally willing to reject a claim as to confirm one. MB_0001 exists because it passed; the 9423 correspondence is documented in the paper precisely because it didn't, and is kept as a worked example rather than deleted.
