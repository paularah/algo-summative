from heapq import heappop, heappush
from collections import defaultdict
import sys


def create_adjancency_list(edges):
    # creates a graph
    graph = defaultdict(list)
    # iterates over every egde and add it to th egraph
    for (start, end, weight) in edges:
        # Undirected graph has edge from start to end and end to start
        graph[start].append([end, weight])
        graph[end].append([start, weight])
    return graph


def shortest_reach(n, edges, s):
    """
    The shortest_reach funtion returns an array of the minumum distance between the start node and all other nodes in the graph. Where -1 in the output
    translates as  there are no edges, and 0 translates as the starting node.

    Time Complexity -> O(E*log(V)) where E is number of edges in the graph and V is the number of vertices in the graph. WE iterate over the edges (E) in the
    # graph and we leverage on the python min heap as a priority queue to get the minimum distanced vertex that amounts to O(LogV).
    Space Complexity -> O(E + V) - E is number of edges and V is the number of vertices used in making the adjacency list.
    """
    # creates an adjacency list from the edges
    graph = create_adjancency_list(edges)

    weights = [sys.maxsize] * (n + 1)
    # sets the weight of the starting vertex to 0

    weights[s] = 0
    # pushes the starting vertex to top of stack
    stack = [(s, 0)]

    # creats a set to keep track of  vertices that have been seen before
    seen_vertices = set()

    while stack:
        # retrives the last vertex from the top of the heap
        vertex, weight = heappop(stack)

        # if the vertex hasn't been previously seen
        if vertex not in seen_vertices:
            # add vertex to the set of previously seen vertices
            seen_vertices.add(vertex)
            # iterates over the vertices connected to the current vertex v
            for v_vertex, w_weight in graph[vertex]:
                # gets the current weight to reach vertex of child
                curr_weight = weights[v_vertex]
                # compares the current weight with weight derived from v_vertex parents added to the weight between
                #  child_v and v_vertex.
                if curr_weight > weight + w_weight:
                    weights[v_vertex] = weight + w_weight
                    # Push the updated vertex to the heap
                    heappush(stack, (v_vertex, weight + w_weight))
    path_weights = [-1 if weight ==
                    sys.maxsize else weight for weight in weights[1:]]
    return path_weights


start_node_number = 1
shortest_path_weights = shortest_reach(
    5, [[1, 2, 5], [1, 3, 15], [2, 3, 6], [3, 4, 2]], start_node_number)
for index in range(len(shortest_path_weights)):
    # skips the starting node nmber
    if index + 1 == start_node_number:
        continue
    # print out shortest paths in the specified format using f strings
    print(
        f"{start_node_number}/S -> {index + 1} - Shortest Path Value : {shortest_path_weights[index]}")
