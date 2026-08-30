# Proposed SG_0001 Revision Memo

Compares `mathematical-basis/analysis/INVARIANT_EXTRACTION_MB_0001_0002_0003_0004.md` against the current `specification-grammar/SG_0001_SPECIFICATION_ROLES.md`. This is a proposal, not an edit — nothing in `SG_0001_SPECIFICATION_ROLES.md` is changed by this document. Organized into the four categories requested: what four MB specimens now support, what MB_0004 alone supports, what sensors-becker separately contributes, and what remains open.

## A. Invariants now supported by four MB specimens (reconfirmed, not just carried forward)

- **SG-1's seven-key envelope.** Reconfirmed exactly on a fourth specimen structurally unlike the first three — a graph-theory audit of someone else's proof, not a self-derived result. The envelope held without modification.
- **SG-3's constraints/boundary pairing** (`leading_constraints` + `excluded_generalizations`). Still present, still doing real work, in MB_0004 — but MB_0004 also required a third field (`theorem_exceptions`) alongside the pair, which the pairing alone couldn't express. The two-field pairing is confirmed as necessary; MB_0004 shows it isn't always sufficient. (Full treatment in category B.)
- **SG-6's core claim — proof and verification are distinct roles.** MB_0004 gives this the cleanest demonstration yet: the proof is explicitly labeled an audit, is structurally separate from the test from the first draft (unlike MB_0003, which violated this and had to be fixed), and both proof and test honestly name the *same* gap (Lemma 3.5) rather than either one silently claiming to cover it. This is stronger evidence than a fix-after-violation; it's a case where the separation was designed in and held.
- **SG-5's provenance-honesty pattern.** `commit_hash: null` with an explanatory comment, not a fabricated value, reconfirmed identically in MB_0004's results file.
- **SG-7's extension-point claim.** `theorem_exceptions` is a fourth distinct domain-specific extension field, exactly the pattern SG-7 predicts. Directly reconfirming.

None of these require wording changes to SG_0001 as currently written — they're re-confirmations, not new information the current text is missing.

## B. Findings supported by MB_0004 alone (one data point each — not yet proposed for SG)

- **A three-way split, not the two-way split SG-3 currently states.** MB_0004's theorem has domain constraints (finite simple graph, k-connected, degree threshold), a claim (existence of a k-removable matching), and a set of necessary exceptions that satisfy the domain constraints yet must still be excluded from the claim. That's a structurally distinct third category from both "constrains the object" and "extends outside the claim" as SG-3 currently frames the pairing. `theorem_exceptions` was introduced as an SG-7 extension specifically so this wouldn't force a premature SG-3 rewrite. One specimen. Not proposed for promotion yet — needs a second specimen with a similar shape (a sharp threshold with in-domain boundary exceptions) to know if this recurs or was a one-off binding for this one paper.
- **Status-value vocabulary is open within a fixed axis name.** `mathematical` gained `audited` as a legitimate second value, distinct from `proved`. This is evidence for something SG-2 doesn't currently say: SG-2 covers *how many axes* and *where they live structurally*, not *whether the set of values an axis can take is closed*. One data point (one axis, one new value, one specimen).
- **Execution success is not claim coverage, and this is a different failure mode from sensors-becker's V1/V2/V3.** The extraction document already stated this as an explicit "no, not yet" rather than folding it into SG-6. Repeating it here as a reminder: this needs a genuinely independent second example (ideally outside both mathematical-basis and graph theory) before it's more than one incident.
- **Provenance may be two-dimensional** (`role` × `original_claim_status`), not one label. MB_0003 and MB_0004 share a `role` (`canonical_reference`) but differ in `original_claim_status` (extended vs. re-verified-as-stated), showing the two fields carry independent information. This is drawn from comparing all four specimens, but the distinguishing evidence is specifically the MB_0003/MB_0004 pair — closer to "two data points that happen to differ" than "four specimens converging on a pattern."

None of these four are proposed for SG_0001 yet. Each is one specimen's worth (or a pair's worth) of evidence, and SG_0001's own history (built from three specimens that all happened to share a mod-30 context, later found to need real correction from sensors-becker) is the argument for waiting rather than generalizing early.

## C. Cross-domain evidence from sensors-becker (already reflected in SG_0001; noted here only where MB_0004 changes the picture)

SG-1's "roles need not be co-located" and SG-2's "gradability may be structurally distributed" both rest entirely on sensors-becker's evidence, not MB_0001–4's — all four MB specimens keep every role in one file, so MB_0004 neither reinforces nor weakens those two claims. Worth stating plainly so a future reader doesn't assume MB_0004 adds weight there; it doesn't.

SG-3's domain-constraint/claim-boundary distinction, flagged as unresolved after the sensors-becker pressure test, gets a second, independent data point from MB_0004 — from a completely different domain (pure graph theory, not engineering). That sensors-becker's `engineering_constraints` (facts about a detector) and MB_0004's `theorem_exceptions` (necessary in-domain exclusions) are *both* things the current two-field pairing can't cleanly express, in two unrelated domains, is modestly stronger evidence that this is a real recurring specification-design gap rather than an artifact of one domain's idiosyncrasy. Still not enough to write the resolution — sensors-becker's gap and MB_0004's gap aren't even the same shape (domain fact vs. in-domain necessary exclusion) — but it raises the priority of resolving SG-3 properly.

## D. Unresolved hypotheses (explicitly not decided by this memo)

- Does `theorem_exceptions` recur across a fifth specimen with a similar sharp-threshold-plus-boundary-case shape, or was it a one-paper binding?
- Should SG formalize "axis names are fixed per domain-binding, but the value vocabulary within an axis is open and may grow" as its own rule? (Candidate wording exists in category B; not proposed as SG text yet.)
- Is there a genuine unifying verification-completeness principle spanning sensors-becker's V1/V2/V3 and MB_0004's scope-coverage failure, or are they permanently distinct? Current evidence: distinct. One more independent example needed either way.
- Is provenance's two-dimensionality (role × treatment) real and general, or specific to how MB happens to record it?
- What actually resolves SG-3 — a three-way split (domain constraint / claim boundary / exception set, per MB_0004), a differently-shaped two-way split that accommodates both sensors-becker's and MB_0004's gaps, or something neither specimen has shown yet?

## Recommendation

Nothing in category A needs an SG_0001 edit — it's confirmation, not new information. Everything in category B and D should stay out of SG_0001 for now, exactly as flagged when MB_0004 was frozen. If any single change is worth making now, it's the smallest one: a note in SG-2 acknowledging that status-*value* vocabularies are open, separate from the already-stated claim about axis structure and location — this is a narrow, unambiguous, low-risk addition directly evidenced by MB_0004, unlike the other three candidates in category B, which all still rest on one specimen for a more consequential claim. Left to your judgment whether even that one is worth making now or held for a fifth specimen.
