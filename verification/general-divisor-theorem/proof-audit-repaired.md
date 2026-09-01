# Proof Audit (Repaired): `general-divisor-theorem.md` v2 against `theorem-specification.md`

Specification treated as authoritative throughout; `theorem-specification.md` unchanged since
the first audit. `proof-audit.md` preserved unchanged as the prior record. This audit covers the
repaired `general-divisor-theorem.md` after the three targeted edits (restored exponent-blindness
lemma; arbitrary-window generalization for Claim 2; explicit periodicity proof for Claim 3).
Every step below was re-derived by hand against the document text — none of this relies on the
computational test suite to fill in a step the prose doesn't establish.

---

## Claim 1 — Dichotomy on $a$

**PROOF LOCATION.** "Proof of the case split and the count," first half — unchanged from the
prior audit.

**AUDIT.** No edits were made to this part of the document, and none were needed. Re-checked
against the frozen spec: variables match, the argument that a shared prime $p\mid\gcd(a,d)$ kills
every $n$ in the class (not just asymptotically) is intact, no hidden assumptions.

**STATUS: PROVED AS STATED.** (Unchanged from first audit.)

---

## Claim 2 — Exact per-period count

**PROOF LOCATION.** "Proof of the case split and the count," second half, now extended with the
new paragraph beginning "This bijection is a statement about residues mod $mR$..."

**AUDIT.** The repair replaces "within one block of length $mR$" with a bijection stated purely
in terms of residues mod $mR$ (not tied to any interval), then adds the explicit fact needed to
port that to arbitrary windows: **every interval of $mR$ consecutive integers is a complete
residue system mod $mR$**. This is a standard elementary fact (an immediate consequence of the
division algorithm — among any $mR$ consecutive integers, each residue class mod $mR$ is hit
exactly once) and is stated precisely enough to check: "as $n$ ranges over any such interval,
$n\bmod mR$ takes each value in $\{0,\dots,mR-1\}$ exactly once." Given that, the sub-collection
with $n\equiv a\pmod m$ within *any* such window numbers exactly $R$ elements (one for each
residue mod $mR$ that reduces to $a$ mod $m$) and bijects onto $\mathbb Z/R\mathbb Z$ via
$n\bmod R$ by the identical argument used for the first block — this re-use is legitimate because
the bijection argument was never actually tied to a specific interval, only to the residue
structure, which is the same in every window.

The closing sentence — "summing over $q$ disjoint consecutive such windows gives
$|S(qT_{\min})|=q\varphi(R)$" — is now a direct consequence (each window independently
contributes exactly $\varphi(R)$, by the paragraph just proved) rather than an implicit step. This
matches the frozen Claim 2 exactly: "for every $n_0$... any half-open window... $|S(qT_{\min})| =
q\cdot\varphi(R)$."

Re-derived independently: taking any $k\ge0$ and the window $(kT_{\min}, (k+1)T_{\min}]$ (i.e.
$mR$ consecutive integers starting at $kT_{\min}+1$), the argument gives exactly $\varphi(R)$
accepted values in it, for every $k$ — which is precisely "any half-open window" restricted to
period-aligned windows, and the document's general argument (any $mR$ consecutive integers, not
only period-aligned ones) is in fact strictly more general than what the spec's second sentence
literally requires, while matching the first sentence ("any half-open window") exactly.

**STATUS: PROVED AS STATED.** Gap from the first audit closed.

---

## Claim 3 — Minimality of $T_{\min}$

**PROOF LOCATION.** Two paragraphs, now separated with distinct headers: "Proof that
$T_{\min}=mR$ is a period" (new) and "Proof that no smaller $t$ is a period" (the original CRT
witness argument, retained verbatim as requested, only its header and one internal
cross-reference changed).

**AUDIT — the new periodicity paragraph.** Re-derived by hand, checking each inference:

1. *Factorization.* $I(n) = \mathbb1[n\equiv a\pmod m]\cdot\mathbb1[\gcd(n,R)=1]$ is claimed to
   hold for **all** $n$, not just accepted ones. Checked both sub-cases: if $n\not\equiv a\pmod
   m$, the first factor is $0$ and $I(n)=0$ by definition of "accepted," consistent regardless of
   the second factor's value. If $n\equiv a\pmod m$, the first factor is $1$, and $I(n)$ reduces
   to $\mathbb1[\gcd(n,N)=1]$, which the document correctly identifies (via the case-split
   argument earlier in the proof, properly cross-referenced with "by the reduction established
   above") as equal to $\mathbb1[\gcd(n,R)=1]$ *given* $\gcd(a,d)=1$. So the factorization holds
   identically, not merely on the accepted subset — this is the right level of generality for a
   periodicity argument, since periodicity must hold for every $n$, not only accepted ones.

2. *Period of each factor.* First factor: period $m$ is immediate from depending only on $n\bmod
   m$. Second factor: the claim "$\gcd(n,R)=1$ is determined entirely by which primes of $R$
   divide $n$, and $n\bmod R$ determines that" is correct — for any prime $p\mid R$, $p\mid n
   \iff p \mid (n\bmod R)$, since $p\mid R$ means reduction mod $p$ factors through reduction mod
   $R$. So the second factor has period $R$. Both are elementary and correctly justified, not
   merely asserted.

3. *Combining periods.* "Since $m\mid mR$ and $R\mid mR$, both factors... are unchanged under
   $n\mapsto n+mR$." This is the standard fact that a period-$p$ function is also invariant under
   shifts by any multiple of $p$ — used correctly and is elementary enough not to need its own
   sub-proof (on the same footing as the document's un-reproved use of CRT elsewhere).

This paragraph is independent of the windowed-count argument (Claim 2's proof), as intended and
as explicitly noted in the document's own parenthetical remark — checked, and the independence
claim is accurate: nowhere does this paragraph invoke $\varphi(R)$ or the count.

**AUDIT — the retained witness argument.** Unchanged from the first audit, where it was already
found sound (the $m\mid t$ and $p\mid t$-for-every-$p\mid R$ steps are both self-contained and
were not the source of the original gap). Re-checked here for consistency with the new material:
the argument still doesn't depend on "$mR$ is a period" as a premise — it only concludes $t\ge
mR$ for any period $t$, which is the correct complementary half.

**AUDIT — the closing line.** "Combined with the previous paragraph — that $mR$ itself *is* a
period — this gives $T_{\min}=mR$ exactly minimal: it is a period, and no smaller positive integer
is." This now correctly cites both halves as jointly necessary and sufficient: existence (from the
new paragraph) plus the lower bound (from the retained paragraph) together give exact minimality.
No circularity: the existence half doesn't use the lower-bound half, and vice versa, confirmed
above.

**STATUS: PROVED AS STATED.** Gap from the first audit closed. Both proof halves are now present,
independent, and correctly combined; this is exactly the two-part structure requested (new
periodicity argument for existence, retained CRT witness argument for the lower bound) rather than
replacing one with the other.

---

## Claim 4 — Correction factor exact identity

**PROOF LOCATION.** "Proof of the ratio $C(N,m)=d/\varphi(d)$," now explicitly citing the
restored Lemma at both points, plus the new "Lemma (exponent-blindness)" section itself
(between Setup and Theorem 3).

**AUDIT — the Lemma.** Re-derived by hand: for $k=1$, both sides are $1/1$ and $1/1$ — trivially
equal (using $\varphi(1)=1$ and $\operatorname{rad}(1)=1$ by convention, consistent with the rest
of the document). For $k>1$, $k/\varphi(k) = \prod_i p_i^{e_i}/\varphi(p_i^{e_i})$ by
multiplicativity — correct, standard. Each factor $p_i^{e_i}/\varphi(p_i^{e_i}) = 1/(1-1/p_i)$,
verified directly from $\varphi(p^e)=p^e-p^{e-1}=p^e(1-1/p)$, independent of $e$ — correct. The
resulting product $\prod_{p\mid k} p/(p-1)$ depends only on the set $\{p : p\mid k\}$, which is
exactly $\operatorname{rad}(k)$'s prime set, and applying the identical computation to
$\operatorname{rad}(k)$ (all exponents $1$) gives the same product — correct, and the "$e_i\ge1$
only" domain restriction is handled correctly since $\operatorname{rad}(k)$'s exponents are all
exactly $1\ge1$.

**AUDIT — the two invocations.** First: "$\varphi(B)/B=\varphi(R)/R$" is now explicitly derived
by applying the Lemma to $k=B$ (noting $\operatorname{rad}(B)=R$, established in the setup of
this proof paragraph, $B=\prod_{p\mid N,p\nmid m}p^{e_p}$). Re-checked: $\operatorname{rad}(B)$ is
indeed $R$, since $B$'s prime factors are exactly $N$'s primes not dividing $m$, which is $R$'s
defining set. Second: "$A/\varphi(A)=d/\varphi(d)$" applies the Lemma to $k=A$
($\operatorname{rad}(A)=d$, similarly checked correct). Both invocations are now named and
justified, closing the citation gap identified in the first audit.

**AUDIT — the surrounding algebra.** Unchanged from the first audit, where every equality was
already re-derived by hand and found correct (the chain of fraction manipulations, the
cancellation reducing to $A/\varphi(A)$, and the final substitution). $\varphi(N)=\varphi(A)\varphi(B)$
is now explicitly labeled "by multiplicativity of $\varphi$ over coprime arguments" — this is a
standard, widely-citable fact (on the same footing as CRT, which the document also uses without
re-proof throughout) and does not need its own lemma in this file.

**STATUS: PROVED AS STATED.** Gap from the first audit closed — the previously unstated
exponent-blindness fact is now an explicit, proved lemma, cited by name at both points where it's
used.

---

## Dependency map (post-repair)

```
Lemma (exponent-blindness)  [NEW, proved from phi(p^e)/p^e = 1-1/p + multiplicativity]
        |
        +--> Claim 4, first invocation: phi(B)/B = phi(R)/R
        +--> Claim 4, second invocation: A/phi(A) = d/phi(d)

CRT (existence, coprime moduli) [standard, cited not reproved -- same treatment throughout]
        |
        +--> Claim 1: n = a (mod m), p|m => n = a (mod p)  [elementary, not CRT itself]
        +--> Claim 2: bijection {n mod mR : n=a(m)} <-> Z/RZ
        +--> Claim 3 (lower bound half): witnesses n0, n1

Complete-residue-system fact [NEW, standard, one-line justification given]
        |
        +--> Claim 2: extends the bijection to every window, not one block

Product-of-periodic-functions fact [NEW, elementary, justified inline]
        |
        +--> Claim 3 (existence half): I(n) factors into period-m x period-R, so mR is a period

Multiplicativity of phi over coprime arguments [standard, cited not reproved]
        |
        +--> Claim 4: phi(N) = phi(A)*phi(B)
```

No claim now depends on an unstated fact. The two gaps from the first audit are closed by the two
new boxed items above (the Lemma and the product-of-periodic-functions fact); everything else was
already sound and is unchanged.

---

## Summary

| Claim | First audit | This audit |
|---|---|---|
| 1 (dichotomy) | PROVED AS STATED | PROVED AS STATED (unchanged) |
| 2 (exact count, arbitrary windows) | PROOF GAP | **PROVED AS STATED** |
| 3 (minimality) | PROOF GAP | **PROVED AS STATED** |
| 4 (ratio identity) | USES UNSTATED ASSUMPTION | **PROVED AS STATED** |

**No new gaps found.** All four claims now reach `PROVED AS STATED` against the unchanged frozen
specification, with every step re-derived by hand in this audit rather than taken on the strength
of the computational tests. The chain is now: theorem candidate → frozen specification →
adversarial computation (`test_general_divisor_theorem.py`, `verification-results.md`) → proof
audit (`proof-audit.md`) → explicit repairs (`general-divisor-theorem.md` v2) → this post-repair
audit (`proof-audit-repaired.md`). `proof-audit.md` is left in place unchanged as the record of
what was found and fixed.
