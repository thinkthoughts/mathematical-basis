# sources/mb_0004/chu-2026-removable-matchings.md

Excerpt of Hojin Chu, "A sharp extension of Halin's removable-edge theorem to matchings," arXiv:2608.09394v1 [math.CO], posted August 10, 2026. School of Computational Sciences, Korea Institute for Advanced Study (KIAS).

Preserved as the ground-truth reference this statement was checked against and independently re-verified computationally against, not imported on authority.

## Definitions (Section 1, as given in the source)

All graphs considered are finite, undirected, and simple. For a graph G, V(G), E(G), δ(G), κ(G) denote vertex set, edge set, minimum degree, connectivity.

"A subgraph H of a k-connected graph G is called k-removable if G − E(H) remains k-connected." An edge e is k-removable if H = {e} is k-removable. H = M for a matching M is a k-removable matching.

## Theorem 1.1 (Halin, cited as prior work)

"Let k be a positive integer. Every k-connected graph G with δ(G) ≥ k + 1 contains a k-removable edge."

## Theorem 1.3 (the paper's main result)

"Let k and m be positive integers. Every k-connected graph G with

  δ(G) ≥ max{k + 1, 2m − 2}

contains a k-removable matching of size m, unless G ≅ K_{2m−1}, or (k, m) = (1, 2) and G is a cycle."

Immediately following (Section 1, as given): "Both exceptions in Theorem 1.3 are unavoidable, since K_{2m−1} has no matching of size m and a cycle has no 1-removable matching of size two. Consequently, the condition δ(G) ≥ max{k + 1, 2m − 1} is the sharp minimum degree condition guaranteeing a k-removable matching of size m without exceptions."

## Corollary 1.4 (resolves a named conjecture)

Taking m = ⌈(δ(G)+1)/2⌉ in Theorem 1.3 resolves a conjecture of Li, Zhou, Fujita, and Mao (2026): "Every k-connected graph G with δ(G) ≥ k + 1 contains a k-removable matching of size ⌈(δ(G) + 1)/2⌉, unless either k = 1 and G is a cycle, or δ(G) is even and G ≅ K_{δ(G)+1}."

## Corollary 5.1 and the f(k,δ) parameter

The paper's concluding section resolves a question posed by Li, Zhou, Fujita, and Mao about the largest t such that every k-connected graph G with |V(G)| ≥ 2δ and δ(G) ≥ δ has a k-removable matching of size t: "f(k, δ) ≥ ⌈(δ+1)/2⌉" for (k,δ) ≠ (1,2), and combined with a prior upper bound, "⌈(k+2)/2⌉ ≤ f(k,k+1) ≤ k," giving the exact value f(3,4) = 3.

## Proof structure (Sections 2-4, summarized, not reproduced verbatim)

The proof proceeds via: (1) Theorem 2.2, a "prescribed-set" strengthening of Halin's theorem, guaranteeing a k-removable edge with both endpoints outside a given vertex set W under a degree condition relative to |W|, with an explicit exceptional forest structure when the bound is not strengthened; (2) two "dense matching" lemmas (Lemma 3.3, Lemma 3.5) handling near-complete graphs via explicit cycle/matching constructions and the Tutte-Berge formula; (3) the main proof of Theorem 1.3 in Section 4, by contradiction: assuming a minimal counterexample, choosing a maximum k-removable matching M minimizing the number of components of G[U] (U = vertices not covered by M), and deriving a sequence of structural claims (4.1-4.6) forcing G[U] to be a single short path, which is then shown to contradict Lemma 3.3 or Lemma 3.5.

## Declared AI use (source's own disclosure, preserved for completeness)

The source paper's own declaration states the author used an AI tool "to generate an initial proof of Lemma 3.5 and to provide grammatical and editorial suggestions," and states the author "independently verified the mathematical arguments, reviewed and revised all AI-assisted text, and takes full responsibility for the correctness of the proof." Recorded here as part of the source's own provenance, not evaluated further by this repository.

## Role in this repository

`statements/MB_0004_REMOVABLE_MATCHING_THRESHOLD.yaml` restates Theorem 1.3 as a leading specification, with the two named exceptions recorded in a `theorem_exceptions` field (an SG-7 domain-specific extension, not folded into `excluded_generalizations`, which in MB_0001-3 records untested extensions beyond a proven domain — a different role than these in-domain, hypothesis-satisfying necessary exclusions). `proofs/MB_0004_REMOVABLE_MATCHING_THRESHOLD.md` audits the source's proof structure rather than re-deriving it independently from scratch, given its length and reliance on the source's own prior-paper citations (Halin, Mader, Tutte-Berge). `tests/MB_0004_removable_matching_verification.py` independently re-implements and checks the theorem and both exceptions computationally for small graphs, exhaustively.
