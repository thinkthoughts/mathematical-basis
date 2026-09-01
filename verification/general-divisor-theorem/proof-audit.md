# Proof Audit: `general-divisor-theorem.md` against `theorem-specification.md`

Specification treated as authoritative throughout. `theorem-specification.md` was not
modified. Derivation document audited: `general-divisor-theorem.md` (Section "Theorem 3,
Final form" and its four proof paragraphs).

**Headline result: two real gaps found, both around the same missing lemma. Neither is a
counterexample — both are "true but unproven in this document" — but both should be closed
before calling the proof complete, and one of them (Claim 3) is exactly the failure mode
flagged for stress-testing (the earlier $mN'$ candidate looked plausible for the same
reason: an assertion stood in for a periodicity argument).**

---

## Claim 1 — Dichotomy on $a$

**SPEC CLAIM.** If $\gcd(a,d)=1$: governed by Claims 2–4. If $\gcd(a,d)>1$: $S(L)=\varnothing$
for every $L$.

**PROOF LOCATION.** "Proof of the case split and the count," first half (up through "...giving
the zero case").

**DEPENDENCIES.** Definition of $d$; $p\mid m \Rightarrow n\equiv a\pmod p$ for $n\equiv a\pmod m$
(trivial reduction, not a named external lemma).

**AUDIT.** Variables match the spec exactly: $d=\operatorname{rad}(\gcd(m,N))$, same object
used both places. The argument is: fix $n\equiv a\pmod m$; for each $p\mid d$, since $p\mid m$,
$n\equiv a\pmod p$, so $n$ and $a$ agree on divisibility by $p$. If $\gcd(a,d)=1$ this holds for
every $p\mid d$ simultaneously, so every such $n$ is coprime to $d$. If instead some $p\mid d$
divides $a$, then that same $p$ divides *every* $n$ in the class, and since $p\mid d\mid N$,
every such $n$ fails $\gcd(n,N)=1$ — giving $S(L)=\varnothing$ for literally every $L\ge1$, not
just asymptotically. Quantifiers check out: the zero-branch argument produces a single shared
prime that kills *every* candidate $n$, which is exactly what "$S(L)=\varnothing$ for every $L$"
requires (not merely "most $n$ excluded"). No hidden assumptions found: doesn't assume $a>0$,
doesn't assume $m\mid N$, doesn't quietly replace $N$ with $\operatorname{rad}(N)$ anywhere in
this step.

**STATUS: PROVED AS STATED.**

---

## Claim 2 — Exact per-period count

**SPEC CLAIM.** For every $n_0$, the count of accepted values in *any* half-open window of
length $T_{\min}$ is exactly $\varphi(R)$. Equivalently $|S(qT_{\min})|=q\varphi(R)$ for every
$q\ge0$.

**PROOF LOCATION.** "Proof of the case split and the count," second half: "Assume now
$\gcd(a,d)=1$: ... Since $\gcd(m,R)=1$, CRT gives, within one block of length $mR$, a bijection
between $\{n\bmod mR: n\equiv a\pmod m\}$ and $\mathbb Z/R\mathbb Z$; exactly $\varphi(R)$ are
coprime to $R$. This is the exact count per period $mR$."

**DEPENDENCIES.** CRT (existence/uniqueness for coprime moduli, standard, correctly invoked
since $\gcd(m,R)=1$ is established in the Setup).

**AUDIT.** The reduction $\gcd(n,N)=1 \iff \gcd(n,R)=1$ (given $n\equiv a\pmod m$,
$\gcd(a,d)=1$) is correctly re-derived, not just asserted — it follows from Claim 1's argument
one paragraph earlier. The CRT bijection claim itself is correct as a statement about *complete
residue systems modulo $mR$*: any $mR$ consecutive integers realize each residue class mod $mR$
exactly once, so among them, the $R$ integers satisfying $n\equiv a\pmod m$ realize each residue
mod $R$ exactly once (this is what the bijection is really saying), giving exactly $\varphi(R)$
coprime-to-$R$ among them.

**Gap.** As *written*, the proof says "within **one block** of length $mR$" — most naturally
read as referring to a specific interval (e.g. the first period), not to an arbitrary window.
The underlying fact does generalize immediately, because *any* window of $mR$ consecutive
integers is a complete residue system mod $mR$ — but the document never states this
generalization, and the frozen spec's Claim 2 is explicitly phrased as "any half-open window,"
not "the first window." This matters concretely for the theorem's own stated formula
$|S(L)|=q\varphi(R)+R_{\mathrm{rem}}(s)$: getting $q\varphi(R)$ for $q$ full periods either needs
(a) the arbitrary-window fact applied to each of the $q$ windows directly, or (b) positional
periodicity of the indicator (so all $q$ blocks are provably identical to the first). The
document supplies neither explicitly — it computes one block's count and moves on. This is a
real, fixable gap, not a computational red flag (the strengthened test suite verified exactly
this claim, exhaustively, over 4.5M arbitrary windows, with zero counterexamples) — but the
*written proof* doesn't yet cover it.

**Suggested fix (one sentence):** "Since any interval of $mR$ consecutive integers is a complete
residue system mod $mR$, the same bijection argument applies verbatim to every such interval, not
only $[1,mR]$; hence the count is $\varphi(R)$ in every window of length $T_{\min}$, and summing
over $q$ disjoint such windows gives $|S(qT_{\min})|=q\varphi(R)$."

**STATUS: PROOF GAP** (true and computationally confirmed; not yet established in writing for
arbitrary windows, only for one unspecified block).

---

## Claim 3 — Minimality of $T_{\min}$

**SPEC CLAIM.** $T_{\min}=mR$ is the exact minimal positive period of
$\mathbb{1}[n\equiv a\pmod m,\ \gcd(n,N)=1]$, under $\gcd(a,d)=1$ (the spec scopes this claim to
the nonzero branch only — see note at the end on this).

**PROOF LOCATION.** "Proof of minimality of $T_{\min}=mR$," full paragraph.

**DEPENDENCIES.** CRT (for constructing $n_0$ and $n_1$); the definition of "period" as a
biconditional ($n$ accepted $\iff$ $n+t$ accepted, for all $n$); squarefreeness of $R$ (for the
"every prime of $R$ divides $t$ $\Rightarrow$ $R\mid t$" step); **and, un-cited, the claim that
$T_{\min}$ itself *is* a period** — this last one is the load-bearing gap.

**AUDIT — the "$m\mid t$" step.** Correct and self-contained. $n_0$ is constructed via CRT to be
accepted; if $t$ is a period then $n_0+t$ is accepted, hence $\equiv a\pmod m$; since $n_0\equiv
a\pmod m$ too, $t\equiv0\pmod m$. No gap.

**AUDIT — the "$p\mid t$ for every $p\mid R$" step.** Correct and self-contained. For a prime
$p\mid R$, assuming $p\nmid t$, the constructed $n_1$ is accepted (coprime to $d$ via
$\gcd(a,d)=1$ as in Claim 1; coprime to $R$ by construction, using $p\nmid t$ to make
$n_1\equiv-t\pmod p$ nonzero mod $p$) but $n_1+t\equiv0\pmod p$ makes it *not* coprime to $R$,
hence not accepted — contradicting the one-directional implication built into "period." This
step never needs $m\mid t$ from the previous paragraph (it's independently valid via the
coprimality-to-$R$ failure alone), and never smuggles in $m\mid N$ or squarefreeness of $N$
itself (only of $R$, which is squarefree by construction). No gap here either.

**AUDIT — the closing line.** "Hence $p\mid t$ for every prime $p\mid R$; since $R$ is
squarefree, $R\mid t$. Combined with $m\mid t$ and $\gcd(m,R)=1$: $mR\mid t$, so $t\ge mR$.
**Since $mR$ is itself a period**, $T_{\min}=mR$ is exactly minimal."

The bolded clause is asserted, not proved, anywhere in this document. What has actually been
shown up to this point is: *if* $t>0$ is a period, *then* $mR\mid t$. That is a valid lower
bound on periods — but it only becomes "the minimal period is $mR$" once you also know $mR$
itself *is* a period. Nothing in the "count" proof (Claim 2's paragraph) establishes this either:
that paragraph proves a *count* fact (exactly $\varphi(R)$ accepted values per block), and count
invariance across blocks does **not**, in general, imply positional periodicity of the underlying
0/1 sequence (a length-$k$ window can have constant sum without the sequence itself repeating
with period $k$ — e.g. $1,1,0,0,1,1,0,0,\dots$ has non-constant length-2 window sums despite being
period-4, illustrating that window-sum behavior and positional periodicity are logically separate
facts that happen to coincide only under further structure). So the minimality proof currently
rests on an unproven premise.

**Is the premise true?** Yes, and provable directly, independent of the windowed-count argument:
write the indicator as a product of two conditions, $\mathbb 1[n\equiv a\pmod m]$ (periodic with
period $m$, trivially) and $\mathbb 1[\gcd(n,R)=1]$ (periodic with period $R$, since coprimality
to a squarefree number depends only on $n\bmod R$) — this second reduction itself relies on the
$\gcd(n,N)=1\iff\gcd(n,R)=1$ fact from Claim 1, so it is properly scoped to the $\gcd(a,d)=1$
branch. A product of a period-$m$ function and a period-$R$ function is periodic with period
$\operatorname{lcm}(m,R)=mR$ (since $m\mid mR$ and $R\mid mR$ individually). This is a two-line
argument that is simply absent from the document.

**STATUS: PROOF GAP.** The minimality *bound* ($t\ge mR$ for any period $t$) is fully proved.
The minimality *conclusion* ($mR$ achieves that bound, i.e. is itself a period) is asserted, not
proved. This is precisely the kind of gap flagged for scrutiny — structurally the same failure
shape as the earlier $mN'$ mistake (an unproven periodicity/minimality assertion standing in for
an argument) — except here the assertion happens to be true, whereas $mN'$ was false. The
document does not currently distinguish "true and I checked" from "true and I asserted," and this
audit is exactly the mechanism that should have caught that distinction before freezing.

**Zero-branch scope, checked explicitly (per request).** The document does correctly restrict
this proof to $\gcd(a,d)=1$: "Assume $\gcd(a,d)=1$ (else the accepted set is empty and the
question is vacuous)." This matches the frozen spec's own scoping of Claim 3 to the nonzero
branch. On the zero branch the indicator is identically $0$, whose minimal positive period is
$1$ (any $t$ works, trivially, so the minimal one is $1$) — not $T_{\min}$ in general, and
neither the spec nor the document claims otherwise. No gap on this point; flagged as verified,
not as a finding.

---

## Claim 4 — Correction factor exact identity

**SPEC CLAIM.** $\varphi(R)\cdot N\cdot\varphi(d) = \varphi(N)\cdot R\cdot d$ (exact integer
identity).

**PROOF LOCATION.** "Proof of the ratio $C(N,m)=d/\varphi(d)$," full paragraph and display.

**DEPENDENCIES.** $N=AB$ decomposition with $\operatorname{rad}(A)=d$, $\operatorname{rad}(B)=R$,
$\gcd(A,B)=1$; multiplicativity of $\varphi$ over coprime arguments ($\varphi(N)=\varphi(A)\varphi(B)$
— standard, correctly invoked, not restated/proved in this document, which is acceptable for a
fact this standard); and **"exponent-blindness" of $k/\varphi(k)$** ($\varphi(B)/B=\varphi(R)/R$
since $\operatorname{rad}(B)=R$, and later $A/\varphi(A)=d/\varphi(d)$ since
$\operatorname{rad}(A)=d$) — used twice, cited nowhere.

**AUDIT.** Re-deriving the algebra directly: the claimed chain is
$$
C = \frac{\varphi(R)/(mR)}{\varphi(N)/(Nm)} = \frac{N\varphi(R)}{R\varphi(N)}
= \frac{AB\varphi(R)}{R\varphi(A)\varphi(B)} = \frac{AB\varphi(R)}{R\varphi(A)(B\varphi(R)/R)}
= \frac{A}{\varphi(A)} = \frac{d}{\varphi(d)}.
$$
Checking each equality independently: first equality is definitional (density ratio). Second
substitutes $N=AB$, $\varphi(N)=\varphi(A)\varphi(B)$ — correct given multiplicativity. Third
substitutes $\varphi(B)=B\varphi(R)/R$ — this is exactly the exponent-blindness fact, used but
never stated. Fourth is pure algebraic cancellation (the $R$'s and one $B$ cancel) — checked by
hand, correct: $\dfrac{AB\varphi(R)}{\varphi(A)\,B\varphi(R)} = \dfrac{A}{\varphi(A)}$. Fifth
substitutes $A/\varphi(A)=d/\varphi(d)$ — exponent-blindness again, same uncited fact. The
document does *not* prove this identity is exact rather than asymptotic — but re-checking, every
step above is an exact algebraic equality (no limits, no $O(\cdot)$ terms), so the chain, if its
one external input is granted, does establish the frozen spec's exact cross-multiplied identity,
not merely a limiting ratio.

The exponent-blindness fact itself ($k/\varphi(k)$ depends only on $\operatorname{rad}(k)$) is
true and elementary ($\varphi(p^e)/p^e=1-1/p$ for every $e\ge1$, independent of $e$; multiplicativity
does the rest) — it appeared as an explicit, proved lemma in an earlier draft of this same
document lineage but is **not present in the final file audited here**. This is a genuine
citation gap: a reader auditing this file in isolation has no way to verify the third and fifth
equalities above without reconstructing the lemma themselves.

**STATUS: USES UNSTATED ASSUMPTION.** The algebra is correct and the identity does hold exactly
as the spec requires, but the proof leans on an uncited external fact not stated anywhere in this
file. This should be promoted to an explicit, proved lemma before the document is considered
self-contained.

---

## Dependency map (what's actually load-bearing)

```
                    CRT (existence, coprime moduli)
                     |         |          |
                     v         v          v
Claim 1 -----------> uses in reduction n≡a(mod m) => coprime-to-d automatic
   |
   v (feeds into)
Claim 2 -----------> CRT bijection {n mod mR : n≡a(m)} <-> Z/RZ
   |                 [GAP: stated for "one block," not proved for arbitrary windows]
   |
   v (needed as premise, not currently supplied)
Claim 3 -----------> CRT witnesses n0, n1  =>  lower bound t >= mR  [solid]
                     "mR is a period"  [GAP: asserted, not derived --
                      true via: (period-m fn) x (period-R fn) has period lcm(m,R)=mR,
                      itself resting on Claim-1's n≡a(m) => coprime-to-d reduction]

Claim 4 -----------> N = A*B, gcd(A,B)=1
                     phi(N) = phi(A)*phi(B)   [standard multiplicativity, uncited but safe]
                     phi(B)/B = phi(R)/R,
                     A/phi(A) = d/phi(d)      [GAP: exponent-blindness lemma, uncited, not
                                                restated in this file even though it appeared
                                                in an earlier draft in the same lineage]
```

**Single most load-bearing missing piece:** the positional-periodicity lemma ("a function that is
periodic mod $m$ times a function periodic mod $R$, with $\gcd(m,R)=1$, is periodic mod $mR$").
It's needed to fully close both Claim 2 (arbitrary-window form) and Claim 3 (the premise that
$T_{\min}$ is itself a period), and it is not stated anywhere in the current document — everywhere
it's needed, the document instead does a windowed-count computation (Claim 2) or a bare assertion
(Claim 3) that happen to be consistent with it but don't establish it.

**Second missing piece:** the exponent-blindness lemma for $k/\varphi(k)$, needed twice in Claim 4,
present in an earlier draft but dropped from this final file.

---

## Summary

| Claim | Status |
|---|---|
| 1 (dichotomy) | PROVED AS STATED |
| 2 (exact count) | PROOF GAP — arbitrary-window generalization not written down |
| 3 (minimality) | PROOF GAP — "$T_{\min}$ is a period" asserted, not proved |
| 4 (ratio identity) | USES UNSTATED ASSUMPTION — exponent-blindness lemma uncited |

No counterexamples. No claim found to be proving a strictly weaker statement than what's frozen
in the spec — every gap found is a missing derivation step for a fact that is true (and, for
Claims 2 and 3's disputed pieces, already computationally confirmed exhaustively). Per
instructions, none of these gaps have been silently repaired in `general-divisor-theorem.md`;
they're reported here for a deliberate fix pass.
