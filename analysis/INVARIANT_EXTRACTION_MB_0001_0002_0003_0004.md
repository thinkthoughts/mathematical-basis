# Invariant Extraction: MB_0001 / MB_0002 / MB_0003 / MB_0004

Built by direct comparison of all four statement YAMLs, proofs, and results — re-run against the actual files, not carried forward from the three-specimen extraction's conclusions. Where Cycle 1's findings still hold, that's stated as re-confirmed, not assumed.

## Still genuinely invariant, now confirmed across a fourth, structurally different specimen

**1. The seven-key top-level envelope is exact across all four**, verified by direct grep, not recollection: `statement / status / source_provenance / specification / verification / result / footer`, in that order, in every one of MB_0001–4. MB_0004 is a graph-theory audit of someone else's proof, structurally as different from MB_0001–3 as sensors-becker was from all of them — and the envelope held anyway.

**2. `specification` still always carries exactly `domain`, `statement`, `leading_constraints`, `excluded_generalizations`, plus one domain-specific extension field.** Confirmed again: MB_0004 uses `theorem_exceptions`, a fourth distinct extension name.

**3. The four status axis *names* (`mathematical`/`computational`/`provenance`/`publication`) are still invariant. The *vocabulary of values within an axis* is not closed — and MB_0004 changed it.** This is the important refinement Cycle 1 didn't have evidence for: `mathematical` gained a second legitimate value, `audited`, distinct from `proved`. The axis structure held; the value set inside one axis did not. This should be recorded precisely, not rounded up to "the status system worked" or down to "the status system broke."

## The three things explicitly not to assume — checked against evidence, not decided by fiat

**Is `theorem_exceptions` universal?** No evidence either way yet — it appears exactly once, in MB_0004, because MB_0004 is the only specimen so far whose leading theorem has hypothesis-satisfying necessary exceptions. MB_0001–3 didn't need it because none of their claims had this shape. A fifth specimen with a similar shape (a sharp threshold with boundary exceptions) would be needed to know whether `theorem_exceptions` recurs as a pattern or was a one-off binding for one paper's specific structure. Currently: **one data point, not a pattern.**

**Does `audited` belong in a universal SG status vocabulary?** Also one data point. What's more precisely established is the *distinction* `audited` was introduced to name — MB_0004's proof is genuinely different in kind from MB_0001–3's (a structural check of an existing multi-page proof vs. an argument this project derived from scratch) — not that the specific word "audited" is the right universal term for it. A different domain might need a different word for the same underlying distinction, or might not need the distinction at all if every claim in it happens to be independently re-derivable at a scale this project can manage (as MB_0001–3 were).

**Are sensors-becker's V1/V2/V3 and MB_0004's execution-success-vs-claim-coverage finding one hierarchy?** Checked directly, and they don't obviously collapse into each other. V1/V2/V3 is about *what kind of thing* a check examines — structural integrity, source-content accuracy, cross-artifact consistency — three different objects being checked. MB_0004's finding is different in kind: the *same* check, examining the *same* object (does this graph violate the theorem), silently narrowed its own enumeration domain and never tested one of the two cases it existed to test. That's not "checking a different layer" (V1 vs V2 vs V3) — it's "the check's own scope was wrong regardless of which layer it targeted." A plausible shared meta-principle — *a passing verification's actual coverage must itself be checked, separately from whether it passed* — might unify these, but that's speculative pattern-matching across genuinely different failure modes, not a confirmed finding. Recorded as an open hypothesis, not folded into SG-6 or SG-anything yet.

## A finding this extraction has that Cycle 1 didn't: source relationships form a genuine spectrum, not three types

Cycle 1 named three source-provenance relationships (correction, independent re-derivation, extension). MB_0004 adds a fourth, and the four are precisely distinguishable by `source_provenance.original_claim_status`, checked directly across all four files:

| Specimen | `role` | `original_claim_status` | Relationship |
|---|---|---|---|
| MB_0001 | historical_hypothesis_source | `superseded` | Source's specific claim was wrong; corrected and generalized |
| MB_0002 | motivating_prior_discussion | `independently_reverified` | Source was informal/unwritten; independently re-derived from scratch |
| MB_0003 | canonical_reference | `independently_reverified_and_extended` | Source's specific claim was correct; extended past what it claimed |
| MB_0004 | canonical_reference | `independently_reverified` | Source's claim re-verified as stated; not extended, not corrected |

MB_0003 and MB_0004 share a `role` (canonical_reference) but differ in `original_claim_status` (extended vs. not) — confirming the two fields are doing genuinely independent work, not redundant ones. Worth carrying into any future SG treatment of provenance: it's at least a two-dimensional space (how authoritative was the source; what did this project do with it), not a single "how was it used" label.

## What this extraction does not do

It does not revise SG_0001. It does not resolve whether `theorem_exceptions`, `audited`, or a unified verification-depth hierarchy should become general rules — each is left exactly as open as the evidence currently supports, which in all three cases is "one specimen's worth," not enough to generalize from without doing to SG what MB_0004's own first draft did to itself: mistaking a passing single case for established coverage.
