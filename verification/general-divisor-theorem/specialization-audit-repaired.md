# Specialization Audit (Repaired): Theorem 3 ⊃ Theorem 2 ⊃ Theorem 1′ ⊃ Theorem 1

`specialization-audit.md` preserved unchanged as the record of what was found (the missing
Theorem 2 artifact). This audit re-checks the hierarchy now that `theorem-2-minimal-period.md`
exists as a standalone document, proved strictly by substitution into Theorem 3.

---

## Theorem 2 — now checkable

**Document.** `theorem-2-minimal-period.md`, newly created, explicit corollary of Theorem 3 under
$m\mid N$.

**Check.** The document's four-step substitution proof was re-verified line by line:

- Step 1 ($d=\operatorname{rad}(m)$): correct — $m\mid N$ collapses $\gcd(m,N)$ to $m$ by
  definition, so $\operatorname{rad}(\gcd(m,N))=\operatorname{rad}(m)$ directly.
- Step 2 (admissibility $\gcd(a,\operatorname{rad}(m))=1$): correct — direct substitution of Step
  1 into Theorem 3's $\gcd(a,d)=1$ condition, no new argument introduced or needed.
- Step 3 ($R=\operatorname{rad}(N)/\operatorname{rad}(m)$, $T_{\min}=m\operatorname{rad}(N)/\operatorname{rad}(m)$,
  count $\varphi(R)$): correct — pure substitution into Theorem 3's already-proved $R$, $T_{\min}$,
  and count formulas; minimality is inherited from Theorem 3's proof (which covers arbitrary
  $(N,m,a)$, including this case) without needing to be re-argued.
- Step 4 ($C=m/\varphi(m)$): correct — substitutes $d=\operatorname{rad}(m)$ into Theorem 3's
  $C=d/\varphi(d)$, then applies the exponent-blindness lemma to $k=m$, exactly as instructed.
  Re-derived by hand: $\operatorname{rad}(m)/\varphi(\operatorname{rad}(m)) = m/\varphi(m)$ is a
  direct instance of the lemma (`general-divisor-theorem.md`), not a new fact.

**Numerical re-check** ($N=12,m=2,a=1$, the document's own worked example, reused from
`specialization-audit.md`'s internal-consistency spot check): $d=2$, $R=3$, $T_{\min}=6$, count
$\varphi(3)=2$, $C=2$. Direct enumeration in $[1,6]$ for $n\equiv1\pmod2$, coprime to $12$:
$\{1,5\}$, count $2$. Matches on every quantity.

**STATUS: PROVED AS COROLLARY.** No independent re-derivation was required or performed — every
quantity in `theorem-2-minimal-period.md` is a direct substitution into already-proved Theorem 3
formulas, exactly as instructed. Gap from `specialization-audit.md` closed: Theorem 2 is now a
genuine, checkable artifact rather than a single surviving formula.

---

## Theorem 1′ — reclassification, not an edit

`extended-unitary-divisor-theorem.md` is unchanged (as instructed — preserved as historical
evidence). This audit only sharpens how its period claim is described, per the request to be more
precise than "period caveat."

**Precise statement.** Theorem 1′ proves that $N$ **is a period** of the accepted-set indicator —
that claim is correct and remains correct; nothing about it is false. What Theorem 1′ does not
claim, and does not need to claim for its own proof to hold, is that $N$ is the *minimal* period.
Given Theorem 2 (now a checkable document) and Theorem 3, the exact minimal period under Theorem
1′'s own hypotheses ($m$ unitary in $N$, so $m\mid N$ applies and Theorem 2 governs) is
$$
T_{\min} = m\,\frac{\operatorname{rad}(N)}{\operatorname{rad}(m)} = m\,\operatorname{rad}(N/m)
$$
(the second equality holds specifically under unitarity: $m$ unitary means $\operatorname{rad}(N)/\operatorname{rad}(m)=\operatorname{rad}(N/m)$,
since $N/m$'s primes are exactly $N$'s primes not dividing $m$ — the same reduction used in
`specialization-audit.md`'s Theorem 1′ section). And $T_{\min}\mid N$ always, with equality
exactly when $N/m$ is squarefree.

So, precisely: **Theorem 1′'s $N$ is a valid but generally non-minimal period; $T_{\min}=m\operatorname{rad}(N/m)$
is the minimal one, and $T_{\min}\mid N$.** The $N=18,m=2$ example remains the sharpest witness:
$N=18$ is a period (true, as Theorem 1′ claims), but the minimal period is $6=2\cdot\operatorname{rad}(9)$.

**On updating the wording.** Per instruction, `extended-unitary-divisor-theorem.md` is **not**
edited in this pass. When it is eventually revised, the audit here records the precise fix needed:
replace "period $N$" / "Write $L=qN+s$" framing with "**a** period $N$ (not necessarily minimal —
see Theorem 2 for the exact minimal period $m\operatorname{rad}(N/m)$)," since the current phrasing
implicitly reads as though $N$ is the fundamental period, which is true only in the squarefree-$N/m$
case.

**STATUS: PROVED AS COROLLARY** (unchanged from `specialization-audit.md`), now with a precise,
checkable minimality classification rather than an open caveat — because Theorem 2 supplies the
exact comparison point that was previously mechanically derived ad hoc within the audit itself.

---

## Theorem 1 — unchanged

No new information changes this check. Re-confirmed against `theorem-2-minimal-period.md` as an
intermediate step: Theorem 1's hypotheses ($N=P_k$ squarefree, $m$ squarefree) satisfy $m\mid N$
(Theorem 2 applies) and $m$ unitary in $N$ automatically (Theorem 1′ applies), and squarefreeness
of $N$ forces $N/m$ squarefree too, so Theorem 1′'s coarser period $N$ and Theorem 2/3's minimal
period $T_{\min}$ coincide — consistent with `specialization-audit.md`'s finding that Theorem 1
needed no period-minimality caveat at all.

**STATUS: PROVED AS COROLLARY, exact match** (unchanged from `specialization-audit.md`).

---

## Summary

| Specialization | Status (prior audit) | Status (this audit) |
|---|---|---|
| Theorem 2 | GAP — no standalone document | **PROVED AS COROLLARY** — `theorem-2-minimal-period.md` created |
| Theorem 1′ | PROVED AS COROLLARY (period caveat) | **PROVED AS COROLLARY** — caveat sharpened to an exact minimal-period formula; document itself left unedited pending a future wording pass |
| Theorem 1 | PROVED AS COROLLARY, exact | **PROVED AS COROLLARY, exact** (unchanged) |

**The hierarchy is now mechanically verified end to end:**
$$
\text{Theorem 1} \subset \text{Theorem 1}' \subset \text{Theorem 2} \subset \text{Theorem 3},
$$
with Theorem 3 supplying every load-bearing formula and each earlier stage recovered by pure
substitution — no independent re-derivations were needed anywhere in this pass, and no new
mismatches were found. The one open item is editorial, not mathematical: `extended-unitary-divisor-theorem.md`'s
period language should eventually be updated to say "a period" rather than implying minimality,
but per instruction that edit is deferred rather than made here.
