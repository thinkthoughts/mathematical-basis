# Proof: MB_0002 — Unit-Group Structure Specifies Distinct Quotient Readings

Statement under proof: `statements/MB_0002_UNIT_GROUP_QUOTIENTS.yaml`. Executable check: `tests/MB_0002_unit_group_quotients.py`.

## Claim

(ℤ/30ℤ)ˣ ≅ C4 × C2. It has exactly three subgroups of order 2 — ⟨11⟩, ⟨19⟩, ⟨29⟩ — and the quotient (ℤ/30ℤ)ˣ / H depends on which is chosen: H = ⟨19⟩ gives C2 × C2; H = ⟨11⟩ or H = ⟨29⟩ gives C4.

## Proof

**Step 1: (ℤ/30ℤ)ˣ has order 8.**

By multiplicativity of Euler's totient and 30 = 2·3·5, |(ℤ/30ℤ)ˣ| = φ(30) = φ(2)φ(3)φ(5) = 1·2·4 = 8. Explicitly, (ℤ/30ℤ)ˣ = {1,7,11,13,17,19,23,29}.

**Step 2: identifying the isomorphism type from the element-order profile.**

By the Chinese Remainder Theorem, ℤ/30ℤ ≅ ℤ/2ℤ × ℤ/3ℤ × ℤ/5ℤ, so (ℤ/30ℤ)ˣ ≅ (ℤ/2ℤ)ˣ × (ℤ/3ℤ)ˣ × (ℤ/5ℤ)ˣ ≅ {1} × C2 × C4 ≅ C4 × C2, using that the multiplicative group of a field 𝔽_p is cyclic of order p−1.

This can also be confirmed directly from the group, without invoking CRT, using a standard fact: a finite abelian group of order 8 is isomorphic to exactly one of C8, C4×C2, or C2×C2×C2, and these three are distinguished completely by their count of elements of order 2 (respectively 1, 3, and 7 — this follows from each group's structure: C8 has a unique element of order 2, its generator's 4th power; C4×C2 has three, one from each nontrivial combination of the order-≤2 elements in each factor; C2×C2×C2 has all 7 non-identity elements of order 2). Direct computation of every element's multiplicative order mod 30 gives:

  order 1: {1}
  order 2: {11, 19, 29}
  order 4: {7, 13, 17, 23}
  order 8: {}

Exactly 3 elements of order 2 identifies the group as C4 × C2, independent of the CRT argument above.

**Step 3: enumerating the order-2 subgroups.**

In an abelian group, every element generates a unique cyclic subgroup, and distinct elements of the same order can generate the same or different subgroups. Here, each of the three order-2 elements generates a 2-element subgroup {1, a}; since 11, 19, 29 are distinct and none equals another's product with 1 in a way that would merge their subgroups (each subgroup {1,a} for a ∈ {11,19,29} is trivially distinct since the non-identity elements differ), there are exactly three distinct order-2 subgroups: ⟨11⟩={1,11}, ⟨19⟩={1,19}, ⟨29⟩={1,29}.

**Step 4: computing each quotient.**

For H a subgroup of an abelian group G, G/H is again a group, of order |G|/|H| = 8/2 = 4. A group of order 4 is isomorphic to either C4 or C2×C2, distinguished by whether it has an element of order 4.

For each H, the four cosets are computed directly by multiplying each coset representative by H's elements mod 30, and the order of each coset (as an element of the quotient group) is computed by repeated multiplication until returning to the identity coset:

- H = ⟨11⟩ = {1,11}. Cosets: {1,11}, {7,17}, {13,23}, {19,29}. Representative 7 has quotient-order 4 (7² ≡ 19 mod the coset structure, continuing to order 4 before returning to {1,11}). Since an order-4 element exists, this quotient is **C4**.
- H = ⟨19⟩ = {1,19}. Cosets: {1,19}, {7,13}, {11,29}, {17,23}. Every non-identity representative (7, 11, 17) has quotient-order 2. No element of order 4 exists, so this quotient is **C2 × C2**.
- H = ⟨29⟩ = {1,29}. Cosets: {1,29}, {7,23}, {11,19}, {13,17}. Representative 7 has quotient-order 4. This quotient is **C4**.

(The full coset multiplication tables and per-element order computations are reproduced exactly, not merely asserted, in `tests/MB_0002_unit_group_quotients.py`; this proof states the argument, the test verifies the arithmetic underlying each step.)

**Step 5: conclusion.**

Two of the three order-2 subgroups (⟨11⟩, ⟨29⟩) give a C4 quotient; the third (⟨19⟩) gives C2×C2. Since all three subgroups have the same order (2) and sit inside the same ambient group ((ℤ/30ℤ)ˣ), the quotient's isomorphism type is not determined by the ambient group and the subgroup's order alone — it depends on which specific order-2 subgroup is chosen. ∎

## Scope

This proof establishes the claim for (ℤ/30ℤ)ˣ specifically. A general classification of order-2 subgroups and their quotient types across arbitrary groups isomorphic to C4×C2 is outside MB_0002's scope — not because it is mathematically open (it is standard, tractable group theory), but because this statement establishes the concrete case and does not generalize beyond it. See `statements/MB_0002_UNIT_GROUP_QUOTIENTS.yaml`'s `excluded_generalizations`.
