"""
tests/MB_0002_unit_group_quotients.py

Verification for MB_0002 (Unit-Group Structure Specifies Distinct
Quotient Readings).

Source: derived from the residue-manifold-learning "OpenWave"
group-structure audit (Q8-comparison work referenced earlier in this
project's history), re-derived independently here rather than
imported on the strength of that prior claim.

Claims checked:
  1. (Z/30Z)^x is isomorphic to C4 x C2 (not C8, not C2 x C2 x C2),
     established via its element-order profile, which is a complete
     invariant among abelian groups of order 8.
  2. (Z/30Z)^x has exactly three subgroups of order 2: <11>, <19>, <29>.
  3. The three order-2 subgroups give non-isomorphic quotients:
     (Z/30Z)^x / <19> = C2 x C2
     (Z/30Z)^x / <11> = C4
     (Z/30Z)^x / <29> = C4
     i.e. the choice of substructure specifies the quotient; no
     single quotient type is forced by the ambient group alone.
"""
from math import gcd


def run():
    n = 30
    units = [a for a in range(1, n) if gcd(a, n) == 1]

    def mult(a, b):
        return (a * b) % n

    def element_order(a):
        x, k = a, 1
        while x != 1:
            x = mult(x, a)
            k += 1
        return k

    orders = {a: element_order(a) for a in units}
    order_2 = sorted(a for a in units if orders[a] == 2)
    order_4 = sorted(a for a in units if orders[a] == 4)
    order_8 = sorted(a for a in units if orders[a] == 8)

    # Isomorphism type from element-order profile (complete invariant
    # for abelian groups of order 8: C8, C4xC2, C2xC2xC2 are
    # distinguished by their count of order-2 elements: 1, 3, 7
    # respectively).
    if order_8:
        group_type = "C8"
    elif len(order_2) == 7:
        group_type = "C2xC2xC2"
    elif len(order_2) == 3 and len(order_4) == 4:
        group_type = "C4xC2"
    else:
        group_type = "UNRECOGNIZED"

    quotient_results = []
    for gen in order_2:
        H = {1, gen}
        cosets, seen = [], set()
        for a in units:
            if a in seen:
                continue
            coset = frozenset(mult(a, h) for h in H)
            cosets.append(coset)
            seen |= coset
        coset_reps = {min(c): c for c in cosets}

        def coset_of(a, reps=coset_reps):
            for rep, c in reps.items():
                if a in c:
                    return rep
            raise ValueError

        identity = coset_of(1)
        quot_orders = {}
        for r in coset_reps:
            x, k = r, 1
            while x != identity:
                x = coset_of(mult(x, r))
                k += 1
            quot_orders[r] = k
        max_order = max(quot_orders.values())
        quot_type = "C4" if max_order == 4 else "C2xC2" if max_order == 2 else "?"
        quotient_results.append({
            "generator": gen,
            "subgroup": sorted(H),
            "cosets": [sorted(c) for c in cosets],
            "quotient_element_orders": quot_orders,
            "quotient_type": quot_type,
        })

    summary = {
        "group_type_confirmed": group_type,
        "group_type_expected": "C4xC2",
        "group_type_match": group_type == "C4xC2",
        "order_2_subgroup_count": len(order_2),
        "order_2_subgroup_count_expected": 3,
        "quotient_types": {r["generator"]: r["quotient_type"] for r in quotient_results},
        "quotient_types_expected": {19: "C2xC2", 11: "C4", 29: "C4"},
        "distinct_quotient_types_from_same_ambient_group": len(
            set(r["quotient_type"] for r in quotient_results)
        ) > 1,
        "claim_status": "supported" if (
            group_type == "C4xC2"
            and len(order_2) == 3
            and {r["generator"]: r["quotient_type"] for r in quotient_results}
                == {19: "C2xC2", 11: "C4", 29: "C4"}
        ) else "rejected",
    }

    return {
        "units": units,
        "element_orders": orders,
        "order_2_elements": order_2,
        "order_4_elements": order_4,
        "quotient_results": quotient_results,
        "summary": summary,
    }


if __name__ == "__main__":
    import json
    print(json.dumps(run(), indent=2))
