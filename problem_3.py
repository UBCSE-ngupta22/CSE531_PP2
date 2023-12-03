def bellmanFord(n, weightedEdges):
    inf = float('inf')
    dist = [inf] * (n + 1)

    dist[1] = 0  # Source as vertex 1

    # Relaxation
    for i in range(n - 1):
        for u, v, w in weightedEdges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    return "INFINITY" if dist[n] == inf else dist[n]


# Input
n, m = map(int, input().split())
weightedEdges = []

for _ in range(m):
    u, v, w = map(int, input().split())
    weightedEdges.append((u, v, w))

# No negative cycle detection required as its mentioned there is no negative cycle in the graph
# Output
print(bellmanFord(n, weightedEdges))
