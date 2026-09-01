# Frozen Specification — General Divisor Theorem (candidate v3.2 core)

Status: FROZEN for adversarial verification. Not to be generalized further until this
specification passes independent computational testing.

## Inputs

- $N \ge 1$ (integer)
- $m \ge 1$ (integer)
- $a \in \mathbb{Z}$ (any integer; only $a \bmod m$ matters)

## Derived quantities

$$
d = \operatorname{rad}\bigl(\gcd(m,N)\bigr), \qquad
R = \frac{\operatorname{rad}(N)}{d}, \qquad
T_{\min} = mR = \operatorname{lcm}\bigl(m,\operatorname{rad}(N)\bigr).
$$

($\operatorname{rad}(k)$ = product of distinct primes dividing $k$, with $\operatorname{rad}(1)=1$.)

## Target set

$$
S(L) = \{\, n \le L : n \equiv a \!\!\pmod m,\ \gcd(n,N)=1 \,\}.
$$

## Claim 1 — Dichotomy on $a$

- If $\gcd(a,d) = 1$: $S(L)$ is governed by Claims 2–4 below.
- If $\gcd(a,d) > 1$: $S(L) = \varnothing$ for every $L \ge 1$.

## Claim 2 — Exact per-period count

For every $n_0$, the count of accepted values in any half-open window of length $T_{\min}$ is
exactly $\varphi(R)$ (constant, independent of the window's starting point, once $\gcd(a,d)=1$).

Equivalently: $|S(qT_{\min})| = q\cdot\varphi(R)$ for every integer $q \ge 0$.

## Claim 3 — Minimality of $T_{\min}$

$T_{\min}$ is the exact minimal positive period of the indicator function
$\mathbb{1}[n \equiv a \pmod m,\ \gcd(n,N)=1]$ — i.e. $T_{\min}$ is itself a period, and no
$0 < t < T_{\min}$ is a period.

## Claim 4 — Correction factor identity

Against the naive independence prediction $\frac{\varphi(N)}{N}\cdot\frac{L}{m}$, the exact
identity (not merely an asymptotic ratio) is:

$$
\varphi(R)\cdot N \cdot \varphi(d) \;=\; \varphi(N)\cdot R \cdot d.
$$

This is equivalent to $C(N,m) := \dfrac{\varphi(R)/(mR)}{\varphi(N)/(Nm)} = \dfrac{d}{\varphi(d)}$,
stated as a cross-multiplied integer equation to avoid floating-point rounding in verification.

## Out of scope for this test (frozen, not re-derived)

Everything above is the object under test. Derivations, motivating examples, and the nested
specializations (Theorem 1, 1′, 2) live in the derivation documents and are not re-proved here —
this file exists only to give the test suite an unambiguous, minimal target.
