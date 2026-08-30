"""
tests/MB_0004_removable_matching_verification.py

Verification for MB_0004 (Minimum Degree Specifies K-Removable Matching
Existence, With Two Necessary In-Domain Exceptions).

Source claim (Theorem 1.3, arXiv:2608.09394): every finite simple
k-connected graph G with delta(G) >= max(k+1, 2m-2) has a k-removable
matching of size m, except G = K_{2m-1}, or (k,m)=(1,2) and G is a
cycle. The threshold is sharp: max(k+1, 2m-1) removes both exceptions.

This script exhaustively checks all graphs on n=3..6 vertices against
every valid (k,m) pair whose hypothesis some such graph can satisfy,
confirms both named exceptions are genuinely necessary (not vacuous),
and spot-checks sharpness by searching for graphs at threshold-minus-1
that fail the conclusion.

KNOWN SCOPE LIMIT: exhaustive only to n=6, for tractability -- see
analysis/MB_0004_VERIFICATION_SCOPE_NOTE.md for the history of an
earlier filtering bug in this exact script, and
proofs/MB_0004_REMOVABLE_MATCHING_THRESHOLD.md for why this leaves
Lemma 3.5's regime (n>=7) computationally unchecked by this project.
"""
import networkx as nx
from itertools import combinations


def has_k_removable_matching(G: nx.Graph, k: int, m: int) -> bool:
    """True if some matching of size m in G, once removed, leaves G k-connected."""
    edges = list(G.edges())
    for combo in combinations(edges, m):
        used = set()
        disjoint = True
        for (u, v) in combo:
            if u in used or v in used:
                disjoint = False
                break
            used.add(u)
            used.add(v)
        if not disjoint:
            continue
        H = G.copy()
        H.remove_edges_from(combo)
        if H.number_of_nodes() >= 1:
            try:
                conn = nx.node_connectivity(H)
            except Exception:
                conn = 0
            if conn >= k:
                return True
    return False


def is_cycle(G: nx.Graph) -> bool:
    if G.number_of_nodes() < 3:
        return False
    degs = dict(G.degree())
    return all(d == 2 for d in degs.values()) and nx.is_connected(G)


def all_graphs(n: int):
    nodes = list(range(n))
    possible_edges = list(combinations(nodes, 2))
    for r in range(len(possible_edges) + 1):
        for edge_subset in combinations(possible_edges, r):
            G = nx.Graph()
            G.add_nodes_from(nodes)
            G.add_edges_from(edge_subset)
            yield G


def check_instance(G: nx.Graph, k: int, m: int):
    """Return None if the hypothesis isn't satisfied; else a result dict.

    Deliberately does NOT filter out n < 2m -- an earlier version of this
    script did, which silently excluded the K_{2m-1} exception (n=2m-1)
    from ever being tested. See analysis/MB_0004_VERIFICATION_SCOPE_NOTE.md.
    """
    n = G.number_of_nodes()
    if n < 2:
        return None
    delta = min(dict(G.degree()).values()) if G.number_of_edges() > 0 else 0
    kappa = nx.node_connectivity(G)
    threshold = max(k + 1, 2 * m - 2)
    if kappa < k or delta < threshold:
        return None

    if n < 2 * m:
        conclusion_holds = False  # cannot have a matching of size m at all
    else:
        conclusion_holds = has_k_removable_matching(G, k, m)

    is_K2m1 = (n == 2 * m - 1) and nx.is_isomorphic(G, nx.complete_graph(2 * m - 1))
    is_cycle_exc = (k == 1 and m == 2 and is_cycle(G))
    named_exception = is_K2m1 or is_cycle_exc

    return {
        "n": n, "k": k, "m": m,
        "conclusion_holds": conclusion_holds,
        "is_K2m1_exception": is_K2m1,
        "is_cycle_exception": is_cycle_exc,
        "theorem_consistent": conclusion_holds or named_exception,
    }


def run_main_theorem_check(n_max: int = 6):
    checked = 0
    consistent = 0
    counterexamples = []
    k2m1_triggered = 0
    cycle_triggered = 0

    for n in range(3, n_max + 1):
        for k in range(1, n):
            for m in range(1, n):
                if 2 * m - 1 > n:
                    continue
                for G in all_graphs(n):
                    res = check_instance(G, k, m)
                    if res is None:
                        continue
                    checked += 1
                    if res["theorem_consistent"]:
                        consistent += 1
                        if not res["conclusion_holds"]:
                            if res["is_K2m1_exception"]:
                                k2m1_triggered += 1
                            elif res["is_cycle_exception"]:
                                cycle_triggered += 1
                    else:
                        counterexamples.append(
                            {"n": n, "k": k, "m": m, "edges": list(G.edges())}
                        )

    return {
        "n_range_tested": [3, n_max],
        "instances_checked": checked,
        "instances_consistent": consistent,
        "counterexamples": counterexamples,
        "K2m1_exception_triggered_count": k2m1_triggered,
        "cycle_exception_triggered_count": cycle_triggered,
    }


def run_sharpness_check(n_max: int = 6):
    """Search for graphs at threshold-minus-1 that fail the conclusion,
    as spot-check evidence the degree bound cannot be lowered."""
    sharp_examples = []
    for n in range(4, n_max + 1):
        for k in range(1, n):
            for m in range(1, n):
                if 2 * m - 1 > n:
                    continue
                threshold = max(k + 1, 2 * m - 2)
                weak_threshold = threshold - 1
                if weak_threshold < 1:
                    continue
                for G in all_graphs(n):
                    delta = min(dict(G.degree()).values()) if G.number_of_edges() > 0 else 0
                    if delta != weak_threshold:
                        continue
                    kappa = nx.node_connectivity(G)
                    if kappa < k or n < 2 * m:
                        continue
                    if not has_k_removable_matching(G, k, m):
                        sharp_examples.append(
                            {"n": n, "k": k, "m": m, "delta": delta, "threshold": threshold}
                        )
                        break
    return {"sharpness_examples_found": len(sharp_examples), "examples": sharp_examples}


def run():
    main_result = run_main_theorem_check(n_max=6)
    sharpness_result = run_sharpness_check(n_max=6)

    claim_status = "supported" if (
        len(main_result["counterexamples"]) == 0
        and main_result["K2m1_exception_triggered_count"] > 0
        and main_result["cycle_exception_triggered_count"] > 0
    ) else "rejected"

    return {
        "main_theorem_check": main_result,
        "sharpness_check": sharpness_result,
        "summary": {
            "claim_status": claim_status,
            "note": (
                "Exhaustive only to n=6; Lemma 3.5's regime (n>=7) in the "
                "source proof is NOT covered by this check -- see "
                "proofs/MB_0004_REMOVABLE_MATCHING_THRESHOLD.md."
            ),
        },
    }


if __name__ == "__main__":
    import json
    print(json.dumps(run(), indent=2))
