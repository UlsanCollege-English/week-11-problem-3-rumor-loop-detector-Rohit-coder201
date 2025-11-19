"""
HW03 — Rumor Loop Detector (Cycle in Undirected Graph)

Implement:
- has_cycle(graph)
- find_cycle(graph)
"""

def has_cycle(graph):
    """Return True if the undirected graph has any cycle; else False."""

    visited = set()

    # DFS helper
    def dfs(node, parent):
        visited.add(node)
        for nbr in graph.get(node, []):
            # self-loop count
            if nbr == node:
                return True
            # normal cycle detection
            if nbr not in visited:
                if dfs(nbr, node):
                    return True
            elif nbr != parent:
                return True
        return False

    # run DFS from every component
    for u in graph:
        if u not in visited:
            if dfs(u, None):
                return True

    return False


def find_cycle(graph):
    """
    Return a list of nodes forming a simple cycle where first == last.
    If no cycle, return None.

    Rules:
    - Use DFS and parent map.
    - Self-loop counts as [u, u].
    """

    visited = set()
    parent = {}

    def dfs(node, par):
        visited.add(node)
        parent[node] = par

        for nbr in graph.get(node, []):
            # self-loop
            if nbr == node:
                return [node, node]

            if nbr not in visited:
                cycle = dfs(nbr, node)
                if cycle:
                    return cycle
            else:
                # found a back-edge (nbr != parent)
                if nbr != par:
                    # reconstruct cycle from node → ... → nbr
                    path = [node]
                    cur = node
                    while cur != nbr:
                        cur = parent[cur]
                        path.append(cur)
                    path.append(node)   # close the cycle
                    return path

        return None

    for u in graph:
        if u not in visited:
            cycle = dfs(u, None)
            if cycle:
                return cycle

    return None


if __name__ == "__main__":
    # Example graph with a cycle: A-B-C-A
    g = {
        'A': ['B'],
        'B': ['A', 'C'],
        'C': ['B', 'A']
    }
    print("Has cycle?", has_cycle(g))
    print("Example cycle:", find_cycle(g))
