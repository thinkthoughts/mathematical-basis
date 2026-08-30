"""
tests/MB_0003_fano_orientations.py

Verification for MB_0003 (Fano-Line Orientations Specify a Unique
Alternative Octonion Class).

Checks, for all 128 orientations of the fixed seven Fano lines
(cyclic shifts of {1,2,4} mod 7):
  1. The base orientation (all lines as listed) reproduces Baez's
     canonical octonion multiplication table (arXiv:math/0105155,
     Table 1) exactly.
  2. Exactly 16 of the 128 orientations are alternative (Artin's full
     associator-alternation criterion: both [a,b,c]=-[b,a,c] and
     [a,b,c]=-[a,c,b], checked over all 512 basis triples per
     orientation for each identity).
  3. All 16 alternative orientations are also norm-multiplicative.
  4. All 16 alternative orientations are isomorphic to the reference
     (base) orientation via an explicit sign-flip map on e_1..e_7.
  5. The F2 point-line incidence matrix M has rank 4; the image of
     the sign-flip map eps -> M*eps (mod 2) has exactly 16 elements
     and is set-equal to the exhaustively-found alternative set.
"""
import numpy as np
from itertools import product

LINES = [(1,2,4),(2,3,5),(3,4,6),(4,5,7),(5,6,1),(6,7,2),(7,1,3)]

BAEZ_TABLE_RAW = {
    1: {2:'4', 3:'7', 4:'-2', 5:'6', 6:'-5', 7:'-3'},
    2: {1:'-4', 3:'5', 4:'1', 5:'-3', 6:'7', 7:'-6'},
    3: {1:'-7', 2:'-5', 4:'6', 5:'2', 6:'-4', 7:'1'},
    4: {1:'2', 2:'-1', 3:'-6', 5:'7', 6:'3', 7:'-5'},
    5: {1:'-6', 2:'3', 3:'-2', 4:'-7', 6:'1', 7:'4'},
    6: {1:'5', 2:'-7', 3:'4', 4:'-3', 5:'-1', 7:'2'},
    7: {1:'3', 2:'6', 3:'-1', 4:'5', 5:'-4', 6:'-2'},
}


def build_C(orientation_bits):
    C = np.zeros((8, 8, 8))
    for i in range(8):
        C[i, 0, i] = 1
        C[0, i, i] = 1
    for i in range(1, 8):
        C[i, i, 0] = -1
    for (a, b, c), bit in zip(LINES, orientation_bits):
        cyc = [a, b, c] if bit == 0 else [a, c, b]
        for idx in range(3):
            i, j = cyc[idx], cyc[(idx + 1) % 3]
            k = cyc[(idx + 2) % 3]
            C[i, j, k] = 1
            C[j, i, k] = -1
    return C


def mult(C, x, y):
    return np.einsum('i,j,ijk->k', x, y, C)


def basis(k):
    v = np.zeros(8)
    v[k] = 1
    return v


def check_alternative(C):
    """Full alternativity per Artin's theorem: checks BOTH
    [a,b,c] = -[b,a,c] (swap first two arguments) and
    [a,b,c] = -[a,c,b] (swap last two arguments). Baez's paper notes
    any two of the three transposition-antisymmetries imply the third,
    so checking both of these is sufficient for full alternativity,
    not merely the first-swap identity alone."""
    for i in range(8):
        for j in range(8):
            for k in range(8):
                a, b, c = basis(i), basis(j), basis(k)
                assoc_abc = mult(C, mult(C, a, b), c) - mult(C, a, mult(C, b, c))
                assoc_bac = mult(C, mult(C, b, a), c) - mult(C, b, mult(C, a, c))
                assoc_acb = mult(C, mult(C, a, c), b) - mult(C, a, mult(C, c, b))
                if not np.allclose(assoc_abc, -assoc_bac):
                    return False
                if not np.allclose(assoc_abc, -assoc_acb):
                    return False
    return True


def check_norm_multiplicative(C, n_trials=50, seed=0):
    rng = np.random.default_rng(seed)
    for _ in range(n_trials):
        x = rng.standard_normal(8)
        y = rng.standard_normal(8)
        xy = mult(C, x, y)
        if not np.isclose(np.sum(xy**2), np.sum(x**2) * np.sum(y**2), rtol=1e-6):
            return False
    return True


def find_sign_flip_isomorphism(C_ref, C_target):
    for signs in product([1, -1], repeat=7):
        D = np.diag([1] + list(signs))
        ok = True
        for i in range(8):
            for j in range(8):
                lhs = D @ mult(C_target, D[:, i], D[:, j])
                rhs = mult(C_ref, basis(i), basis(j))
                if not np.allclose(lhs, rhs):
                    ok = False
                    break
            if not ok:
                break
        if ok:
            return signs
    return None


def rank_mod2(A):
    A = A.copy() % 2
    rows, cols = A.shape
    r = 0
    for c in range(cols):
        pivot = None
        for i in range(r, rows):
            if A[i, c] == 1:
                pivot = i
                break
        if pivot is None:
            continue
        A[[r, pivot]] = A[[pivot, r]]
        for i in range(rows):
            if i != r and A[i, c] == 1:
                A[i] = (A[i] + A[r]) % 2
        r += 1
    return r


def run():
    # --- Check 1: base orientation reproduces Baez's table exactly ---
    base_bits = tuple([0] * 7)
    C_base = build_C(base_bits)
    mismatches = []
    for i in range(1, 8):
        for j in range(1, 8):
            if i == j:
                expected = (-1, 0)
            else:
                s = BAEZ_TABLE_RAW[i][j]
                sign = -1 if s.startswith('-') else 1
                k = int(s.lstrip('-'))
                expected = (sign, k)
            v = mult(C_base, basis(i), basis(j))
            nz = np.nonzero(v)[0]
            actual = (int(np.sign(v[nz[0]])), int(nz[0])) if len(nz) else (0, -1)
            if actual != expected:
                mismatches.append((i, j, expected, actual))
    baez_match = len(mismatches) == 0

    # --- Check 2-4: exhaustive classification of all 128 orientations ---
    alt_orientations = []
    for bits in product([0, 1], repeat=7):
        C = build_C(bits)
        if check_alternative(C):
            alt_orientations.append(bits)

    norm_mult_results = {bits: check_norm_multiplicative(build_C(bits)) for bits in alt_orientations}
    all_norm_mult = all(norm_mult_results.values())

    iso_results = {}
    for bits in alt_orientations:
        signs = find_sign_flip_isomorphism(C_base, build_C(bits))
        iso_results[bits] = signs is not None
    all_isomorphic = all(iso_results.values())

    # --- Check 5: F2 rank / image structure ---
    M = np.zeros((7, 7), dtype=int)
    for li, line in enumerate(LINES):
        for p in line:
            M[li, p - 1] = 1
    rank = rank_mod2(M)

    image_patterns = set()
    for eps in product([0, 1], repeat=7):
        s = tuple((M @ np.array(eps)) % 2)
        image_patterns.add(s)

    alt_set = set(alt_orientations)
    image_equals_alt_set = image_patterns == alt_set

    summary = {
        "baez_table_reproduced_exactly": baez_match,
        "mismatches_vs_baez": len(mismatches),
        "total_orientations": 128,
        "alternative_count": len(alt_orientations),
        "alternative_count_expected": 16,
        "all_alternative_are_norm_multiplicative": all_norm_mult,
        "all_alternative_are_isomorphic_to_reference": all_isomorphic,
        "F2_incidence_matrix_rank": rank,
        "F2_incidence_matrix_rank_expected": 4,
        "image_size": len(image_patterns),
        "image_size_expected": 16,
        "image_equals_alternative_set": image_equals_alt_set,
        "claim_status": "supported" if (
            baez_match
            and len(alt_orientations) == 16
            and all_norm_mult
            and all_isomorphic
            and rank == 4
            and len(image_patterns) == 16
            and image_equals_alt_set
        ) else "rejected",
    }

    return {
        "alternative_orientations": [list(b) for b in alt_orientations],
        "summary": summary,
    }


if __name__ == "__main__":
    import json
    print(json.dumps(run(), indent=2))
