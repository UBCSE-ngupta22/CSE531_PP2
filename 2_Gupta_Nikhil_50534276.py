def kruskal(n, k, weightedEdges):
    # Using Union Find Data Structure
    def findSet(u, par):
        if par[u] != u:
            par[u] = findSet(par[u], par)
        return par[u]

    def unionSets(u, v, par, depth):
        rootU, rootV = findSet(u, par), findSet(v, par)

        if rootU != rootV:
            if depth[rootU] > depth[rootV]:
                par[rootV] = rootU
            elif depth[rootU] < depth[rootV]:
                par[rootU] = rootV
            else:
                par[rootU] = rootV
                depth[rootV] += 1

    # Sort graph according to weights
    weightedEdges.sort(key=lambda item: item[2])
    depth = [0 for _ in range(n+1)]
    par = [_ for _ in range(n+1)]
    totalWeight, count = 0, 0

    for u, v, w in weightedEdges:
        if findSet(u, par) != findSet(v, par) and (n-count) != k:
            count += 1
            unionSets(u, v, par, depth)
            totalWeight += w

    return totalWeight


# Input
n, m, k = map(int, input().split())
weightedEdges = []

for _ in range(m):
    u, v, w = map(int, input().split())
    weightedEdges.append((u, v, w))

# Output
print(kruskal(n, k, weightedEdges))
