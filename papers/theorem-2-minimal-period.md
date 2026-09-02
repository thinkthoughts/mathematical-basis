# Theorem 2 — The Divisor Case ($m \mid N$)

*This is a corollary of the General Divisor Theorem (Theorem 3, `general-divisor-theorem.md`),
not an independent derivation. It exists as its own document because the specialization audit
(`specialization-audit.md`) found that no standalone statement of this case had survived the
document's earlier revisions — only a single correction-factor line remained. This file restores
the full statement (period, count, and correction factor) as a checkable artifact, proved strictly
by substitution into the already-proved Theorem 3.*

## Setup

$N, m \ge 1$ integers with $m \mid N$, $a \in \mathbb{Z}$.

## Statement

Let $S(L) = \{n \le L : n \equiv a \pmod m,\ \gcd(n,N)=1\}$.

**Admissible branch: $\gcd(a, \mathrm{rad}(m)) = 1$.** Then $S(L)$ has exact minimal period
$$
T_{\min} = m\,\frac{\mathrm{rad}(N)}{\mathrm{rad}(m)},
$$
with exactly
$$
\varphi(R), \qquad R = \frac{\mathrm{rad}(N)}{\mathrm{rad}(m)},
$$
accepted values per minimal period, and correction factor (against the naive predicted count
$\frac{\varphi(N)}{N}\cdot\frac{L}{m}$)
$$
C(N,m) = \frac{m}{\varphi(m)}.
$$

**Complementary branch: $\gcd(a, \mathrm{rad}(m)) > 1$.** Then $S(L) = \varnothing$ for
every $L$.

## Proof — by substitution into Theorem 3

Theorem 3 (proved, not re-derived here) states, for arbitrary $N, m\ge1, a\in\mathbb Z$, with
$d=\mathrm{rad}(\gcd(m,N))$ and $R=\mathrm{rad}(N)/d$:

- admissible iff $\gcd(a,d)=1$, else $S(L)=\varnothing$ for every $L$;
- minimal period $T_{\min}=mR$;
- exact count $\varphi(R)$ per minimal period;
- $C(N,m) = d/\varphi(d)$.

**Step 1: specialize $d$.** Since $m \mid N$, every prime dividing $m$ also divides $N$, so
$\gcd(m,N)=m$ and therefore
$$
d = \mathrm{rad}(\gcd(m,N)) = \mathrm{rad}(m).
$$
This is a direct substitution, not a new argument: $d$ is defined identically in both documents,
and $m\mid N$ collapses $\gcd(m,N)$ to $m$ by definition of divisibility.

**Step 2: specialize the admissibility condition.** Theorem 3's condition $\gcd(a,d)=1$ becomes,
under Step 1, exactly $\gcd(a,\mathrm{rad}(m))=1$ — matching this document's stated
admissible branch verbatim. The complementary branch follows identically from Theorem 3's
complementary branch.

**Step 3: specialize $R$ and $T_{\min}$.** Substituting $d=\mathrm{rad}(m)$ into
$R=\mathrm{rad}(N)/d$ gives
$$
R = \frac{\mathrm{rad}(N)}{\mathrm{rad}(m)},
$$
matching this document's stated $R$. Then $T_{\min}=mR$ becomes
$$
T_{\min} = m\,\frac{\mathrm{rad}(N)}{\mathrm{rad}(m)},
$$
matching the statement above exactly. The exact count per minimal period, $\varphi(R)$, carries
over unchanged from Theorem 3, since $R$ itself is just the substituted value — no new argument
is needed for the count or the minimality of $T_{\min}$, both of which are already proved for
arbitrary $(N,m,a)$ in Theorem 3 and therefore hold here as a special case.

**Step 4: specialize $C(N,m)$.** Theorem 3 gives $C=d/\varphi(d)$. Substituting
$d=\mathrm{rad}(m)$:
$$
C(N,m) = \frac{\mathrm{rad}(m)}{\varphi(\mathrm{rad}(m))}.
$$
By the exponent-blindness lemma (`general-divisor-theorem.md`, "Lemma (exponent-blindness)"),
applied to $k=m$:
$$
\frac{m}{\varphi(m)} = \frac{\mathrm{rad}(m)}{\varphi(\mathrm{rad}(m))}.
$$
Hence $C(N,m) = m/\varphi(m)$, matching the statement above exactly. $\blacksquare$

No step above required re-deriving CRT, the periodicity argument, or the ratio computation — all
four were already established for arbitrary $(N,m,a)$ in Theorem 3, and $m\mid N$ only fixes what
$d$, $R$, and $T_{\min}$ evaluate to.

## Note on period vs. Theorem 1′'s period

This is the *minimal* period. Where $m$ additionally happens to be a unitary divisor of $N$
(Theorem 1′'s hypothesis, a further specialization of $m\mid N$), Theorem 1′ states a valid period
of $N$ itself — but $N$ is generally a proper multiple of the minimal period given here,
$T_{\min}=m\mathrm{rad}(N/m)$, whenever $N/m$ has a repeated prime factor. See
`specialization-audit.md` and `specialization-audit-repaired.md` for the worked comparison.

## Worked example: $N=12, m=2, a=1$

$m\mid N$ ($2\mid12$). $\mathrm{rad}(m)=\mathrm{rad}(2)=2$. $\gcd(a,\mathrm{rad}(m))=\gcd(1,2)=1$: admissible branch.

$$
d=2,\qquad R=\frac{\mathrm{rad}(12)}{\mathrm{rad}(2)}=\frac{6}{2}=3,\qquad T_{\min}=2\cdot3=6,\qquad C=\frac{2}{\varphi(2)}=2.
$$

Direct check: $n\equiv1\pmod2$ (odd), coprime to $12$ (i.e. also not divisible by $3$), in
$[1,6]$: $\{1,5\}$ — count $2 = \varphi(R) = \varphi(3)$. ✓

Naive prediction: $\varphi(12)/12\cdot(6/2) = (4/12)\cdot3 = 1$. Ratio $2/1=2=C$. ✓ And
$m/\varphi(m)=2/\varphi(2)=2$, matching $C$ directly, as the theorem states.

This is the same $(N,m)$ pair used as the internal-consistency spot check in
`specialization-audit.md`; it is reproduced here as this document's own worked example so the
artifact is self-contained.

## Relation to the hierarchy

Theorem 2 is the specialization of Theorem 3 to $m\mid N$. It is itself further specialized by:
- **Theorem 1′** (`extended-unitary-divisor-theorem.md`): $m$ additionally a unitary divisor of
  $N$ — a strictly stronger hypothesis than $m\mid N$ alone.
- **Theorem 1** (printed paper, Draft v3.1): $N$ additionally squarefree (forcing every divisor to
  be unitary automatically, collapsing Theorem 1′'s coarser period into the minimal one as well).

This document does not restate those further specializations; see `specialization-audit-repaired.md`
for the mechanical checks connecting all four documents.
