# mathematical-basis

A repository of verified mathematical-basis statements (`MB_####`), each carrying its source provenance, its leading specification, a proof, an executable verification, and a stored result — end to end, one statement at a time.

## What belongs here

A statement earns an `MB_####` entry once it has:

1. **Source provenance** — where the claim originated, preserved as-given under `sources/`.
2. **A leading specification** — the general mathematical statement, not a specific numerical instance of it.
3. **A proof** — the mathematical argument establishing the statement, as a standalone artifact (a full paper under `papers/`, or a shorter dedicated file under `proofs/`). A computational check that a claim holds is not a substitute for this; where the claim is a theorem, it needs a mathematical justification, not only numerical support.
4. **An executable verification** — a script that computes the claim, not a script that asserts it.
5. **A stored result** — the actual output of running that script, not a paraphrase of an expected output.

A claim that has only some of these is not yet an `MB_####` entry. `persist.pdf`, for example, motivated this repository's first statement but is not itself one — it is a source, audited and found to support a different, more general claim than the one it originally reported. See MB_0001, below, for how that distinction plays out concretely.

Not every statement needs a full paper — MB_0001 has one because the result and its context warranted it; MB_0002 has a shorter dedicated proof file instead, which satisfies requirement 3 equally. Publication (a paper, or eventually an outward-facing writeup) is optional on top of this five-part minimum, not part of it.

## Repo layout

```
mathematical-basis/
├── README.md
├── RO_A_READING_ORDER.md
├── RO_B_MATHEMATICAL_BASIS.md
├── .gitattributes                   # *.pdf binary
├── sources/
│   ├── mb_0001/
│   │   ├── README.md
│   │   └── persist.pdf              # v1.1, historical basis, claims preserved verbatim
│   ├── mb_0003/
│   │   └── baez-octonions.md        # excerpt of Baez's Table 1 and Fano-plane construction
│   └── readingpoint/
│       └── README.md                # verified excerpt of readingpoint.app's stated principle
├── statements/
│   ├── MB_0001_RESIDUE_CONDITIONING.yaml
│   ├── MB_0002_UNIT_GROUP_QUOTIENTS.yaml
│   └── MB_0003_FANO_ORIENTATIONS.yaml
├── proofs/
│   ├── MB_0002_UNIT_GROUP_QUOTIENTS.md
│   └── MB_0003_FANO_ORIENTATIONS.md
├── tests/
│   ├── MB_0001_general_sweep.py
│   ├── MB_0002_unit_group_quotients.py
│   └── MB_0003_fano_orientations.py
├── results/
│   ├── MB_0001_general_sweep.yaml
│   ├── MB_0002_unit_group_quotients.yaml
│   └── MB_0003_fano_orientations.yaml
└── papers/
    └── density-correction/
        └── paper.md                 # v3.1, current draft (MB_0001 only; MB_0002/MB_0003's proofs are in proofs/, not full papers)
```

## Status

- **MB_0001 — Residue Conditioning Specifies a Primorial Density Correction.** mathematical: proved · computational: supported · provenance: audited · publication: draft. Source: `sources/mb_0001/persist.pdf` (audited; its reported constant of 24/25 did not hold, and was superseded by the general result C(m) = m/φ(m)). Statement: `statements/MB_0001_RESIDUE_CONDITIONING.yaml`. Verification: `tests/MB_0001_general_sweep.py`. Result: `results/MB_0001_general_sweep.yaml`. Paper: `papers/density-correction/paper.md`.
- **MB_0002 — Unit-Group Structure Specifies Distinct Quotient Readings.** mathematical: proved · computational: supported · provenance: audited · publication: draft. Source: motivating prior discussion (RML/OpenWave group-structure context), independently re-derived rather than imported. Establishes (ℤ/30ℤ)ˣ ≅ C4×C2 and that its three order-2 subgroups give non-isomorphic quotients (C2×C2 from ⟨19⟩; C4 from ⟨11⟩ and ⟨29⟩). Statement: `statements/MB_0002_UNIT_GROUP_QUOTIENTS.yaml`. Proof: `proofs/MB_0002_UNIT_GROUP_QUOTIENTS.md`. Verification: `tests/MB_0002_unit_group_quotients.py`. Result: `results/MB_0002_unit_group_quotients.yaml`.
- **MB_0003 — Fano-Line Orientations Specify a Unique Alternative Octonion Class.** mathematical: proved · computational: supported · provenance: audited · publication: draft. Source: `sources/mb_0003/baez-octonions.md` (excerpt of John C. Baez, "The Octonions," arXiv:math/0105155). Fixes the seven Fano lines given by cyclic shifts of {1,2,4} mod 7; of the 2⁷=128 independent line-orientation choices, exactly 16 yield an alternative algebra, all 16 isomorphic to the standard octonions via explicit sign-flip maps, the remaining 112 failing alternativity. Proof identifies the count structurally via the Fano incidence matrix's rank 4 over 𝔽₂ (2⁴=16), not just by enumeration. This is the project's first specimen outside the mod-30/primorial family — nonassociative algebra, with a verification style (exhaustive combinatorial reconstruction + algebraic identity checking) distinct from MB_0001's numerical sweeps and MB_0002's exact enumeration. Statement: `statements/MB_0003_FANO_ORIENTATIONS.yaml`. Proof: `proofs/MB_0003_FANO_ORIENTATIONS.md`. Verification: `tests/MB_0003_fano_orientations.py`. Result: `results/MB_0003_fano_orientations.yaml`.
- **MB_0004 and beyond** — not yet started. `sources/readingpoint/AUDIT.md` was checked as a candidate source and closed with no new statement found (its mod-30 claims are already covered by MB_0001 or are standard facts; see that file for the full audit). Candidates should go through the same source → statement → proof → verification → result pipeline before being numbered, one at a time, rather than being pre-assigned.

## Principle

Admissible generalizations trail leading specifications.
