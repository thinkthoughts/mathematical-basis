# The General Divisor Theorem: Exact Density Correction under Residue Conditioning

thinkthoughts
https://github.com/thinkthoughts/mathematical-basis

**Draft v3.2** — extends Draft v3.1 (preserved unchanged as `paper-v3.1.pdf`); see the Change Log
at the end of this document for a full record of changes.

## Abstract

Let $N,m$ be positive integers and $a$ an integer. Write
$$
d=\operatorname{rad}(\gcd(m,N)),
\qquad
R=\frac{\operatorname{rad}(N)}{d}.
$$
For
$$
S(N,L,m,a)
=
\{1\le n\le L:n\equiv a\pmod m,\ \gcd(n,N)=1\},
$$
we prove an exact dichotomy. If $\gcd(a,d)=1$, the associated indicator has exact minimal period
$$
T_{\min}=mR=\operatorname{lcm}(m,\operatorname{rad}(N)),
$$
with exactly $\varphi(R)$ accepted values per period. Relative to the naive independent-density prediction
$$
\frac{\varphi(N)}{N}\frac{L}{m},
$$
the exact correction factor is
$$
C(N,m)=\frac{d}{\varphi(d)},
$$
independent of the admissible residue $a$. If $\gcd(a,d)>1$, the accepted set is empty for every $L$. These period, count, and correction formulas are exact, rather than asymptotic, and require no divisibility or squarefreeness restriction on $N$ or $m$.

The theorem recovers the motivating primorial result when $N=P_k$ and $m\mid P_k$: squarefreeness gives $d=m$, $R=P_k/m$, $T_{\min}=P_k$, and $C(N,m)=m/\varphi(m)$. We also examine a separate weighted-vector construction as a worked example distinguishing a shared label, a shared reading, and a shared specification.

## 1. Introduction / General Setup

Let $N$ and $m$ be positive integers and $a$ an integer. We study the counting problem
$$
S(N,L,m,a) = \{1\le n\le L : n\equiv a\pmod m,\ \gcd(n,N)=1\},
$$
the integers up to $L$ lying in a fixed residue class modulo $m$ and coprime to $N$.

A naive density heuristic treats the residue condition and the coprimality condition as
independent: density $1/m$ from the residue class, multiplied by $\varphi(N)/N$ from coprimality
to $N$. This gives the naive prediction
$$
|S(N,L,m,a)| \approx \frac{\varphi(N)}{N}\frac{L}{m}.
$$

This double-counts a restriction whenever $m$ and $N$ share a prime factor. If a prime $p$ divides
both $m$ and $N$, and $n\equiv a\pmod m$ with $\gcd(a,p)=1$, then $n$ is already guaranteed
coprime to $p$ by the residue condition alone — the factor $\varphi(N)/N$ re-imposes that
restriction a second time. The primes doing this double duty are exactly the primes shared between
$m$ and $N$; primes of $N$ not dividing $m$, and primes of $m$ not dividing $N$, play no special
role in this double-counting.

This motivates isolating the shared-prime structure directly, via
$$
d=\operatorname{rad}(\gcd(m,N)), \qquad R=\frac{\operatorname{rad}(N)}{d},
$$
the radical of the primes $m$ and $N$ have in common, and the radical formed from the primes of
$N$ not shared with $m$. Section 2 states and proves the exact correction this produces. Section 3 walks
through its specializations, recovering progressively more restrictive — and historically earlier
— versions of the same result, down to the primorial case that originally motivated this work.

## 2. The General Divisor Theorem

### 2.1 A lemma used throughout

**Lemma** (exponent-blindness). For every integer $k\ge1$,
$$
\frac{k}{\varphi(k)} = \frac{\operatorname{rad}(k)}{\varphi(\operatorname{rad}(k))},
$$
where $\operatorname{rad}(k)$ is the product of the distinct primes dividing $k$
($\operatorname{rad}(1)=1$).

**Proof.** For $k=1$ both sides equal $1$. For $k>1$, write $k=\prod_i p_i^{e_i}$. For each prime
power, $\varphi(p_i^{e_i})/p_i^{e_i}=1-1/p_i$, independent of $e_i$. By multiplicativity,
$$
\frac{k}{\varphi(k)} = \prod_i\frac{1}{1-1/p_i} = \prod_{p\mid k}\frac{p}{p-1},
$$
which depends only on the set of primes dividing $k$ — i.e. only on $\operatorname{rad}(k)$.
Applying the identical computation to $\operatorname{rad}(k)$ (all exponents $1$) gives the same
product. $\blacksquare$

### 2.2 Theorem 3 (General Divisor Theorem)

Let $N,m$ be any positive integers, $a$ any integer. Define
$$
d = \operatorname{rad}(\gcd(m,N)), \qquad R = \frac{\operatorname{rad}(N)}{d}.
$$
Let $S(L)=\{1\le n\le L : n\equiv a\pmod m,\ \gcd(n,N)=1\}$.

**Case $\gcd(a,d)=1$.** Writing $L=qT_{\min}+s$, $0\le s<T_{\min}$,
$$
|S(L)| = q\,\varphi(R) + R_{\mathrm{rem}}(s), \qquad T_{\min} = mR = \operatorname{lcm}(m,\operatorname{rad}(N)),
$$
$T_{\min}$ is the exact minimal period of the indicator $\mathbb1[n\equiv a\pmod m,\ \gcd(n,N)=1]$,
and against the naive predicted count $\frac{\varphi(N)}{N}\frac{L}{m}$,
$$
C(N,m) = \frac{d}{\varphi(d)} = \prod_{p\mid\gcd(m,N)}\frac{p}{p-1}.
$$

**Case $\gcd(a,d)>1$.** Then $S(L)=\varnothing$ for every $L$.

**Proof.**

*Dichotomy and exact count.* Fix $n\equiv a\pmod m$. For each prime $p\mid d$: since $p\mid m$,
$n\equiv a\pmod p$, so $n$ is coprime to $p$ iff $a$ is. If $\gcd(a,d)=1$, every such $n$ is
coprime to all of $d$; if some $p\mid d$ divides $a$, then $p$ divides every $n$ in the class, and
since $p\mid d\mid N$, no such $n$ is coprime to $N$ — giving $S(L)=\varnothing$ for every $L$.
Assume now $\gcd(a,d)=1$: then $\gcd(n,N)=1 \iff \gcd(n,R)=1$ (the only primes of $N$ left to
check are $R$'s). Since $\gcd(m,R)=1$, any interval of $mR$ consecutive integers is a complete
residue system mod $mR$; among such an interval, the sub-collection with $n\equiv a\pmod m$
numbers exactly $R$ elements and bijects with $\mathbb Z/R\mathbb Z$ via $n\bmod R$ (CRT), of which
exactly $\varphi(R)$ are coprime to $R$. This holds for every such window, giving the exact count
$\varphi(R)$ per length-$T_{\min}$ window and, summing over $q$ disjoint windows,
$|S(qT_{\min})|=q\varphi(R)$.

*$T_{\min}$ is a period.* For $n\equiv a\pmod m$, $\gcd(n,N)=1\iff\gcd(n,R)=1$ as above; for
$n\not\equiv a\pmod m$, $n$ is unaccepted regardless. So the indicator factors as
$I(n)=\mathbb1[n\equiv a\pmod m]\cdot\mathbb1[\gcd(n,R)=1]$ for all $n$. The first factor has
period $m$ (depends only on $n\bmod m$); the second has period $R$ (coprimality to $R$ depends
only on $n\bmod R$, since $R$ is squarefree). Since $m\mid mR$ and $R\mid mR$, both factors, and
hence their product, are unchanged under $n\mapsto n+mR$: $T_{\min}=mR$ is a period.

*No smaller $t$ is a period.* By CRT (using $\gcd(m,R)=1$) pick $n_0\equiv a\pmod m$,
$n_0\equiv1\pmod R$; $n_0$ is accepted. If $t>0$ is any period, $n_0+t$ is accepted, so
$n_0+t\equiv a\pmod m$, giving $m\mid t$. Fix a prime $p\mid R$ and suppose $p\nmid t$; by CRT
choose $n_1\equiv a\pmod m$, $n_1\equiv-t\pmod p$, $n_1\equiv1\pmod q$ for every other prime
$q\mid R$. Then $n_1$ is accepted but $n_1+t\equiv0\pmod p$ is not — contradicting periodicity.
Hence $p\mid t$ for every prime $p\mid R$; since $R$ is squarefree, $R\mid t$, and with $m\mid t$,
$\gcd(m,R)=1$: $mR\mid t$. Thus $mR\mid t$ for every positive period $t$. Since $mR$ itself is a
period, it is the exact minimal positive period: $T_{\min}=mR$.

*Ratio.* Write $N=AB$, $A=\prod_{p\mid N,p\mid m}p^{e_p}$ ($\operatorname{rad}(A)=d$),
$B=\prod_{p\mid N,p\nmid m}p^{e_p}$ ($\operatorname{rad}(B)=R$), $\gcd(A,B)=1$, so
$\varphi(N)=\varphi(A)\varphi(B)$. By the Lemma (applied to $k=B$), $\varphi(B)/B=\varphi(R)/R$.
Then
$$
C = \frac{\varphi(R)/(mR)}{\varphi(N)/(Nm)} = \frac{N\varphi(R)}{R\varphi(N)} = \frac{AB\varphi(R)}{R\varphi(A)\varphi(B)} = \frac{AB\varphi(R)}{R\varphi(A)(B\varphi(R)/R)} = \frac{A}{\varphi(A)}.
$$
By the Lemma once more (applied to $k=A$), $A/\varphi(A)=d/\varphi(d)$, giving $C=d/\varphi(d)$.
$\blacksquare$

## 3. Specializations and Distinguishing Examples

Having proved Theorem 3 in full generality, we now walk down its specializations, each obtained by
substituting a stronger hypothesis on $(N,m,a)$ directly into $d$, $R$, $T_{\min}$, and $C(N,m)$ —
no independent re-derivation is required at any stage:
$$
\text{Theorem 3} \;\longrightarrow\; \text{Theorem 2} \;\longrightarrow\; \text{Theorem }1' \;\longrightarrow\; \text{Theorem 1},
$$
where each arrow denotes "specializes to": the target theorem imposes stronger hypotheses, and its
period, count, and correction-factor formulas are recovered from the source theorem by direct
substitution, not by an independent proof.

### 3.1 Theorem 2 (specialization: $m\mid N$)

If $m\mid N$, then $\gcd(m,N)=m$, so $d=\operatorname{rad}(m)$ directly. Substituting into Theorem
3:
$$
R = \frac{\operatorname{rad}(N)}{\operatorname{rad}(m)}, \qquad T_{\min} = m\,\frac{\operatorname{rad}(N)}{\operatorname{rad}(m)}, \qquad C(N,m) = \frac{\operatorname{rad}(m)}{\varphi(\operatorname{rad}(m))} = \frac{m}{\varphi(m)}
$$
(the last equality by the Lemma applied to $k=m$), with admissibility $\gcd(a,\operatorname{rad}(m))=1$
and the same complementary zero branch. No new argument is required beyond this substitution;
minimality, the exact count $\varphi(R)$, and the ratio are all inherited directly from Theorem 3.

### 3.2 Theorem 1′ (specialization: $m$ unitary in $N$)

Call $m$ a *unitary divisor* of $N$ if $\gcd(m,N/m)=1$ — equivalently, $m$ absorbs the full
exponent of each of its primes in $N$. Under this hypothesis (a strengthening of $m\mid N$), write
$N'=N/m$. Then $\operatorname{rad}(N)=\operatorname{rad}(m)\operatorname{rad}(N')$ (coprime
factors), so $R=\operatorname{rad}(N)/\operatorname{rad}(m)=\operatorname{rad}(N')$ and
$$
T_{\min} = m\operatorname{rad}(N'), \qquad C(N,m)=\frac{m}{\varphi(m)},
$$
as in Theorem 2. The interval $N=mN'$ is also a period of the indicator (it is an integer multiple
of $T_{\min}$, since $N'/\operatorname{rad}(N')$ is an integer), with total count $\varphi(N')$
over that longer interval — this matches Theorem 3's prediction exactly (using exponent-blindness
to check $\varphi(N')/N'=\varphi(\operatorname{rad}(N'))/\operatorname{rad}(N')$), but **$N$ is
generally not the minimal period**: it equals $T_{\min}$ only when $N'$ is itself squarefree.

### 3.3 Two distinguishing examples

**$N=18,\ m=2$ — coarser vs. minimal period.** Here $m=2$ is a unitary divisor of $N=18=2\cdot3^2$
($\gcd(2,9)=1$), so Theorem 1′ applies and gives a valid period of $N=18$ with count
$\varphi(9)=6$. But $\operatorname{rad}(N')=\operatorname{rad}(9)=3$, so Theorem 3's exact minimal
period is
$$
T_{\min} = m\operatorname{rad}(N') = 2\cdot3 = 6.
$$
Direct enumeration confirms this: taking $a=1$, $n\equiv1\pmod2$ and $\gcd(n,18)=1$ (odd and not
divisible by $3$) gives $\{1,5,7,11,13,17,\dots\}$ in $[1,18]$, i.e. $\{1,5,7,11,13,17\}$ — a
pattern that visibly repeats every $6$ integers, not every $18$. So $18$ is a genuine period (as
Theorem 1′ correctly states) but not the minimal one; $6$ is.

**$N=5,\ m=6,\ a=2$ — the sharp admissibility condition.** Here $\gcd(a,m)=\gcd(2,6)=2\ne1$, so
this case would be *excluded* under Theorem 1's or Theorem 1′'s hypothesis $\gcd(a,m)=1$. But
$d=\operatorname{rad}(\gcd(6,5))=\operatorname{rad}(1)=1$, and $\gcd(a,d)=\gcd(2,1)=1$: admissible
under Theorem 3's sharp condition. Here $R=\operatorname{rad}(5)=5$ (since $5\nmid6$),
$T_{\min}=mR=30$. Direct check, $n\equiv2\pmod6$ in $[1,30]$: $\{2,8,14,20,26\}$; coprime to $5$:
$\{2,8,14,26\}$ — count $4=\varphi(5)$, matching the theorem. And $C(5,6)=d/\varphi(d)=1$, matching the naive prediction exactly
($\varphi(5)/5\cdot(30/6)=4$) — whereas $m/\varphi(m)=6/\varphi(6)=3$ would have been wrong. This
confirms that $\gcd(a,d)=1$ is the exact admissibility condition, not merely a cosmetic restatement
of $\gcd(a,m)=1$: it is strictly weaker in general, admitting strictly more values of $a$, since
$d$ contains only the primes shared between $m$ and $N$.

### 3.4 Theorem 1 (specialization: primorial $N$)

Let $P_k = p_1p_2\cdots p_k$ denote the $k$-th primorial, the product of the first $k$ primes
($p_1=2,p_2=3,\dots$). By construction $P_k$ is squarefree. Let $m$ be a squarefree divisor of
$P_k$ with $m>1$, and let $a$ be an integer with $\gcd(a,m)=1$.

If, in addition to $m\mid N$, $N$ is squarefree ($N=P_k$), then every divisor of $N$ — including
$m$ — is automatically unitary, so Theorem 1′ applies with $N'=P_k/m$; and since $P_k$ is
squarefree, $N'=P_k/m$ is squarefree too (a divisor of a squarefree number is squarefree), so
$\operatorname{rad}(N')=N'$ and the coarser and minimal periods of Section 3.2 coincide exactly:
$$
T_{\min}=m\operatorname{rad}(N')=mN'=P_k.
$$
Because $P_k$ is squarefree, $\operatorname{rad}(m)=m$, so $d=\operatorname{rad}(\gcd(m,P_k))=\operatorname{rad}(m)=m$
exactly — the sharp admissibility condition $\gcd(a,d)=1$ used in Theorem 3 is, in this primorial
setting, *identical* to the hypothesis $\gcd(a,m)=1$ above. This is the same pattern already seen
in Theorem 2 ($d=\operatorname{rad}(m)$ whenever $m\mid N$); it collapses to an equality here
specifically because $m$ is squarefree.

This gives:

**Theorem 1** (primorial specialization). Let $P_k$, $m$, and $a$ be as above. Write
$$
L = qP_k + s,\qquad 0\le s<P_k.
$$
Then
$$
|S(P_k,L,m,a)| = q\,\varphi(P_k/m) + R(s),
$$
where
$$
R(s) = \bigl|\{1\le n\le s : n\equiv a\pmod m,\ \gcd(n,P_k)=1\}\bigr|
$$
is the exact count within the partial final period and satisfies $0\le R(s)\le\lceil s/m\rceil$,
with minimal period $P_k$ and correction factor
$$
C(m) = \frac{m}{\varphi(m)},
$$
independent of the admissible residue $a$. This is exactly Theorem 3 specialized as above, with no
adjustment to period, count, or correction factor required.

#### Independent primorial proof

The following is the original proof of Theorem 1, self-contained and independent of Theorem 3,
retained here as the paper's historical starting point.

**Proof.** Since $m\mid P_k$ and $P_k$ is squarefree, $m$ and $P_k/m$ are coprime and squarefree,
and $P_k/m$ consists exactly of the prime factors of $P_k$ that do not divide $m$.

Within one period $[1,P_k]$, exactly $P_k/m$ integers satisfy $n\equiv a\pmod m$. By the Chinese
Remainder Theorem, because $m$ and $P_k/m$ are coprime, the residue of $n$ modulo $P_k/m$ ranges
uniformly over all residue classes as $n$ ranges over its fixed class modulo $m$ within one period.

Hence exactly the fraction
$$
\prod_{p\mid P_k/m}\Bigl(1-\frac1p\Bigr) = \frac{\varphi(P_k/m)}{P_k/m}
$$
of these $P_k/m$ values are additionally coprime to every prime dividing $P_k/m$. Since
$\gcd(a,m)=1$, they are already coprime to every prime dividing $m$. Therefore the exact count per
period is
$$
\frac{P_k}{m}\cdot\frac{\varphi(P_k/m)}{P_k/m} = \varphi(P_k/m).
$$

The count does not depend on the specific value of $a$ beyond $\gcd(a,m)=1$, because the argument
uses only that the residue class modulo $m$ is fixed and coprime to $m$.

Using multiplicativity of Euler's totient function, $\varphi(P_k)=\varphi(m)\varphi(P_k/m)$, so
$\varphi(P_k/m)=\varphi(P_k)/\varphi(m)$. The naive predicted count per period is
$\varphi(P_k)/m$. The ratio is therefore
$$
\frac{\varphi(P_k)/\varphi(m)}{\varphi(P_k)/m} = \frac{m}{\varphi(m)} = C(m).
$$
This ratio is exact per full period and independent of $k$. Periodicity with period $P_k$ gives
the general-$L$ statement with the bounded remainder above. $\blacksquare$

#### Standardized refined-density identity

Throughout this paper, the refined predicted count is written in the equivalent forms
$$
E_{\mathrm{refined}}(L) = \frac{L}{m}\prod_{p\mid P_k/m}\Bigl(1-\frac1p\Bigr) = L\,\frac{\varphi(P_k/m)}{P_k}.
$$
These are equal because $\frac{L}{m}\cdot\frac{\varphi(P_k/m)}{P_k/m} = L\,\frac{\varphi(P_k/m)}{P_k}$.

**Corollary 1** ($m=6$ case). For $m=6$ and $a\in\{1,5\}$,
$$
C(6) = \frac{6}{\varphi(6)} = \frac62 = 3.
$$
This corrects the earlier draft's reported limiting constant $24/25$ for the case $a=5$.

Against the refined predicted count $E_{\mathrm{refined}}(L)=L\varphi(P_k/6)/P_k$, the ratio is
exactly $1$.

*(In Section 2's general notation, $C(6)=6/\varphi(6)=d/\varphi(d)$ with $d=6$, since $6$ is
already squarefree — the two notations agree exactly, as they must by the remark above.)*

**Corollary 2** (Combined residue classes). Since the per-period count $\varphi(P_k/m)$ is
independent of which admissible $a$ is used, the same ratio $C(m)$ holds for any union of
admissible residue classes modulo $m$. For example, the classes $n\equiv1$ or $5\pmod6$ together
give the same ratio $3$ as either class individually, because both the exact and naive counts
scale by the same number of residue classes.

Both corollaries were verified numerically at $P_k=210$ for $m\in\{6,10,30\}$, multiple values of
$a$, and $L$ up to $10^7$, matching the predicted $C(m)$ to five decimal places or better in every
case and matching the exact per-period counts $\varphi(P_k/m)$ precisely; see
`tests/basis/test_persistent_constant.py`.

## 4. A Failed Correspondence as a Reading-Point Example

An earlier draft defined a weighted tuple $(9,4,2,3)$ with angles $\theta_k\in\{0°,60°,120°,180°\}$
and
$$
V = \sum_{k=1}^4 w_k e^{i\theta_k} = 9 + 4e^{i\pi/3} + 2e^{i2\pi/3} + 3e^{i\pi} = 7 + 3\sqrt3\,i.
$$
The reported reading was $r_V = \arg(V) \approx 36.586776°$.

The same draft separately noted that the point $(1,1)$ has reading $r_D=\arg(1+i)=45°$, and
described the combination as a "9423 phase-lock representation," implying a correspondence between
the two constructions.

Since $r_V\ne r_D$, no such correspondence holds under the stated construction.

An exhaustive search over all $24$ permutations of assigning the four weights to the four fixed
angles confirms that this discrepancy is not an artifact of ordering: no permutation reaches
exactly $45°$, with the closest approaches at $43.898°$ and $46.102°$
(`tests/basis/test_9423_phase_lock.py`).

This gives the three-level distinction
$$
\text{shared label} \not\Rightarrow \text{shared reading} \not\Rightarrow \text{shared specification.}
$$

The draft's own label, "9423 phase-lock representation," was shared across both objects by
assertion, but the named readings are not shared: $r_V=36.586776° \ne 45° = r_D$.

The second implication is worth stating independently. Even had $r_V=r_D$ exactly, that equality
alone would not establish a structural correspondence between $V$'s construction and the point
$(1,1)$. No transformation, projection, or limiting operation connecting the two objects would
thereby be specified.

A shared label asserts a correspondence. A shared reading is, at most, evidence that two objects
were run through procedures producing the same observable category. Neither, on its own, specifies
the correspondence itself.

Section 3 gives a cleaner instance of the same principle. The reported ratio for $m=6,a=5$ has
taken three different numerical values during the paper's development: $24/25$ (originally
reported, against no explicitly stated refined predicted count), $3$ (against the naive predicted
count $(\varphi(P_k)/P_k)(L/6)$), and $1$ (against the refined predicted count
$L\varphi(P_k/6)/P_k$). None of
these numbers is meaningful without specifying which predictor produced it. The number alone is
insufficient; the reading requires its producing specification to be stated alongside it.

## 5. Numerical Verification

At $P_k=210=2\cdot3\cdot5\cdot7$, $m=6$, $a=5$, the numerical results are:

**Table 1: Numerical verification at $P_k=210$, $m=6$, $a=5$.**

| $L$ | actual | naive predicted | naive ratio | refined predicted | refined ratio |
|---|---|---|---|---|---|
| $10^5$ | 11,428 | 3,809.52 | 2.99985 | 11,428.57 | 0.99995 |
| $10^6$ | 114,285 | 38,095.24 | 2.99998 | 114,285.71 | 0.99999 |
| $10^7$ | 1,142,856 | 380,952.38 | 3.00000 | 1,142,857.14 | 1.00000 |
| $10^8$ | 11,428,571 | 3,809,523.81 | 3.00000 | 11,428,571.43 | 1.00000 |

Additional verification across $m\in\{6,10,30\}$ and all admissible $a\bmod m$ confirms
$C(m)=m/\varphi(m)$ exactly: $C(6)=3$, $C(10)=2.5$, $C(30)=3.75$. It also confirms the exact
per-period count $\varphi(P_k/m)$, independently of $a$, at $P_k=210$ and $L$ up to $10^7$; see
`tests/basis/test_persistent_constant.py`.

*(These values also follow directly from Section 2's general formulas: e.g.
$C(10)=10/\varphi(10)=2.5$ and $C(30)=30/\varphi(30)=3.75$ reproduce exactly.)*

## 6. Conclusion

The General Divisor Theorem (Theorem 3) gives an exact, elementary correction to the naive
independent-density heuristic for counting integers in a fixed residue class that are also
coprime to a modulus — for arbitrary positive integers $N,m$ and any integer $a$, with no
divisibility or squarefreeness restriction on either. Writing $d=\operatorname{rad}(\gcd(m,N))$
for the primes $m$ and $N$ share, and $R=\operatorname{rad}(N)/d$ for what remains, the indicator
has exact minimal period $T_{\min}=\operatorname{lcm}(m,\operatorname{rad}(N))$, with exactly
$\varphi(R)$ accepted values per period, whenever $\gcd(a,d)=1$; the correction factor against the
naive prediction is then exactly
$$
C(N,m) = \frac{d}{\varphi(d)},
$$
independent of which admissible $a$ is chosen. If instead $\gcd(a,d)>1$, the accepted set is
identically empty for every $L$ — a genuine dichotomy, not an edge case. The theorem follows from
the Chinese Remainder Theorem and multiplicativity of $\varphi$, requiring no sieve-theoretic or
analytic machinery, and its proof was independently audited and confirmed against exhaustive
bounded computational tests, including the minimal-period claim; verification artifacts — along
with the audit history — are available in the repository (Appendix A).

The primorial case that motivated this work is recovered exactly as one specialization: for
$N=P_k$ squarefree and $m$ a squarefree divisor of $P_k$, squarefreeness forces $d=m$, giving
$$
C(m) = \frac{m}{\varphi(m)}.
$$
The primorial theorem is recovered without modification to its period, count, or correction
factor. In its development, the $m=6$ case also corrected an earlier reported constant $24/25$ to
$C(6)=3$; against the refined predicted count, the ratio is exactly $1$.

Section 4 gives a separate worked example of why a reading should be stated together with its
producing specification. A weighted-vector construction labeled as corresponding to a $45°$
diagonal direction yields a different reading under the stated construction. Together with the
density-correction example, this distinguishes a shared label, a shared reading, and a shared
specification.

## Appendix A. Verification Code

```python
from math import gcd
from sympy import totient, primefactors

def naive_predicted(limit, primorial, m):
    density = totient(primorial) / primorial
    return density * (limit / m)

def count_residue(limit, primorial, m, a):
    c = 0
    n = a
    while n <= 0:
        n += m
    for n in range(n, limit + 1, m):
        if gcd(n, primorial) == 1:
            c += 1
    return c

def refined_predicted(limit, primorial, m):
    # density = product over primes dividing Pk but NOT dividing m
    m_primes = set(primefactors(m))
    dens = 1.0
    for p in primefactors(primorial):
        if p not in m_primes:
            dens *= (1 - 1.0 / p)
    return dens * (limit / m)
```

Full runnable versions, including the general $(m,a)$ sweep and the permutation search for Section
4, are in `tests/basis/test_persistent_constant.py` and `tests/basis/test_9423_phase_lock.py`.

*(Added in v3.2.)* The corresponding exhaustive verification for the general theorem of Section 2
— covering arbitrary $(N,m,a)$, both branches of the dichotomy, arbitrary-window invariance, and
divisor-based exact minimal-period detection over more than $4.7\times10^6$ checks, with zero
counterexamples found — is in `test_general_divisor_theorem.py`, with results recorded in
`verification-results.md`. The proof itself was independently audited line by line against a
frozen specification (`theorem-specification.md`); a first pass (`proof-audit.md`) found two
genuine gaps — an unproved arbitrary-window generalization and an unproved minimality premise —
which were then closed and confirmed by a second, independent pass (`proof-audit-repaired.md`).
Neither gap affected the primorial case (Section 3.4), which was independently reconfirmed as an
exact specialization in `specialization-audit-repaired.md`.

## Appendix B. References

[1] G. H. Hardy and E. M. Wright, *An Introduction to the Theory of Numbers*, Oxford University
Press. Relevant background: the Chinese Remainder Theorem, Euler's totient function, and
multiplicativity of $\varphi$.

## Appendix C. Project Vocabulary

The notation in this appendix is project-specific and is not part of Theorem 1. The theorem itself
remains legible and valid independently of this vocabulary.

**Pi — expand.** $m \mapsto \mathbb Z/m\mathbb Z$. This exposes the complete residue/state space
for a given modulus before any restriction is imposed.

**$\pi$ — extend.** $P_k \mapsto P_{k+1}=p_{k+1}P_k$. This adds another specification/constraint
by extending the primorial by one further prime.

**$\Pi$ — resist.** $\prod_{p\mid P_k/m}(1-1/p)$. This is the fraction of candidates remaining
admissible under the divisibility constraints not already imposed by the residue condition; it is
the quantity appearing directly in the proof of Theorem 1.

These roles give the progression
$$
\text{Pi (expand)} \to \pi\text{ (extend)} \to \Pi\text{ (resist)} \to r\text{ (read)}.
$$
These names label roles already present in the proof of Theorem 1. The proof itself does not
depend on this vocabulary and holds independently of it.

*(Added in v3.2.)* This vocabulary describes Theorem 1's proof specifically. The "extend" step
($P_k\to P_{k+1}$) does not have a natural analog in Theorem 3: the general theorem's $N$ has no
canonical "next $N$" the way the primorial sequence does, so this vocabulary should not be read as
describing the general theorem of Section 2.

---

## Change Log (v3.1 → v3.2)

Keyed to `v3.2-integration-audit.md`. Rows below list only sections where content changed;
sections not listed are byte-for-byte identical to Draft v3.1 (modulo renumbering).

| v3.1 location | Change made | Audit classification |
|---|---|---|
| Abstract | Added paragraph on the general theorem and its recovery of Theorem 1 | NEW MATERIAL |
| Section 1 | Added remark: $d=m$ in the primorial setting, so $\gcd(a,d)=1\iff\gcd(a,m)=1$ | WORDING |
| Section 2, after Theorem 1's proof | Added remark pointing to Section 3 and explaining why no minimal-period subtlety arises here | NEW MATERIAL |
| Section 2, Corollary 1 | Added parenthetical connecting $C(6)=m/\varphi(m)$ to $d/\varphi(d)$ notation | WORDING |
| Section 2, Corollary 2 | Unchanged | NO CHANGE |
| **New Section 3** | Full new section: Lemma, Theorem 3, Theorem 2, Theorem 1′, two worked examples, recovery of Theorem 1 | NEW MATERIAL (largest item) |
| Old Section 3 → new Section 4 | Renumbered only; text unchanged | NO CHANGE |
| Old Section 4 → new Section 5, Table 1 | Renumbered; values unchanged; rechecked against Section 3 formulas, no discrepancy, added confirmation parenthetical | RECHECK NUMBERS → NO CHANGE |
| Old Section 4 → new Section 5, $C(6),C(10),C(30)$ | Renumbered; values unchanged; rechecked, no discrepancy | RECHECK NUMBERS → NO CHANGE |
| Old Section 5 → new Section 6 (Conclusion) | Extended with paragraph on the general theorem, its audit status, and exact recovery of Theorem 1 | NEW MATERIAL |
| Appendix A | Added pointer to `test_general_divisor_theorem.py` | NEW MATERIAL (pointer only) |
| Appendix B | Unchanged | NO CHANGE |
| Appendix C | Added scope-limiting sentence about the "extend" step | WORDING |

No row involved a `MATHEMATICAL UPDATE` — consistent with the integration audit's finding that no
existing claim in Draft v3.1 required correction.

**Note (result-order restructuring):** this Change Log documents the v3.1→v3.2 *content* changes
only, as it did before the result-order restructuring. It describes the section numbers and
positions that existed at the time those changes were made (discovery order); it has been left
unedited, per instruction, rather than updated to reflect the current physical section numbers.
For the record of the subsequent reordering pass itself (moved blocks, rewritten bridges, deleted
redundancies, and the full cross-reference audit), see `v3.2-result-order-audit.md`.
