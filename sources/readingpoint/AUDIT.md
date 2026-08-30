# sources/readingpoint/AUDIT.md

Audit of readingpoint.app's live content (fetched and verified 2026-08-29, same fetch as `README.md` in this directory), classified per the five-category scheme proposed for discovering MB_0002 candidates rather than manufacturing one.

## 1. Already-established mathematical facts

- Every prime p > 5 is coprime to 30, so its residue mod 30 lies in {1,7,11,13,17,19,23,29} — standard elementary number theory (this is exactly MB_0001's m=30 specialization: 8 = φ(30)).
- "30 positions → 8 candidate reading points. Divisibility by 2, 3, 5 removes the other 22 residue positions." — arithmetically trivial (30 − 8 = 22) and correct.
- "Occupying one of the eight remaining classes is necessary for a prime greater than 5, but it does not by itself establish primality." — correctly hedged; the site itself already states this as necessary-not-sufficient rather than overclaiming.
- 𝔰𝔬(10) has rank 5, with five mutually commuting Cartan generators, labeling the weights of the 16-dimensional chiral spinor representation — standard Lie theory (rank of 𝔰𝔬(2n) is n), correctly stated.
- (1+1)×3×5 = 30 — trivial arithmetic.
- A pentagon has 5 sides; a hand has 5 digits; a music staff has 5 lines; 5-dimensional space has dimension 5 — trivially true, definitional.

## 2. Project definitions/specification vocabulary

- "Reading point" itself, as the site's core term — not standard mathematical vocabulary; already formalized in this repo's `reading-point.yaml` (in residue-manifold-learning) as object → specification → interaction → observable → reading.
- "+5 constraint" as a label for the arithmetic setup — a naming choice, not a theorem.
- The stated general principle — "Different objects can produce the same numerical reading point without being identified with one another," "Their specifications remain distinct" — this is methodology/epistemic vocabulary, not a mathematical claim requiring proof. It's already the operative principle behind `correspondence.yaml`'s firewall and this repo's own label/reading/specification hierarchy (paper.md §3).

## 3. Candidate mathematical statements requiring formalization

**None found on the current page.** This is worth stating plainly rather than manufacturing a candidate to fill the category: every quantitative claim on the page is either already standard (category 1) or already covered by MB_0001's general theorem (the 8-residue count is literally C(30)'s companion fact, φ(30)=8, already proved as a corollary of Theorem 1's machinery). There is no claim here at the level persist.pdf's 24/25 or 9423 sections were at — an assertion presented as more than it had actually established.

## 4. Correspondences requiring independent support

**None found.** This is the most important negative result of the audit: the page is explicit and disciplined about *not* claiming correspondence beyond a shared reading. Its own text states this directly: "A reading point does not claim that a hand, a Lie algebra, a geometric space, a polygon, and a music staff are the same object." The hand/SO(10)/pentagon/staff examples are presented as independent specifications of the same numeral, with no implied structural link between them — exactly the discipline this repository's own audits (persist.pdf §3) had to arrive at the hard way. Unlike persist.pdf, readingpoint.app does not currently contain an unsupported correspondence claim.

## 5. Examples/readings rather than mathematical claims

- The hand, pentagon, 5-dimensional space, and music staff, as illustrations of "reading point 5" — descriptive, not claims requiring verification.
- The interactive integer-residue tool (enter n, read n mod 30, check membership in the eight classes) — a computational utility, not a claim.

## Conclusion

Contrary to the expectation that this audit would surface MB_0002, it mainly confirms that **MB_0001 already contains the mathematical content readingpoint.app's mod-30 material draws on** — the 8-residue class count is C(30)'s companion fact (φ(30)=8), not a separate result needing its own proof. The site's own epistemic discipline (no correspondence claims beyond a shared reading, correctly hedged necessary-vs-sufficient language) means this audit did not find a persist.pdf-style gap to formalize.

If there is a next mathematical-basis candidate, it more likely comes from a genuinely new source — a different paper, a different construction — than from re-auditing readingpoint.app's existing page, which appears to already be sound as written. Worth deciding explicitly: keep auditing readingpoint.app's other pages (if it has more than the one fetched here), or treat this page as closed and look elsewhere for MB_0002.
