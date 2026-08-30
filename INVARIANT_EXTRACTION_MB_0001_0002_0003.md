# Invariant Extraction: MB_0001 / MB_0002 / MB_0003

Built by direct comparison of the three statement YAMLs, proofs, tests, and results — not by assumption. Where something looked invariant but wasn't, that's flagged rather than smoothed over.

## Genuinely invariant (candidates for specification-grammar)

**1. Top-level statement structure, exact and identical across all three:**

```
statement: {id, title, repository}
status: {mathematical, computational, provenance, publication}
source_provenance: [{source_ref, role, original_claim, original_claim_status, note}]
specification: {domain, statement, leading_constraints, excluded_generalizations, <one domain-specific field>}
verification: {proof_ref, executable_ref}
result: {result_ref, claim_status, summary}
footer: {principle}
```

Verified by direct `grep` against all three files, not recalled from memory — this document's first draft assumed a discrepancy that turned out to be a grep-pattern artifact, not a real one; worth noting since it's exactly the kind of error this project's own discipline exists to catch.

**2. The four-axis status split** (`mathematical` / `computational` / `provenance` / `publication`), each independently gradable, present verbatim in all three. This is the single most load-bearing invariant — it's what made MB_0003's proof/verification separation a checkable question rather than a vibe.

**3. `specification` always carries `leading_constraints` and `excluded_generalizations` as separate lists.** Every statement names what it does NOT claim, distinct from what it does. This is not incidental — MB_0001's excluded_generalizations blocks the 9423 correspondence from being read back into the theorem; MB_0002's blocks over-generalizing to arbitrary C4×C2 groups; MB_0003's blocks over-generalizing to other Fano labelings. Three different domains, same structural role.

**4. `footer.principle` is the literal string "Admissible generalizations trail leading specifications" in all three**, unchanged. Whether this specific sentence belongs in specification-grammar itself or stays a mathematical-basis convention is a real question — it's invariant here because all three statements were written under the same standing instruction, not because three independent domains converged on it.

**5. A specialization is always a *reading* of the leading specification, never a separately-discovered fact.** MB_0001: C(6)=3 is a reading of C(m)=m/φ(m), not a fact found first and generalized after. MB_0002: the three quotient types are readings of "quotient depends on subgroup choice," not three unrelated computations. MB_0003: 16 is 2^rank(M), read off the leading specification's structure, not a count that got explained afterward. In all three, the *order of discovery* in this project's own history sometimes went numeral-first (MB_0001's 24/25→3 correction genuinely started numerically) — but the *final statement* always presents the general form first and the number as its consequence. Worth being honest that this ordering is an editorial choice imposed on the write-up, not always the actual discovery order.

**6. Result files are captured, not asserted**: every `results/*.yaml` embeds the literal JSON a test actually printed, plus `executable_sha256` and `run_timestamp_utc`. All three have `commit_hash: null` rather than a fabricated value, for the same reason in each case (no git checkout exists in this environment).

## Invariant only after active correction — worth flagging, not smoothing over

**Proof independent of verification did NOT hold automatically for MB_0003.** MB_0001's and MB_0002's proofs were derived analytically before their tests were written to check them — the separation was clean from the first draft in both cases. MB_0003's first draft was different: Part 4 originally used the exhaustive 128-case count as a load-bearing step in closing the proof, exactly the failure mode the five-stage contract is meant to prevent. It took explicit review pressure (twice — once to make the classification analytic at all, once more to replace a rank comparison with the CM≡0 algebraic identity) to actually achieve the separation.

This matters for what gets extracted: **"proof and verification are separate roles" is the right invariant to name, but it is not self-enforcing by file layout alone.** A `proofs/` directory existing next to a `tests/` directory doesn't stop a proof file from quietly leaning on the test's output. What actually caught it was a specific, askable question: *does this proof's argument cite the test's result as evidence for a step it hasn't independently established?* That question — not just the directory split — is the thing worth carrying into specification-grammar, probably as an explicit review checklist item rather than an assumed consequence of the architecture.

## Explicitly NOT invariant — domain-specific, do not extract

- **Verification style.** Numerical sweep (MB_0001) vs. exact finite enumeration (MB_0002) vs. analytic derivation + exhaustive combinatorial check (MB_0003) are genuinely different, and that was the point of choosing three specimens this different. Specification-grammar should not prescribe *how* verification happens.
- **Proof artifact weight.** MB_0001 has a full paper (`papers/density-correction/`); MB_0002 and MB_0003 have single-file proofs under `proofs/`. The README already states the rule correctly: "the invariant should be proof, not paper."
- **The relationship between statement and source varies genuinely, not just cosmetically**: MB_0001 corrects a wrong source claim; MB_0002 independently re-derives a claim from an informal discussion; MB_0003 extends a correct source construction past what it itself claimed. `original_claim_status` takes three different values (`superseded` / `independently_reverified` / `independently_reverified_and_extended`) precisely because these are three different relationships, not one relationship expressed three ways.
- **The domain-specific `specification` field** (`specializations` / `project_interpretation`+`element_orders`+`quotients` / `structural_explanation`) is exactly where each statement's actual mathematical content differs — this is the extension point, not something to standardize away.

## What this suggests for specification-grammar

Extract: the seven-key top-level shape, the four-axis status split, the leading_constraints/excluded_generalizations pairing, the captured-result convention (hash + timestamp + no fabricated commit hash), and — as a checklist item, not a structural guarantee — the proof-independence question that MB_0003 failed on its first draft.

Do not extract: anything about verification method, proof format/length, or the specific content shape of the domain-specific specification field. Those three are supposed to keep varying as new domains arrive; standardizing them would defeat the point of having tested three different ones.
