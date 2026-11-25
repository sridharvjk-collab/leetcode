from collections import deque
class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        queue = deque([source])
        visited.add(source)
        while queue:
            curr = queue.popleft()
            for neighbour in graph[curr]:
                if neighbour == destination:
                    return True
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
        return False