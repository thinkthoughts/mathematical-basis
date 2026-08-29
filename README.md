# mathematical-basis

A repository of verified mathematical-basis statements (`MB_####`), each carrying its source provenance, its leading specification, an executable verification, and a stored result — end to end, one statement at a time.

## What belongs here

A statement earns an `MB_####` entry once it has:

1. **Source provenance** — where the claim originated, preserved as-given under `sources/`.
2. **A leading specification** — the general mathematical statement, not a specific numerical instance of it.
3. **An executable verification** — a script that computes the claim, not a script that asserts it.
4. **A stored result** — the actual output of running that script, not a paraphrase of an expected output.

A claim that has only some of these is not yet an `MB_####` entry. `persist.pdf`, for example, motivated this repository's first statement but is not itself one — it is a source, audited and found to support a different, more general claim than the one it originally reported. See MB_0001, below, for how that distinction plays out concretely.

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
│   └── readingpoint/
│       └── README.md                # verified excerpt of readingpoint.app's stated principle
├── statements/
│   └── MB_0001_RESIDUE_CONDITIONING.yaml
├── tests/
│   └── MB_0001_general_sweep.py
├── results/
│   └── MB_0001_general_sweep.yaml
└── papers/
    └── density-correction/
        └── paper.md                 # v3.1, current draft
```

## Status

- **MB_0001 — Residue Conditioning Specifies a Primorial Density Correction.** mathematical: proved · computational: supported · provenance: audited · publication: draft. Source: `sources/mb_0001/persist.pdf` (audited; its reported constant of 24/25 did not hold, and was superseded by the general result C(m) = m/φ(m)). Statement: `statements/MB_0001_RESIDUE_CONDITIONING.yaml`. Verification: `tests/MB_0001_general_sweep.py`. Result: `results/MB_0001_general_sweep.yaml`. Paper: `papers/density-correction/paper.md`.
- **MB_0002 — Unit-Group Structure Specifies Distinct Quotient Readings.** mathematical: proved · computational: supported · provenance: audited · publication: draft. Source: motivating prior discussion (RML/OpenWave group-structure context), independently re-derived rather than imported. Establishes (ℤ/30ℤ)ˣ ≅ C4×C2 and that its three order-2 subgroups give non-isomorphic quotients (C2×C2 from ⟨19⟩; C4 from ⟨11⟩ and ⟨29⟩). Statement: `statements/MB_0002_UNIT_GROUP_QUOTIENTS.yaml`. Verification: `tests/MB_0002_unit_group_quotients.py`. Result: `results/MB_0002_unit_group_quotients.yaml`. No separate paper yet — proof is inline in the statement.
- **MB_0003 and beyond** — not yet started. `sources/readingpoint/AUDIT.md` was checked as a candidate source and closed with no new statement found (its mod-30 claims are already covered by MB_0001 or are standard facts; see that file for the full audit). Candidates should go through the same source → statement → verification → result pipeline before being numbered, one at a time, rather than being pre-assigned.

## Principle

Admissible generalizations trail leading specifications.
