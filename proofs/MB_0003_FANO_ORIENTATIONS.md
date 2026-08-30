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

**Part 4: the image is exactly the full alternative set.**

Direct exhaustive verification (`tests/MB_0003_fano_orientations.py`) checks all 128 orientations against Artin's associator-alternation criterion, over all 512 basis triples per orientation (a check that is mathematically sufficient by trilinearity of the associator, not merely a sample). This finds exactly 16 alternative orientations.

Since image(M) ⊆ alternative orientations (Part 3) and |image(M)| = 16 = |alternative orientations| (Part 2, and the exhaustive count), and both are finite sets, image(M) = alternative orientations exactly.

**Conclusion.** An orientation s is alternative if and only if s ∈ image(M) — equivalently, if and only if s is reachable from the base Baez orientation by some basis sign-flip. Since every element of this image is explicitly isomorphic to the standard octonions (Part 3), all 16 alternative orientations give the same algebra up to isomorphism: there is exactly one isomorphism class among the 128, realized by exactly 16 of the 128 orientation choices. ∎

## What this proof establishes that the exhaustive check alone does not

The exhaustive check (128 cases, each requiring checking 512 basis triples for the associator identity) establishes the count and the specific isomorphisms by brute force. This proof additionally explains *why* the count is 16: it is 2^rank(M) for the Fano incidence matrix's 𝔽₂-rank, a quantity with independent meaning in coding theory (the Fano plane's line vectors are related to the [7,4] Hamming code / [7,3] simplex code). The exhaustive computation and the rank-4 structural fact are independent derivations of the same number, and their agreement (Part 4) is itself part of the proof, not a coincidence to be explained away.

## Scope

This proof is scoped to the single fixed line-labeling given in Setup. It does not separately establish that a different labeling of the seven Fano lines would give the same rank-4 / 16-orientation result, though this is expected to follow from the classical uniqueness of the Fano plane up to point relabeling — that fact is cited, not re-derived here. See `statements/MB_0003_FANO_ORIENTATIONS.yaml`'s `excluded_generalizations`.
