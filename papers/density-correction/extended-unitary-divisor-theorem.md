# Extension: Density Correction for Unitary Divisors of Arbitrary N

*Proposed addition to "Density Correction under Residue Conditioning in Primorial Systems," following Section 2.*

## Motivation

Theorem 1 requires $m$ to be a squarefree divisor of $P_k$. But every divisor of $P_k$ is automatically squarefree, since $P_k$ itself is squarefree by construction — so that hypothesis carries no force. The proof of Theorem 1 uses exactly two facts: $\gcd(m, P_k/m) = 1$, and the resulting multiplicativity $\varphi(P_k) = \varphi(m)\varphi(P_k/m)$. Neither fact depends on $P_k$ being squarefree. This lets the theorem extend to arbitrary $N$, provided the coprimality condition on $m$ is imposed directly.

## Definition (Unitary divisor)

For a positive integer $N$, a divisor $m \mid N$ is a **unitary divisor** of $N$ if
$$
\gcd\!\left(m, \frac{N}{m}\right) = 1.
$$

When $N$ is squarefree, every divisor is unitary automatically — this is why the distinction was invisible in the primorial case. For general $N$, unitary divisors are the divisors that absorb the *entire* exponent of each prime they touch: if $N = \prod p_i^{e_i}$, then $m$ is a unitary divisor of $N$ exactly when $m$ is a product of a subset of the full prime-power factors $p_i^{e_i}$.

## Theorem 1′ (Extended form)

Let $N$ be any positive integer, let $m$ be a unitary divisor of $N$ with $m > 1$, and let $a$ be an integer with $\gcd(a, m) = 1$. Write $L = qN + s$, $0 \le s < N$. Then
$$
\bigl|\{n \le L : n \equiv a \!\!\pmod m,\ \gcd(n, N) = 1\}\bigr| = q\,\varphi(N/m) + R(s),
$$
where $R(s)$ is the exact count within the partial final period and satisfies $0 \le R(s) \le \lceil s/m \rceil$.

Against the naive predicted count $\dfrac{\varphi(N)}{N}\cdot\dfrac{L}{m}$, the ratio converges as $L \to \infty$ to
$$
C(m) = \frac{m}{\varphi(m)},
$$
independent of both the choice of admissible $a$ and the choice of $N$ among those having $m$ as a unitary divisor.

**Proof.** Since $\gcd(m, N/m) = 1$, the Chinese Remainder Theorem applies exactly as in Theorem 1: within one period $[1, N]$, exactly $N/m$ integers satisfy $n \equiv a \pmod m$, and as $n$ ranges over that fixed class, its residue modulo $N/m$ ranges uniformly over all residues mod $N/m$. Hence the fraction of these additionally coprime to every prime dividing $N/m$ is $\varphi(N/m)/(N/m)$, giving an exact per-period count of $\varphi(N/m)$.

Since $\gcd(a,m)=1$, these $n$ are already coprime to every prime dividing $m$, so no further restriction from $m$'s primes is needed — this step used only $\gcd(m, N/m)=1$, not squarefreeness of $N$.

By multiplicativity of $\varphi$ over coprime arguments, $\varphi(N) = \varphi(m)\,\varphi(N/m)$, so the same algebraic manipulation as in Theorem 1 gives
$$
C(m) = \frac{\varphi(N)/\varphi(m)}{\varphi(N)/m} = \frac{m}{\varphi(m)}. \qquad \blacksquare
$$

## Worked example: a genuinely non-squarefree $m$

Take $N = 12 = 2^2 \cdot 3$ and $m = 4$. Then $N/m = 3$, and $\gcd(4,3)=1$, so $4$ is a unitary divisor of $12$ — even though $4$ is not squarefree. Theorem 1′ applies where Theorem 1 as originally stated does not, since $4 \nmid P_k$ for any primorial $P_k$.

Admissible $a$: $\gcd(a,4)=1 \Rightarrow a \in \{1,3\} \pmod 4$.

- Exact per-period count: $\varphi(N/m) = \varphi(3) = 2$.
- Naive prediction per period: $\varphi(12)/12 \cdot (12/4) = (4/12)\cdot 3 = 1$.
- $C(4) = 4/\varphi(4) = 4/2 = 2$. Check: $2/1 = 2$. ✓.

## Boundary case: non-unitary $m$

If $m \mid N$ but $\gcd(m, N/m) \ne 1$, the CRT step fails — the residue of $n$ modulo $N/m$ does **not** range uniformly over a full set of residues as $n$ ranges over its class mod $m$, because $m$ and $N/m$ share a factor and the two conditions are no longer independent. Example: $N=12$, $m=2$, $N/m=6$, $\gcd(2,6)=2\ne 1$.

This case is explicitly **outside** the scope of Theorem 1′. Following the paper's own discipline in Section 3 — a shared label (both are "divisors of $N$ with a residue condition") does not entail a shared specification — this boundary should be stated rather than left implicit. No claim is made here about what ratio (if any) governs the non-unitary case; that is a separate question requiring separate proof.

## Relation to Theorem 1

Theorem 1 is the special case $N = P_k$: since $P_k$ is squarefree, *every* divisor $m$ of $P_k$ satisfies $\gcd(m, P_k/m)=1$ automatically, so the "unitary" qualifier is vacuous and can be dropped — recovering the original statement exactly. Theorem 1′ is the strictly more general statement; Corollaries 1 and 2 carry over unchanged as the case $N=P_k$.
