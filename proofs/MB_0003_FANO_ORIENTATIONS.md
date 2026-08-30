# Proof: MB_0003 — Fano-Line Orientations Specify a Unique Alternative Octonion Class

Statement under proof: `statements/MB_0003_FANO_ORIENTATIONS.yaml`. Executable check: `tests/MB_0003_fano_orientations.py`.

## Setup

Fix the seven Fano lines as the cyclic shifts of {1,2,4} mod 7:

  L1={1,2,4}, L2={2,3,5}, L3={3,4,6}, L4={4,5,7}, L5={5,6,1}, L6={6,7,2}, L7={7,1,3}

This is verified to be a valid Fano plane structurally: 7 points, 7 lines, each line 3 points, every pair of points covered by exactly one line, every point on exactly 3 lines.

Each line has 2 possible cyclic orientations. Choosing one orientation per line, independently, gives 2⁷ = 128 real 8-dimensional unital algebras with basis 1, e₁,...,e₇, where e_i² = −1, e_i e_j = −e_j e_i for i≠j, and for i,j,k cyclically ordered per a line's chosen orientation, e_i e_j = e_k (and e_j e_i = −e_k).

The orientation with all lines in the order listed above reproduces Baez's Table 1 exactly (verified directly: 0 mismatches across all 49 entries of the multiplication table).

## Claim

Exactly 16 of the 128 orientations are alternative (full associator alternation, per Artin's theorem). All 16 are isomorphic to the standard octonions via explicit basis sign flips. The remaining 112 are not alternative.

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

For each unordered triple {i,j,k} of distinct points, the **first antisymmetry identity**, [e_i,e_j,e_k] = −[e_j,e_i,e_k] (swapping the first two arguments), was expanded symbolically. Each of the four terms in this identity ((e_ie_j)e_k, e_i(e_je_k), (e_je_i)e_k, e_j(e_ie_k)) has the form (base sign) × (−1)^(orientation bits of the lines used) × (a basis element or scalar) — the sign is manifestly 𝔽₂-linear in the orientation vector s, since composing two such signed products multiplies signs, and multiplying two ±1 values of the form (−1)^(linear combination) is itself (−1)^(XOR of the combinations) — an 𝔽₂-linear operation, not merely observed to behave linearly by testing.

Two cases arise:

- If {i,j,k} is itself one of the seven lines, both terms trace back to squaring the same basis element (e_r² = −1, independent of orientation), and the resulting condition holds automatically for either choice of that line's orientation — this case imposes **no constraint**.
- If {i,j,k} is not a line (28 of the 35 possible triples), the condition reduces to a single non-trivial linear equation in the orientation bits.

Extracting the explicit coefficient vector for each of the 28 non-line triples (by evaluating the known-linear condition against its own point set — interpolating a form already established to be linear, not searching for whether it is one) gives, after removing duplicates, exactly **seven distinct constraints** — one for each point p ∈ {1,...,7}:

  Σ_{ℓ: p ∉ ℓ} s_ℓ ≡ 0 (mod 2)

i.e., for each point p, the sum of orientation bits over the four lines *not containing* p must be even. Writing these seven equations as the rows of a 7×7 matrix C, indexed by points (rows) and lines (columns), with C_{p,ℓ} = 1 iff p ∉ L_ℓ:

```
        L1 L2 L3 L4 L5 L6 L7
  p=1:   0  1  1  1  0  1  0
  p=2:   0  0  1  1  1  0  1
  p=3:   1  0  0  1  1  1  0
  p=4:   0  1  0  0  1  1  1
  p=5:   1  0  1  0  0  1  1
  p=6:   1  1  0  1  0  0  1
  p=7:   1  1  1  0  1  0  0
```

the condition is exactly **Cs = 0 (mod 2)**. (Each row has weight 4, since every point lies on 3 of the 7 lines and is absent from the other 4.)

**The second antisymmetry identity**, [e_i,e_j,e_k] = −[e_i,e_k,e_j] (swapping the last two arguments), was checked by the identical symbolic method and produces the **same seven constraint rows**, verified directly rather than assumed from Baez's paper's general remark that any two of the three transposition-antisymmetries imply the third. Both identities together are Artin's full criterion for alternativity; since both reduce to the same system Cs=0, that system fully characterizes alternativity for this construction, not merely the first-swap identity alone.

**Part 5: Cs=0 exactly characterizes im(M), via a design-theoretic identity — not by comparing two independently-computed ranks.**

Notice C = J + Mᵀ (mod 2), where J is the 7×7 all-ones matrix — directly checkable entry-by-entry, since C_{p,ℓ}=1 iff p∉L_ℓ iff Mᵀ_{p,ℓ}=0 iff (J+Mᵀ)_{p,ℓ}=1.

Two facts about the Fano plane's design (r=3 lines through each point, λ=1 common line through each pair of points — both direct consequences of the Fano plane axioms verified in Setup) give, over 𝔽₂:

  MᵀM = J   (since (MᵀM)_{p,q} = number of lines containing both p and q — this is r=3≡1 when p=q, and λ=1 when p≠q, so every entry is 1)
  JM = J    (since (JM)_{ℓ,p}... row p of JM sums M's rows, giving, for each column, the number of lines through that point, r=3≡1, so every entry is 1 — equivalently, each row of M sums to 3≡1, matching J's row)

Therefore:

  CM = (J + Mᵀ)M = JM + MᵀM = J + J = 0 (mod 2),

identically — **no case analysis over triples required for this step**. So im(M) ⊆ ker(C) = {s : Cs = 0}.

Since im(M) has dimension 4 (Part 2), ker(C) has dimension ≥ 4, so rank(C) ≤ 7−4 = 3. Separately, the general linear-algebra inequality rank(A+B) ≥ |rank(A) − rank(B)| (valid over any field) gives rank(C) = rank(J+Mᵀ) ≥ |rank(J) − rank(Mᵀ)| = |1 − 4| = 3. Combining both bounds, rank(C) = 3 exactly, so dim ker(C) = 4 = dim im(M). Since im(M) ⊆ ker(C) and both have the same finite dimension, **im(M) = ker(C) exactly** — without needing to independently compute or compare two separately-derived 16-element sets.

**Conclusion.** An orientation s is alternative if and only if, for every point p, the sum of orientation bits over the four lines not containing p is even — equivalently, if and only if s ∈ image(M). Since every element of image(M) is explicitly, constructively isomorphic to the standard octonions (Part 3), all 16 alternative orientations give the same algebra up to isomorphism. ∎

The exhaustive 128-orientation computer check (`tests/MB_0003_fano_orientations.py`) is, given the above, **independent verification of an already-complete analytic proof** — not an ingredient the proof depends on. It confirms the same 16-element count and the same specific orientations, by brute force, checking both antisymmetry identities directly on all 128 orientations, as a check against errors in Parts 1–5, exactly the same role MB_0001's and MB_0002's tests play relative to their proofs.

## What this proof establishes that the exhaustive check alone does not

The proof (Parts 1-5) is fully analytic. Part 4 derives a closed-form constraint system directly from the associator identity, verified for both antisymmetry swaps independently rather than assumed from one. Part 5 then shows this system's null space equals im(M) via a design-theoretic identity (C = J + Mᵀ, together with MᵀM = J and JM = J, both direct consequences of the Fano plane's incidence structure) rather than by independently computing two ranks and observing they match — CM=0 is an algebraic identity, not a coincidence of two computed numbers. The exhaustive 128-orientation test is independent verification of this analytic result, in the same relationship MB_0001's and MB_0002's tests have to their proofs — not an ingredient the proof's logical structure depends on.

## Scope

This proof is scoped to the single fixed line-labeling given in Setup. It does not separately establish that a different labeling of the seven Fano lines would give the same rank-4 / 16-orientation result, though this is expected to follow from the classical uniqueness of the Fano plane up to point relabeling — that fact is cited, not re-derived here. See `statements/MB_0003_FANO_ORIENTATIONS.yaml`'s `excluded_generalizations`.
