# sources/mb_0003/baez-octonions.md

Excerpt of John C. Baez, "The Octonions", Bulletin of the American Mathematical Society 39 (2002), 145-205. arXiv:math/0105155v4 [math.RA], fetched 2026-08-30.

Preserved as the ground-truth reference this statement was checked against — not imported on authority, but used as the target the reconstruction in `tests/MB_0003_fano_orientations.py` was verified to reproduce exactly.

## Table 1 — Octonion Multiplication Table (Section 2, as given in the source)

Row i, column j gives e_i · e_j:

```
      e1    e2    e3    e4    e5    e6    e7
e1    -1    e4    e7   -e2    e6   -e5   -e3
e2   -e4    -1    e5    e1   -e3    e7   -e6
e3   -e7   -e5    -1    e6    e2   -e4    e1
e4    e2   -e1   -e6    -1    e7    e3   -e5
e5   -e6    e3   -e2   -e7    -1    e1    e4
e6    e5   -e7    e4   -e3   -e1    -1    e2
e7    e3    e6   -e1    e5   -e4   -e2    -1
```

## Section 2.1 — The Fano plane (as given in the source)

"This is the Fano plane, a little gadget with 7 points and 7 lines. The 'lines' are the sides of the triangle, its altitudes, and the circle containing all the midpoints of the sides. Each pair of distinct points lies on a unique line. Each line contains three points, and each of these triples has a cyclic ordering shown by the arrows. If e_i, e_j, and e_k are cyclically ordered in this way then

  e_i e_j = e_k,  e_j e_i = -e_k.

Together with these rules:
- 1 is the multiplicative identity,
- e_1, ..., e_7 are square roots of -1,

the Fano plane completely describes the algebra structure of the octonions."

## Role in this repository

The source gives one specific oriented Fano-plane picture (a specific choice among the 128 possible orientations of the underlying seven lines) and states, correctly, that it describes the octonions. `statements/MB_0003_FANO_ORIENTATIONS.yaml` extends past this single case to classify all 128 orientations of the same seven lines, finding that exactly 16 are alternative and all 16 are isomorphic to the algebra this table defines. The specific line set used (cyclic shifts of {1,2,4} mod 7) reproduces this table exactly under the base (all-forward) orientation choice — verified directly, 0 mismatches across all 49 table entries, in `tests/MB_0003_fano_orientations.py`.
