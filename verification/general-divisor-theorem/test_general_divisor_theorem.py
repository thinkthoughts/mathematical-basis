"""
Independent verification of the FROZEN General Divisor Theorem spec
(theorem-specification.md). Revision 2: Section E is now exhaustive
(divisor-based minimal-period detection, not a curated O(T^2) sweep),
Claim 2 is tested over arbitrary starting windows (not just [1,T] and
[1,2T]), and Section C's exact identity is checked for d=1 as well as
d>1. This test deliberately re-derives every quantity from first
principles (trial-division primefactors, elementary totient,
brute-force enumeration) rather than importing anything from the
paper's own code.

Sections:
  A. Exact count over EVERY starting window of length T_min (Claim 2),
     exhaustive over the full nonzero-branch grid, via prefix sums
     (avoids O(T^2)).
  B. Zero-branch check (Claim 1, gcd(a,d)>1), exhaustive over the grid.
  C. Correction-factor exact integer identity (Claim 4), exhaustive
     over the FULL grid including d=1.
  D. End-to-end formula vs brute force at unaligned L (sanity), exhaustive.
  E. Minimality of T_min (Claim 3), now EXHAUSTIVE over the full
     nonzero-branch grid via divisors of T_min (minimal period of a
     periodic sequence always divides any known period, so only
     divisors of T_min need testing -- no O(T^2) sweep required).
  F. Explicit boundary/base cases, distinguishing examples, and the
     (6,4,2) zero-branch case reported separately (not counted as a
     completed minimality test).

Any failure is reported, not patched around.
"""

import math

# ---------- independent elementary number theory ----------

def primefactors(n):
    n = abs(n)
    if n <= 1:
        return set()
    fs = set()
    d = 2
    while d * d <= n:
        while n % d == 0:
            fs.add(d)
            n //= d
        d += 1
    if n > 1:
        fs.add(n)
    return fs

def radical(n):
    r = 1
    for p in primefactors(n):
        r *= p
    return r

def euler_phi(n):
    if n <= 0:
        raise ValueError("phi undefined for n<=0")
    if n == 1:
        return 1
    result = n
    for p in primefactors(n):
        result = result // p * (p - 1)
    return result

def gcd(x, y):
    return math.gcd(x, y)

def divisors(n):
    divs = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            divs.append(i)
            if i != n // i:
                divs.append(n // i)
        i += 1
    return sorted(divs)

# ---------- direct enumeration ----------

def accepted(n, m, a, N):
    return (n % m == a % m) and (gcd(n, N) == 1)

def brute_count(L, m, a, N):
    if L <= 0:
        return 0
    c = 0
    for n in range(1, L + 1):
        if accepted(n, m, a, N):
            c += 1
    return c

def derived(N, m):
    d = radical(gcd(m, N))
    R = radical(N) // d
    T = m * R
    return d, R, T

def predicted_count(L, m, a, N):
    d, R, T = derived(N, m)
    if gcd(a, d) > 1:
        return 0
    q, s = divmod(L, T)
    rem = brute_count(s, m, a, N)
    return q * euler_phi(R) + rem

# ============================== TEST SECTIONS ==============================

failures = []

def check(name, cond, detail=""):
    if not cond:
        failures.append(f"{name}: {detail}")

N_RANGE = range(1, 61)
M_RANGE = range(1, 25)

# ---- A. Exact count over EVERY starting window of length T_min (Claim 2) ----
countA_cases = 0
countA_windows = 0
for N in N_RANGE:
    for m in M_RANGE:
        d, R, T = derived(N, m)
        phiR = euler_phi(R)
        for a in range(0, m):
            if gcd(a, d) != 1:
                continue
            countA_cases += 1
            # extended block of length 2T, prefix sums -> every window of
            # length T starting at offset k=0..T-1 in O(1) after O(T) build
            ext = [1 if accepted(n, m, a, N) else 0 for n in range(1, 2 * T + 1)]
            prefix = [0] * (2 * T + 1)
            for i in range(2 * T):
                prefix[i + 1] = prefix[i] + ext[i]
            for k in range(T):
                cnt = prefix[k + T] - prefix[k]
                countA_windows += 1
                if cnt != phiR:
                    failures.append(
                        f"A window N={N} m={m} a={a} start_offset={k}: "
                        f"count={cnt} phi(R)={phiR}"
                    )

# ---- B. Zero branch (Claim 1, gcd(a,d)>1), exhaustive ----
countB = 0
for N in N_RANGE:
    for m in M_RANGE:
        d, R, T = derived(N, m)
        if d == 1:
            continue
        for a in range(0, m):
            if gcd(a, d) > 1:
                countB += 1
                L_test = max(5 * T, 5 * N, 50)
                bf = brute_count(L_test, m, a, N)
                check(
                    f"B zero-branch N={N} m={m} a={a}",
                    bf == 0,
                    f"expected 0, got {bf} over L={L_test}",
                )

# ---- C. Exact integer identity (Claim 4), FULL grid including d=1 ----
countC = 0
for N in N_RANGE:
    for m in M_RANGE:
        d, R, T = derived(N, m)
        countC += 1
        lhs = euler_phi(R) * N * euler_phi(d)
        rhs = euler_phi(N) * R * d
        check(
            f"C ratio-identity N={N} m={m} (d={d})",
            lhs == rhs,
            f"phi(R)*N*phi(d)={lhs} vs phi(N)*R*d={rhs}",
        )

# ---- D. End-to-end formula vs brute force at unaligned L, exhaustive ----
countD = 0
for N in N_RANGE:
    for m in M_RANGE:
        d, R, T = derived(N, m)
        for a in range(0, m):
            countD += 1
            for L in (T + 1, T + max(1, T // 3), 3 * T + 2, 1, max(1, T - 1)):
                pred = predicted_count(L, m, a, N)
                bf = brute_count(L, m, a, N)
                check(
                    f"D end-to-end N={N} m={m} a={a} L={L}",
                    pred == bf,
                    f"predicted={pred} brute={bf}",
                )

# ---- E. Minimality of T_min (Claim 3), EXHAUSTIVE via divisors of T_min ----
countE = 0
for N in N_RANGE:
    for m in M_RANGE:
        d, R, T = derived(N, m)
        for a in range(0, m):
            if gcd(a, d) != 1:
                continue  # zero branch: minimality undefined/vacuous, not tested here
            countE += 1
            arr = [1 if accepted(i + 1, m, a, N) else 0 for i in range(T)]
            min_t = T
            for t in divisors(T):
                if all(arr[i] == arr[i % t] for i in range(T)):
                    min_t = t
                    break
            check(
                f"E minimality N={N} m={m} a={a}",
                min_t == T,
                f"found smaller period t={min_t} < T_min={T}",
            )

# ---- F. Explicit boundary / base cases + distinguished examples ----

def base_case_check(name, N, m, a, expect_zero=False):
    d, R, T = derived(N, m)
    if expect_zero:
        L = max(5 * T, 20)
        bf = brute_count(L, m, a, N)
        check(f"F {name}", bf == 0, f"expected 0 got {bf}")
        return
    phiR = euler_phi(R)
    bf = brute_count(T, m, a, N)
    check(f"F {name} count", bf == phiR, f"brute={bf} phi(R)={phiR}")
    lhs = euler_phi(R) * N * euler_phi(d)
    rhs = euler_phi(N) * R * d
    check(f"F {name} ratio", lhs == rhs, f"{lhs} vs {rhs}")

base_case_check("N=1,m=1,a=0", 1, 1, 0)
base_case_check("N=1,m=5,a=2", 1, 5, 2)
base_case_check("N=5,m=1,a=0", 5, 1, 0)
base_case_check("N=17,m=1,a=0 (prime N)", 17, 1, 0)
base_case_check("N=16,m=1,a=0 (prime power N)", 16, 1, 0)
base_case_check("N=6,m=5,a=1 (coprime N,m)", 6, 5, 1)
base_case_check("N=5,m=6,a=2 (weakened admissibility)", 5, 6, 2)
base_case_check("N=18,m=2,a=1 (non-squarefree N', discriminator)", 18, 2, 1)

# (6,4,2) is the zero-branch example -- reported here explicitly and
# separately, NOT counted among Section E's minimality tests (minimality
# is undefined/vacuous on the zero branch: the indicator is identically
# 0, trivially periodic with period 1).
d647, R647, T647 = derived(6, 4)
zero_case_ok = brute_count(max(5 * T647, 20), 4, 2, 6) == 0
check("F (6,4,2) zero-branch example", zero_case_ok, "expected identically 0")

base_case_check("N=12,m=8,a=3", 12, 8, 3, expect_zero=(gcd(3, radical(gcd(8, 12))) > 1))

# negative a spot check
countF2 = 0
for (N, m, a) in [(18, 2, -1), (30, 4, -3), (5, 6, -4), (100, 10, -7), (6, 4, -2)]:
    countF2 += 1
    d, R, T = derived(N, m)
    if gcd(a, d) > 1:
        L = max(5 * T, 20)
        bf = brute_count(L, m, a, N)
        check(f"F2 negative-a zero N={N} m={m} a={a}", bf == 0, f"got {bf}")
    else:
        phiR = euler_phi(R)
        bf = brute_count(T, m, a, N)
        check(f"F2 negative-a count N={N} m={m} a={a}", bf == phiR, f"brute={bf} phi(R)={phiR}")

# ============================== REPORT ==============================

print("=" * 72)
print("GENERAL DIVISOR THEOREM -- INDEPENDENT VERIFICATION REPORT (rev. 2)")
print("=" * 72)
print(f"Grid: N in {list(N_RANGE)[0]}..{list(N_RANGE)[-1]}, m in {list(M_RANGE)[0]}..{list(M_RANGE)[-1]}")
print(f"Section A (arbitrary-window exact count, Claim 2): {countA_cases} nonzero-branch (N,m,a) cases, "
      f"{countA_windows} total windows checked")
print(f"Section B (zero branch, Claim 1):                  {countB} cases checked")
print(f"Section C (ratio exact identity, Claim 4, incl. d=1): {countC} (N,m) pairs checked")
print(f"Section D (end-to-end, 5 L values each):           {countD} (N,m,a) triples, {countD*5} total checks")
print(f"Section E (EXHAUSTIVE minimality via divisors, Claim 3): {countE} nonzero-branch cases checked")
print(f"Section F (boundary/base/distinguishing cases):    9 named cases + (6,4,2) zero-branch example "
      f"reported separately (not a minimality test)")
print(f"Section F2 (negative a):                            {countF2} cases checked")
print("-" * 72)
if failures:
    print(f"RESULT: {len(failures)} FAILURE(S) FOUND")
    for f in failures[:50]:
        print(" -", f)
    if len(failures) > 50:
        print(f"   ... and {len(failures)-50} more")
else:
    print("RESULT: ALL CHECKS PASSED, NO COUNTEREXAMPLES FOUND")
print("=" * 72)
