class Solution(object):
    def maxTargetNodes(self, edges1, edges2, k):
        
        from collections import defaultdict, deque
        def build_adj(n, edges):
            g = [[] for _ in range(n)]
            for u, v in edges:
                g[u].append(v)
                g[v].append(u)
            return g

        def bfs_count(src, g, limit):
            """number of nodes within distance ≤ limit from src"""
            if limit < 0:           # empty radius
                return 0
            seen = {src}
            q = deque([(src, 0)])
            while q:
                node, d = q.popleft()
                if d == limit:
                    continue
                for nb in g[node]:
                    if nb not in seen:
                        seen.add(nb)
                        q.append((nb, d + 1))
            return len(seen)

        # -------- trivial case ----------
        n = len(edges1) + 1
        if k == 0:
            return [1] * n          # only the node itself is reachable

        # -------- build graphs ----------
        m = len(edges2) + 1
        gA = build_adj(n, edges1)
        gB = build_adj(m, edges2)

        # -------- pre-compute reach counts ----------
        reachA = [bfs_count(i, gA, k)   for i in range(n)]     # distance ≤ k
        reachB = [bfs_count(j, gB, k-1) for j in range(m)]     # distance ≤ k-1 (edge adds 1)

        maxB = max(reachB)            # best B-side contribution works for every i
        return [a + maxB for a in reachA]