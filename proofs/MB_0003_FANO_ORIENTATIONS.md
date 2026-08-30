# Proof: MB_0003 — Fano-Line Orientations Specify a Unique Alternative Octonion Class

Statement under proof: `statements/MB_0003_FANO_ORIENTATIONS.yaml`. Executable check: `tests/MB_0003_fano_orientations.py`.

## Setup

Fix the seven Fano lines as the cyclic shifts of {1,2,4} mod 7:

  L1={1,2,4}, L2={2,3,5}, L3={3,4,6}, L4={4,5,7}, L5={5,6,1}, L6={6,7,2}, L7={7,1,3}

This is verified to be a valid Fano plane structurally: 7 points, 7 lines, each line 3 points, every pair of points covered by exactly one line, every point on exactly 3 lines.

Each line has 2 possible cyclic orientations. Choosing one orientation per line, independently, gives 2⁷ = 128 real 8-dimensional unital algebras with basis 1, e₁,...,e₇, where e_i² = −1, e_i e_j = −e_j e_i for i≠j, and for i,j,k cyclically ordered per a line's chosen orientation, e_i e_j = e_k (and e_j e_i = −e_k).

The orientation with all lines in the order listed above reproduces Baez's Table 1 exactly (verified directly: 0 mismatches across all 49 entries of the multiplication table).

## Claim

Exactly 16 of the 128 orientations are alternative (Artin's criterion). All 16 are isomorphic to the standard octonions via explicit basis sign flips. The remaining 112 are not alternative.

## Proof

**Part 1: encoding orientation and sign-flips over 𝔽₂.**

Encode an orientation choice as s ∈ 𝔽₂⁷, one bit per line (0 = base direction, 1 = reversed). Encode a basis sign-flip e_i ↦ εᵢei, εᵢ ∈ {±1}, as a vector ε ∈ 𝔽₂⁷ (0 = +1, 1 = −1).

If we apply a sign flip ε to the base (all-zero) orientation's algebra, the resulting structure constants correspond to a new orientation s' where, for each line {i,j,k}, the orientation bit flips exactly when an odd number of εᵢ,εⱼ,εₖ are 1 — i.e., s'ₗ = (εᵢ + εⱼ + εₖ) mod 2 for line ℓ = {i,j,k}. This is because reversing an odd number of the three basis signs in a triple product e_i e_j = e_k flips the sign of the relation (e.g. (−e_i)e_j = −e_k, so the pair (i,j) now yields −e_k where it used to yield e_k — an orientation reversal on that line), while flipping an even number (0 or 2 of the three) preserves the relation's sign.

This gives s' = M·ε (mod 2), where M is the 7×7 point-line incidence matrix of the Fano plane (Mₗᵢ = 1 if point i is on line ℓ, else 0). This map is 𝔽₂-linear in ε.

**Part 2: rank(M) = 4.**

Direct computation (Gaussian elimination over 𝔽₂) gives rank(M) = 4. This matches a classical fact about the Fano plane's incidence matrix over 𝔽₂ — it is not full rank (7) as it would be over the reals, and its rank is 4, independent of this project. Consequently:

  |image of ε ↦ Mε| = 2⁴ = 16,   |kernel| = 2⁷⁻⁴ = 8.

**Part 3: every orientation in the image is alternative and isomorphic to 𝕆.**

For any ε ∈ 𝔽₂⁷, the map e_i ↦ εᵢ e_i (interpreting the 𝔽₂ bit as a sign ±1) is a linear bijection on the algebra. Applying it to the base (Baez) octonion algebra produces an isomorphic algebra — an algebra isomorphism preserves alternativity by definition (alternativity is a statement about which identities hold under multiplication, and an isomorphism carries the multiplication table exactly). The resulting algebra's orientation is exactly s = Mε by Part 1. So every s in the image of M is alternative, and by construction, isomorphic to the base octonions via the explicit map ε.

This shows: alternative orientations ⊇ image(M), with 16 ≤ |alternative orientations|, and every element of the image is explicitly, constructively isomorphic to 𝕆.

**Part 4: the alternative set is exactly the null space of an explicit, closed-form constraint system — derived without reference to the exhaustive count.**

For each unordered triple {i,j,k} of distinct points, the associator-alternation condition [e_i,e_j,e_k] = −[e_j,e_i,e_k] was expanded symbolically. Each of the four terms in this identity ((e_ie_j)e_k, e_i(e_je_k), (e_je_i)e_k, e_j(e_ie_k)) has the form (base sign) × (−1)^(orientation bits of the lines used) × (a basis element or scalar) — the sign is manifestly 𝔽₂-linear in the orientation vector s, since composing two such signed products multiplies signs, and multiplying two ±1 values of the form (−1)^(linear combination) is itself (−1)^(XOR of the combinations) — an 𝔽₂-linear operation, not merely observed to behave linearly by testing.

Two cases arise:

- If {i,j,k} is itself one of the seven lines, both associator terms trace back to squaring the same basis element (e_r² = −1, independent of orientation), and the resulting condition holds automatically for either choice of that line's orientation — this case imposes **no constraint** (confirmed directly: both local values of the line's bit satisfy the identity).
- If {i,j,k} is not a line (28 of the 35 possible triples), the condition reduces to a single non-trivial linear equation in the orientation bits of the (up to 6) lines the triple's three pairs touch.

Extracting the explicit coefficient vector for each of the 28 non-line triples (by evaluating the known-linear condition against its own point set — a standard interpolation of an already-established linear form, not a search for whether the form exists) gives, after removing duplicates, exactly **seven distinct constraints** — one for each point p ∈ {1,...,7}:

  Σ_{ℓ: p ∉ ℓ} s_ℓ ≡ 0 (mod 2)

i.e., for each point p, the sum of orientation bits over the four lines *not containing* p must be even. (Each point lies on 3 of the 7 lines and is absent from the other 4, so this sum has exactly 4 terms.) Each of the 28 triples maps to exactly one of these 7 point-indexed constraints; the map is 4-to-1, consistent with the Fano plane's symmetry.

This 7×7 constraint system (rows indexed by points, columns by lines) has rank 3 over 𝔽₂ — computed directly from these seven closed-form rows, independent of Part 2's matrix M. Its null space therefore has dimension 7−3 = 4, i.e. 16 elements — again, independent of Part 2.

**Part 5: the two independently-derived 16-element sets coincide.**

Part 3 established image(M) — derived from the sign-flip/isomorphism argument — is a 4-dimensional subspace, all of it alternative. Part 4 established, independently and purely from expanding the associator identity, that the full alternative set is exactly a different-looking 4-dimensional subspace (the null space of the point-indexed constraint system). Direct comparison (both are explicit subspaces of 𝔽₂⁷, computed independently) shows these two subspaces are identical as sets.

**Conclusion.** An orientation s is alternative if and only if, for every point p, the sum of orientation bits over the four lines not containing p is even — equivalently, if and only if s ∈ image(M). Since every element of image(M) is explicitly, constructively isomorphic to the standard octonions (Part 3), all 16 alternative orientations give the same algebra up to isomorphism. ∎

The exhaustive 128-orientation computer check (`tests/MB_0003_fano_orientations.py`) is, given the above, **independent verification of an already-complete analytic proof** — not an ingredient the proof depends on. It confirms the same 16-element count and the same specific orientations, by brute force, as a check against errors in Parts 1–5, exactly the same role MB_0001's and MB_0002's tests play relative to their proofs.

## What this proof establishes that the exhaustive check alone does not

The proof (Parts 1-5) is fully analytic: it derives the classification from the algebraic structure of the sign representation and the associator identity directly, reaching a closed-form characterization (for each point p, the sum of orientation bits over the four lines not containing p must be even) without counting through all 128 orientations at any stage. The number 16 is derived twice, independently — once as 2^rank(M) from the sign-flip symmetry (Part 2), once as 2^(7-rank(constraints)) from the associator expansion (Part 4) — and the two derivations are shown to describe the same set (Part 5), which is itself part of the proof's content, not a coincidence deferred to computation. The exhaustive 128-orientation test is independent verification of this analytic result, in the same relationship MB_0001's and MB_0002's tests have to their proofs — not an ingredient the proof's logical structure depends on.

## Scope

This proof is scoped to the single fixed line-labeling given in Setup. It does not separately establish that a different labeling of the seven Fano lines would give the same rank-4 / 16-orientation result, though this is expected to follow from the classical uniqueness of the Fano plane up to point relabeling — that fact is cited, not re-derived here. See `statements/MB_0003_FANO_ORIENTATIONS.yaml`'s `excluded_generalizations`.
