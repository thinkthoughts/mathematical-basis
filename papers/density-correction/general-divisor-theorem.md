# The General Divisor Theorem

*Final form. Supersedes the unitary-divisor extension and both earlier drafts of the general theorem. All are retained in `papers/` as intermediate derivations — see the note at the end. This version (a) weakens $\gcd(a,m)=1$ to the sharp condition $\gcd(a,d)=1$, (b) states the complementary zero-count case explicitly, and (c) gives a cleaner, fully explicit minimality proof via a single CRT construction.*

## Motivation

The previous draft still required $\gcd(a,m)=1$. But by the same logic that made $m\mid N$ removable, this is stronger than needed: primes of $m$ that don't divide $N$ can never affect $\gcd(n,N)$, so $a$ only needs to avoid the primes $m$ and $N$ actually *share*. The sharp hypothesis is $\gcd(a,d)=1$ where $d=\mathrm{rad}(\gcd(m,N))$ — and when that fails, the count isn't merely different, it's identically zero, giving a genuine dichotomy rather than a boundary case to patch around.

## Setup

$N$ any positive integer, $m>1$ any positive integer, $a$ any integer. Define
$$
d=\mathrm{rad}(\gcd(m,N))=\prod_{p\mid m,\,p\mid N} p, \qquad R=\prod_{p\mid N,\,p\nmid m} p,
$$
so $\gcd(m,R)=1$ and $dR=\mathrm{rad}(N)$.

## Theorem 3 (Final form)

Let $S(L) = \{n\le L : n\equiv a\!\!\pmod m,\ \gcd(n,N)=1\}$.

**Case $\gcd(a,d)=1$.** Then
$$
|S(L)| = q\,\varphi(R) + R_{\mathrm{rem}}(s), \qquad L=qT_{\min}+s,\ 0\le s<T_{\min},
$$
with minimal period $T_{\min}=mR=\mathrm{lcm}(m,\mathrm{rad}(N))$, and against the naive predicted count $\frac{\varphi(N)}{N}\cdot\frac{L}{m}$,
$$
C(N,m) = \frac{d}{\varphi(d)} = \prod_{p\mid \gcd(m,N)} \frac{p}{p-1}.
$$

**Case $\gcd(a,d)>1$.** Then $S(L) = \varnothing$ for every $L$: some prime $p\mid d$ divides both $a$ and $m$, so $n\equiv a\pmod m$ forces $p\mid n$; since $p\mid d\mid N$ also, $\gcd(n,N)\ge p>1$ always.

**Proof of the case split and the count.** Fix $n\equiv a\pmod m$. For each prime $p\mid d$ (shared by $m,N$): $p\mid m\Rightarrow n\equiv a\pmod p$, so $n$ is coprime to $p$ iff $a$ is. So *every* accepted $n$ is automatically coprime to all of $d$ exactly when $\gcd(a,d)=1$; if instead some $p\mid d$ divides $a$, *no* $n$ in the class is coprime to $p$, giving the zero case. Assume now $\gcd(a,d)=1$: every $n\equiv a\pmod m$ is coprime to $d$, so $\gcd(n,N)=1 \iff \gcd(n,R)=1$ (the only primes of $N$ left to check are $R$'s). Since $\gcd(m,R)=1$, CRT gives, within one block of length $mR$, a bijection between $\{n\bmod mR: n\equiv a\pmod m\}$ and $\mathbb Z/R\mathbb Z$; exactly $\varphi(R)$ are coprime to $R$. This is the exact count per period $mR$.

**Proof of minimality of $T_{\min}=mR$.** Assume $\gcd(a,d)=1$ (else the accepted set is empty and the question is vacuous). By CRT (using $\gcd(m,R)=1$), pick
$$
n_0 \equiv a \pmod m, \qquad n_0 \equiv 1 \pmod R.
$$
Then $n_0$ is accepted: coprime to $d$ by the case hypothesis, coprime to $R$ since $n_0\equiv1$. Let $t>0$ be any period of the accepted-set indicator, i.e. $n$ accepted $\iff$ $n+t$ accepted, for all $n$.

Since $n_0$ is accepted, $n_0+t$ is accepted, so $n_0+t\equiv a\pmod m$, giving $t\equiv0\pmod m$: $m\mid t$.

Fix any prime $p\mid R$. Suppose $p\nmid t$. By CRT choose
$$
n_1 \equiv a \pmod m,\qquad n_1\equiv -t \pmod p,\qquad n_1\equiv 1\pmod{q}\ \text{for every prime } q\mid R,\ q\ne p.
$$
(These moduli are pairwise coprime, so this system is solvable.) Since $p\nmid t$, $-t\not\equiv0\pmod p$, so $n_1\not\equiv0\pmod p$; combined with $n_1\equiv1$ mod every other prime of $R$, $n_1$ is coprime to $R$, hence accepted. But $n_1+t\equiv -t+t=0\pmod p$, so $n_1+t$ is *not* coprime to $R$ — not accepted. This contradicts periodicity. Hence $p\mid t$ for every prime $p\mid R$; since $R$ is squarefree, $R\mid t$. Combined with $m\mid t$ and $\gcd(m,R)=1$: $mR\mid t$, so $t\ge mR$. Since $mR$ is itself a period, $T_{\min}=mR$ is exactly minimal. $\blacksquare$

**Proof of the ratio $C(N,m)=d/\varphi(d)$.** Write $N=AB$, $A=\prod_{p\mid N,p\mid m}p^{e_p}$ ($\mathrm{rad}(A)=d$), $B=\prod_{p\mid N,p\nmid m}p^{e_p}$ ($\mathrm{rad}(B)=R$), $\gcd(A,B)=1$. Exponent-blindness gives $\varphi(B)/B=\varphi(R)/R$. Then
$$
C = \frac{\varphi(R)/(mR)}{\varphi(N)/(Nm)} = \frac{N\varphi(R)}{R\varphi(N)} = \frac{AB\varphi(R)}{R\,\varphi(A)\varphi(B)} = \frac{AB\varphi(R)}{R\,\varphi(A)\,(B\varphi(R)/R)} = \frac{A}{\varphi(A)} = \frac{d}{\varphi(d)}.\qquad\blacksquare
$$
Note this proof never used $\gcd(a,d)=1$ — the ratio formula holds throughout the nonzero case regardless of which admissible $a$ (mod the shared primes) is chosen, exactly as the correction factor should be $a$-independent.

## Specializations

- $\gcd(a,m)=1 \Rightarrow \gcd(a,d)=1$ automatically (since $d\mid m$), recovering the previous Theorem 3 as the sub-case where $a$ is required coprime to *all* of $m$, not just the shared part.
- $m\mid N \Rightarrow d=\mathrm{rad}(m)$, giving $C=m/\varphi(m)$ (Theorem 2).
- $m$ unitary in $N$, $N$ squarefree: as before, nesting down to Theorem 1′ and Theorem 1.

## Distinguishing example: $N=5, m=6, a=2$

$\gcd(a,m)=\gcd(2,6)=2\ne1$ — excluded under the old hypothesis. But $d=\mathrm{rad}(\gcd(6,5))=\mathrm{rad}(1)=1$, and $\gcd(a,d)=\gcd(2,1)=1$: admissible under the sharp condition.

$R=\mathrm{rad}(5)=5$ (since $5\nmid6$), $T_{\min}=mR=30$. Direct check, $n\equiv2\pmod6$ in $[1,30]$: $\{2,8,14,20,26\}$. Coprime to $5$: $2$ (yes), $8$ (yes), $14$ (yes), $20$ (no, divisible by 5), $26$ (yes). Count $=4=\varphi(5)$. ✓.

$C(5,6)=d/\varphi(d)=1/\varphi(1)=1$. Naive prediction: $\varphi(5)/5\cdot(30/6)=(4/5)\cdot5=4$. Ratio $4/4=1$. ✓ — and indeed $m/\varphi(m)=6/\varphi(6)=3$ would have been wrong, confirming the weakening is genuine, not cosmetic.

## Zero-count example (for completeness)

$N=6,m=4,a=2$: $d=\mathrm{rad}(\gcd(4,6))=\mathrm{rad}(2)=2$, and $\gcd(a,d)=\gcd(2,2)=2>1$. Prediction: $S(L)=\varnothing$ for all $L$. Check: $n\equiv2\pmod4$ gives $n\in\{2,6,10,14,\dots\}$, all even, hence never coprime to $N=6$ (which is even). Confirmed identically zero.

## The complete hierarchy

$$
d=\mathrm{rad}(\gcd(m,N)),\quad R=\mathrm{rad}(N)/d,\quad T_{\min}=mR,\quad C(N,m)=\frac d{\varphi(d)}\ \ (\text{or }0\text{ if }\gcd(a,d)>1),
$$
reducing each input to exactly the information relevant to the interaction: $N\to\mathrm{rad}(N)$, $m\to$ which primes it shares with $N$, $a\to$ whether it avoids those shared primes.

Theorem 1 (primorial) ⊂ Theorem 1′ (unitary divisor) ⊂ Theorem 2 ($m\mid N$) ⊂ Theorem 3, earlier draft ($\gcd(a,m)=1$) ⊂ **Theorem 3, final** ($\gcd(a,d)=1$, with the complementary zero case). This chain is now closed: every hypothesis in it has been shown either load-bearing (with a distinguishing numerical example) or removable, and no further prime-support information beyond $d$, $R$, and $\mathrm{rad}(N)$ remains to be extracted from $(N,m,a)$.

## Note on document status

All intermediate documents remain in `papers/`. Draft v3.1 of the printed paper remains unchanged. This closed chain, ending at Theorem 3 (final), is the mathematical core proposed for Draft v3.2.
