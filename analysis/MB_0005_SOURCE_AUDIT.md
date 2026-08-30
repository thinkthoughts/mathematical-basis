# MB_0005 Candidate Source Audit: arXiv:2608.27372

Koehler and Sohn, "Universality and sharp thresholds for ellipsoid fitting," August 27, 2026. 79 pages.

Performed independently from the existing `engineering-statements/2608-27372.yaml` and the labreports.app report, which are downstream artifacts from the engineering-statements pipeline and are explicitly NOT used as the source here. Read only: the uploaded paper PDF (pages 1-10 and 73-79), the abstract, the explicit theorem/formula statements, and the appendix numerical experiment section.

## Three-column pre-formalization audit

The Cycle 3 criterion requires: domain constraints, claim scope, and a third boundary mechanism — **each source-native, identifiable before formalization begins**, with the third mechanism not the same shape as MB_0004's in-domain exception set.

### Column 1: Domain constraints

From Theorem 1.2's stated assumptions (page 3):
- Vectors x₁,...,xₙ ∈ ℝᵈ, i.i.d.
- Each xᵢ has **independent** coordinates
- E[x₁ⱼ] = 0 (mean zero)
- E[x²₁ⱼ] = 1 (variance one)
- sup_j ‖x₁ⱼ‖_ψ₂ ≤ Kₓ (uniformly subgaussian)
- **Asymptotic regime**: n,d → ∞ with n/d² → α ∈ (0,∞)
- κ > 1 (nondegeneracy; κ=1 collapses to {±1}ᵈ which always fits)

These are genuinely domain constraints on the objects (the random vectors) and on the sampling regime — not about the claim's scope.

### Column 2: Claim scope

From Theorem 1.2 (pages 3-4):

**(i) SAT side (α < α★(κ))**: With probability tending to 1, there exists R ≻ 0 (positive definite, not just PSD) such that xᵢᵀRxᵢ = 1 for all i. Moreover R can be chosen well-conditioned: λmax(R)/λmin(R) = O(1).

**(ii) UNSAT side (α > α★(κ))**: With probability tending to 1, there is no R ⪰ 0 such that xᵢᵀRxᵢ = 1 for all i. Moreover the optimal squared fitting error converges in probability to e★(α,κ) > 0.

**Corollary 1.3**: For Gaussian data (κ=3), α★(3) = 1/4, resolving the Gaussian ellipsoid fitting conjecture.

The claim is explicitly two-sided and quantified on both sides (SAT proven to exist, UNSAT proven with an explicit error formula).

### Column 3: Third mechanism

**α★(κ)** — the explicit phase boundary, defined via a spectral variational problem on the rescaled semicircle law ν (Equations 6-7, pages 6-7):

α★(κ) = Eκ(ωκ) = s(ωκ) + (κ-3)/2 · m(ωκ)²

where ωκ ∈ [-√2, √2] is the unique solution of ωκ = (κ-3)/2 · m(ωκ), and s(ω), m(ω) are the first two moments of the semicircle law above the spectral cutoff ω.

For κ=3 (Gaussian): ωκ = 0, so α★(3) = s(0) = 1/4.

This is not a domain constraint (it's derived from the coordinate distribution, not imposed on it) and not the claim itself (it's what determines whether the claim holds). It's a **parameter-dependent phase boundary** — a continuous function of κ that divides the (α,κ) parameter space into SAT and UNSAT regimes.

## Is α★(κ) a genuinely separate specification role, or does it collapse?

This is the key pre-formalization question Cycle 3 requires answering before building any MB_0005 artifact.

**Evidence it's genuinely separate:**
- The paper states it explicitly as an object: "There is an explicit threshold α★(κ), defined in Eq. (7), which depends only on κ" — the threshold is named, defined, and handed an equation number distinct from the theorem statement.
- The threshold has its own mathematical properties proven separately: nonincreasing in κ (Figure 1), variational representation (Eq. 7), second-order behavior at the transition (Remark 1.6 and Lemma 5.12).
- The proof is organized around the threshold: Section 5 (Gaussian model) derives α★(κ), then Sections 2-4 transfer this to the general case. The threshold is not incidental to the proof structure; it *is* the proof's organizing object.

**Evidence it partially collapses into the claim:**
- Theorem 1.2 states the claim *conditionally on* α < α★(κ) or α > α★(κ) — in principle, one could fold α★(κ) into the domain constraints as an admissibility condition ("α ≠ α★(κ)") and make the claim unconditional on the two sides. The 2608-27372.yaml does exactly this, listing α★(κ) as one of the `constraints` items ("A sharp SAT-UNSAT phase boundary occurs at α★(κ)").
- For any specific (α,κ) pair, once you know which side of α★(κ) you're on, the claim is just "an ellipsoid fit exists" or "no ellipsoid fit exists" — the threshold doesn't appear in the conclusion except as a condition.

**Assessment:** α★(κ) sits between "domain constraint" and "theorem claim" rather than cleanly inside either. It's more like a **specification of the boundary structure** — a mathematical object that organizes the claim rather than being part of the domain or the conclusion. The engineering-statements YAML folded it into `constraints`, which is one consistent choice; MB_0005 should determine independently what role this serves in the mathematical-basis framework, specifically whether `theorem_exceptions` (MB_0004's extension) generalizes to handle this case or whether a different field name is warranted.

## Verification character assessment

This is fundamentally different from MB_0001-3 and from MB_0004:

**Not independently re-derivable (79 pages, complex machinery):** The proof uses CGMT (Gordon's theorem via convex Gaussian minimax), self-concordant barriers (Lindeberg argument for universality), and random-matrix anti-concentration (the exactification step, Theorem 1.9). This is closer to MB_0004's audit regime than MB_0001-3's from-scratch derivation.

**Finite numerical realization IS tractable and already exists:** Appendix A.5 describes an SDP at d=40 using CVXPY/CLARABEL, binary search in n to estimate the largest feasible constraint density, and direct validation of the constraint xᵢᵀRxᵢ = d (not just solver status). The labreports.app notebook has already implemented and validated this. MB_0005's executable check can independently reproduce this while keeping the asymptotic theorem and the finite computation clearly separate — which is itself valuable for SG-6 (the asymptotic specification vs. computational realization distinction).

**The "verified" status is more nuanced than MB_0001-3:** The phase transition exists with high probability in the asymptotic limit. An SDP at finite d=40 is a *reading of the asymptotic specification*, not a verification of the theorem. This distinction is source-native — the paper itself separates "the theorem" (asymptotic) from "numerical experiments" (finite-dimensional) — and should be preserved explicitly rather than letting a passing computational run be mistaken for theorem verification.

## Simultaneous independent results (source provenance note)

The paper acknowledges simultaneous independent work: de la Cerda, Potechin, Tulsiani, Xu (arXiv:2608.12415, 2026) and Misiakiewicz and Wen (arXiv:2608.10184, 2026) both resolve the same conjecture in the same week. This is routine in mathematics but relevant to provenance: the Koehler-Sohn paper is not the unique contemporary source for this claim. The MB_0005 source provenance should note this, consistent with how the five-stage pipeline handles source relationships (role: canonical_reference; the specific paper chosen is one of at least three contemporaneous proofs).

## Pre-formalization verdict

**Criterion met:** All three columns are source-native and pre-identifiable. The third mechanism (α★(κ)) is genuinely different from:
- sensors-becker's domain constraints (engineering facts about the detector)
- MB_0004's in-domain necessary exceptions (hypothesis-satisfying objects carved out of the conclusion)
- A mere excluded generalization (an untested extension beyond scope)

It's a **continuous parameter-dependent phase boundary** — a function of the input distribution that partitions the parameter space rather than carving specific exceptional objects out of the conclusion.

**One real open question for MB_0005 to determine, not pre-decided here:** Does α★(κ) receive its own specification role field in the statement YAML (distinct from `theorem_exceptions`, `leading_constraints`, and `excluded_generalizations`), or does it collapse cleanly into the `statement` field as the condition-separator? The current engineering-statements YAML treats it as a constraint; a different framing is equally defensible. MB_0005 should determine this from the mathematical-basis architecture's own conventions rather than inheriting the engineering-statements framing.

**Status: promote to MB_0005.** The paper, the domain, the mechanism shape, and the verification regime are all genuinely distinct from MB_0001-4. Cycle 3's selection criterion is satisfied.
