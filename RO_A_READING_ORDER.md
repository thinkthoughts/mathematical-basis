# RO_A — Reading Order

Purpose: understand this repository, in the order a new reader should move through it.

1. **README.md** — what belongs here, and the five things a statement needs before it earns an MB_#### number.
2. **RO_B_MATHEMATICAL_BASIS.md** — the source → statement → proof → verification → result pipeline, walked through concretely using MB_0001.
3. **sources/mb_0001/persist.pdf** — the historical source that motivated MB_0001, preserved as originally written.
4. **statements/MB_0001_RESIDUE_CONDITIONING.yaml** — the leading specification: what MB_0001 actually claims, and what it explicitly does not.
5. **tests/MB_0001_general_sweep.py** — the executable verification. Runnable as-is.
6. **results/MB_0001_general_sweep.yaml** — the stored output of running that script, not a paraphrase of it.
7. **papers/density-correction/paper.md** — the full mathematical writeup: theorem, proof, the 9423 correspondence audit, and the label/reading/specification distinction that audit motivated.

A reader who only has time for two files should read README.md and papers/density-correction/paper.md. A reader auditing the repository's own rigor should read statements/, tests/, and results/ together and check that all three agree with each other before trusting any of the prose.
