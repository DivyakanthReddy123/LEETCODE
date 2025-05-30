class Solution(object):
    def closestMeetingNode(self, edges, node1, node2):
        """
        :type edges: List[int]
        :type node1: int
        :type node2: int
        :rtype: int
        """

        def walk(start):
            n = len(edges)
            dist = [float('inf')] * n
            step, cur = 0, start
            while cur != -1 and dist[cur] == float('inf'):
                dist[cur] = step
                step += 1
                cur = edges[cur]
            return dist

        d1 = walk(node1)
        d2 = walk(node2)

        best_node, best_max = -1, float('inf')
        for i in range(len(edges)):
            max_d = max(d1[i], d2[i])
            if max_d < best_max:
                best_max = max_d
                best_node = i

        return best_node