# Specialization Audit: Theorem 3 ⊃ Theorem 2 ⊃ Theorem 1′ ⊃ Theorem 1

Starting point (load-bearing, from the repaired `general-divisor-theorem.md`):
$$
d=\operatorname{rad}(\gcd(m,N)),\qquad R=\operatorname{rad}(N)/d,\qquad T_{\min}=mR,\qquad C=\frac{d}{\varphi(d)}.
$$
Each specialization below imposes one additional hypothesis on $(N,m,a)$, substitutes it into
these four formulas mechanically, and checks the result against the specialization's existing
independent statement. No independent re-proof is attempted unless a mismatch turns up.

**Headline result: Theorem 1 matches exactly. Theorem 1′ matches, with one point that needs
stating precisely rather than glossed over — its period is the coarser, non-minimal one, by
design, not an error. Theorem 2 cannot be checked against a saved document, because no such
document exists — this is reported as a gap, not silently patched.**

---

## Theorem 2 — additional hypothesis: $m \mid N$

**Mechanical substitution.** If $m\mid N$, then every prime of $m$ divides $N$, so
$\gcd(m,N)=m$ and $d=\operatorname{rad}(m)$. Then:
$$
R = \frac{\operatorname{rad}(N)}{\operatorname{rad}(m)}, \qquad
T_{\min} = m\cdot\frac{\operatorname{rad}(N)}{\operatorname{rad}(m)}, \qquad
C = \frac{\operatorname{rad}(m)}{\varphi(\operatorname{rad}(m))} = \frac{m}{\varphi(m)}
$$
(the last equality by the exponent-blindness lemma, applied to $k=m$).

**Check against the existing statement.** The current "Specializations" section of
`general-divisor-theorem.md` states only: "$m\mid N \Rightarrow d=\operatorname{rad}(m)$, giving
$C=m/\varphi(m)$ (Theorem 2)." This one-line claim is confirmed by the substitution above — no
mismatch on the correction factor.

**Gap found.** There is no `Theorem 2` as a saved, standalone document anywhere in the repo's
current file set. Tracing the actual history in this conversation: an intermediate "Theorem 2 —
minimal period" was derived and written into an earlier revision of this same file
(`general-divisor-theorem.md`), using $N_m$ = full prime-power part of $N$ for $m$'s primes and
$N' = N/N_m$, arriving at exactly $T_{\min}=m\,\operatorname{rad}(N')$ and $C=m/\varphi(m)$ — but
that content was overwritten in place when the file was rewritten to drop the $m\mid N$
restriction and become Theorem 3. It was never saved as its own file before being superseded. So
"Theorem 2" currently exists only as one bullet point (the $C=m/\varphi(m)$ line) plus a name used
in the hierarchy sentence at the bottom of the document — not as an independently checkable
artifact.

**Numerical spot-check (since there's no document to check against, checking the formula's
internal consistency instead).** $N=12=2^2\cdot3$, $m=2$ ($m\mid N$). $d=\operatorname{rad}(2)=2$,
$R=\operatorname{rad}(12)/2 = 6/2=3$, $T_{\min}=2\cdot3=6$, $C=2/\varphi(2)=2$. Direct check:
$n\equiv1\pmod2$ (take $a=1$, admissible since $\gcd(1,2)=1$), coprime to $12$: odd and not
divisible by $3$. In $[1,6]$: $\{1,5\}$ — count $2=\varphi(R)=\varphi(3)$. ✓ Consistent with
Theorem 3 itself (as expected — this is a specialization of an already-proved theorem, not a new
claim), but this doesn't substitute for having a citable Theorem 2 statement to check against.

**STATUS: GAP — no standalone Theorem 2 document exists.** The mechanical specialization is
internally consistent and matches the one line about Theorem 2 that does survive in the current
document, but the audit cannot confirm agreement with "Theorem 2" as a whole because no complete,
independently-stated version of it survives anywhere in the current file set. Recommend either
(a) writing `theorem-2-minimal-period.md` as its own frozen artifact before the hierarchy claim is
considered fully verified, or (b) formally retiring the name "Theorem 2" and describing the
hierarchy as three stages (1 ⊂ 1′ ⊂ 3) rather than four, since the fourth stage currently has no
independent existence to defend.

---

## Theorem 1′ — additional hypothesis: $m$ unitary in $N$ ($\gcd(m,N/m)=1$), plus $\gcd(a,m)=1$

**Mechanical substitution.** Unitary means $m$ absorbs the *full* exponent of each of its primes
in $N$, i.e. $N_m=m$ exactly (using the notation from the audit of Theorem 2 above). So
$d=\operatorname{rad}(m)$ as before, and write $N'=N/m$ (Theorem 1′'s own notation). Then
$\operatorname{rad}(N)=\operatorname{rad}(m)\cdot\operatorname{rad}(N')$ (coprime factors), so
$$
R = \frac{\operatorname{rad}(N)}{\operatorname{rad}(m)} = \operatorname{rad}(N'), \qquad
T_{\min} = mR = m\cdot\operatorname{rad}(N'), \qquad
C = \frac{m}{\varphi(m)}.
$$

**Check against Theorem 1′'s existing statement** (`extended-unitary-divisor-theorem.md`):
Theorem 1′ claims period $N$ (not $T_{\min}$), count $\varphi(N/m)=\varphi(N')$ per period $N$,
and $C(m)=m/\varphi(m)$.

The correction factor matches exactly: $C=m/\varphi(m)$ both ways. No mismatch there.

**The period does not match — by design, not by error.** Theorem 1′'s period is $N=m\cdot N'$;
Theorem 3's minimal period is $T_{\min}=m\cdot\operatorname{rad}(N')$. These are equal only when
$N'$ is already squarefree ($\operatorname{rad}(N')=N'$); otherwise $N=T_{\min}\cdot(N'/\operatorname{rad}(N'))$,
i.e. Theorem 1′'s period is a genuine (non-minimal) integer multiple of the true minimal period.
This is exactly the phenomenon that motivated the minimal-period refinement in the first place —
the $N=18,m=2$ example used throughout this derivation chain **is** an instance of unitary $m$
with non-squarefree $N'$ ($N'=9$), which is precisely why it was able to expose the gap between
$T=mN'=18$ and $T_{\min}=6$. So this is not a new discrepancy; it's the same one already found,
resolved, and tested earlier in this derivation chain, now confirmed to be exactly reproduced by
mechanical substitution rather than needing a separate re-derivation.

**Consistency check on the count.** Over Theorem 1′'s stated period $N$, its claimed count is
$\varphi(N')$. Over $T_{\min}$, Theorem 3 gives $\varphi(R)=\varphi(\operatorname{rad}(N'))$ per
period, and $N/T_{\min} = N'/\operatorname{rad}(N')$ periods fit inside $N$, so Theorem 3 predicts
a total of $\bigl(N'/\operatorname{rad}(N')\bigr)\cdot\varphi(\operatorname{rad}(N'))$ over the
same interval $N$. Using exponent-blindness ($\varphi(N')/N' = \varphi(\operatorname{rad}(N'))/\operatorname{rad}(N')$),
this equals $N'\cdot\varphi(\operatorname{rad}(N'))/\operatorname{rad}(N') = \varphi(N')$ —
matching Theorem 1′'s claimed count exactly. So the two statements agree on the *total* count over
$N$; they differ only in whether that count is attributed to one non-minimal period or several
minimal ones — a labeling difference, not a mathematical one.

**Numerical spot-check.** $N=18$, $m=2$ (unitary: $\gcd(2,9)=1$), $N'=9$. Theorem 1′: period $18$,
count $\varphi(9)=6$. Theorem 3: $d=2$, $R=\operatorname{rad}(9)=3$, $T_{\min}=6$, count $\varphi(3)=2$
per period, $\times3$ periods in $18$ = $6$. Matches.

**STATUS: PROVED AS COROLLARY**, with the period explicitly flagged as the coarser (non-minimal)
one, consistent with — not contradicting — Theorem 3's finer accounting.

---

## Theorem 1 — additional hypothesis: $N=P_k$ (squarefree primorial), $m$ any squarefree divisor
of $P_k$ with $m>1$, $\gcd(a,m)=1$

**Mechanical substitution.** $P_k$ squarefree $\Rightarrow$ every divisor of $P_k$ is squarefree
and automatically unitary (this is stated in `extended-unitary-divisor-theorem.md`'s own "Relation
to Theorem 1" section, and re-confirmed here). So $m$ is squarefree, meaning
$\operatorname{rad}(m)=m$ exactly, giving $d=m$ directly (no lemma needed — $m$ already equals its
own radical). $\operatorname{rad}(P_k)=P_k$ (squarefree), so
$$
R = \frac{P_k}{m}, \qquad T_{\min} = m\cdot\frac{P_k}{m} = P_k, \qquad C = \frac{m}{\varphi(m)}.
$$
Additionally, since $P_k$ is squarefree, $P_k/m$ (a divisor of a squarefree number) is itself
automatically squarefree, so $\operatorname{rad}(P_k/m)=P_k/m=R$ — there is no "coarser vs.
minimal" gap to worry about here at all; $T_{\min}$ and the naive $N=P_k$ period coincide
automatically. This is the mechanical reason Theorem 1 never needed the minimal-period distinction
that Theorem 1′ and Theorem 3 required: squarefreeness of $N$ propagates to $N/m$, collapsing the
two notions of period into one.

**Check against Theorem 1's existing statement** (uploaded paper, Draft v3.1, Theorem 1 /
Corollary 1): period $P_k$, exact per-period count $\varphi(P_k/m)$, $C(m)=m/\varphi(m)$.

All three match exactly: period $T_{\min}=P_k$ ✓, count $\varphi(R)=\varphi(P_k/m)$ ✓ (since
$R=P_k/m$ exactly here, not merely its radical), correction factor $C=m/\varphi(m)$ ✓.

**Numerical spot-check**, reusing the paper's own worked example: $P_k=210=2\cdot3\cdot5\cdot7$,
$m=6$. $d=\operatorname{rad}(6)=6=m$ (squarefree). $R=210/6=35$. $T_{\min}=6\cdot35=210=P_k$. ✓.
$C=6/\varphi(6)=6/2=3$, matching Corollary 1's $C(6)=3$ exactly. Count $\varphi(R)=\varphi(35)=24$,
matching the paper's own per-period count $\varphi(P_k/m)=\varphi(35)=24$ (consistent with Table 1's
reported exact counts scaling correctly across $L=10^5,\dots,10^8$).

**STATUS: PROVED AS COROLLARY. Exact match, no caveats.**

---

## Summary

| Specialization | Extra hypothesis | Period | Count | $C$ | Status |
|---|---|---|---|---|---|
| Theorem 2 | $m\mid N$ | matches internally, no doc to check | matches internally | matches the one surviving line | **GAP — no standalone document** |
| Theorem 1′ | $m$ unitary in $N$, $\gcd(a,m)=1$ | coarser, not minimal (by design) | matches (same total) | matches exactly | **PROVED AS COROLLARY** (period caveat noted) |
| Theorem 1 | $N=P_k$ squarefree, $m$ squarefree, $\gcd(a,m)=1$ | matches exactly | matches exactly | matches exactly | **PROVED AS COROLLARY**, exact |

**Is the hierarchy genuinely a chain of corollaries?** For Theorem 1′ and Theorem 1: yes,
confirmed by direct mechanical substitution with no independent re-derivation required, and no
mismatch found (the one apparent "mismatch" at Theorem 1′, the period, is the same
already-diagnosed coarser-vs-minimal distinction from earlier in this derivation, not a new
problem). For Theorem 2: **not yet fully verifiable**, because the object being claimed as a
corollary was never preserved as an independent artifact — the chain's third link exists only as
a name and a one-line formula, not a checkable theorem statement. This should be resolved (by
writing the missing document or by dropping the name from the hierarchy) before describing
"Theorem 1 ⊂ Theorem 1′ ⊂ Theorem 2 ⊂ Theorem 3" as a fully closed, audited chain.
