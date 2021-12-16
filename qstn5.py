def shortestReach(n, edges, s):
    pathLengths = {v: float('inf') for v in n}
    pathLengths[s] = 0

    adjacentNodes = {v: {} for v in n}
    for (u, v), w_uv in edges.items():
        adjacentNodes[u][v] = w_uv
        adjacentNodes[v][u] = w_uv

    holdingNodes = [v for v in n]
    while len(holdingNodes) > 0:
        upper_bounds = {v: pathLengths[v] for v in holdingNodes}
        u = min(upper_bounds, key=upper_bounds.get)
        holdingNodes.remove(u)

        for v, w_uv in adjacentNodes[u].items():
            pathLengths[v] = min(pathLengths[v], pathLengths[u] + w_uv)

    return pathLengths


n = [0, 1, 2, 3, 4, 5]
edges = {(0, 1): 5, (0, 2): 4, (0, 3): 8, (1, 3): 3, (1, 4): 8, (2, 3): 7, (3, 5): 2}
s = 0

print(shortestReach(n, edges, s=0))
