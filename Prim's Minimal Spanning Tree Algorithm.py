import heapq

def prim_mst(graph, start):
    # Number of vertices in the graph
    n = len(graph)
    
    # Initialize the MST, visited set, and a priority queue
    mst = []
    visited = [False] * n
    min_heap = [(0, start)]  # (weight, node)
    total_cost = 0

    while min_heap:
        weight, u = heapq.heappop(min_heap)

        # Skip if the node has already been visited
        if visited[u]:
            continue
        
        visited[u] = True
        total_cost += weight

        # Add the edge to MST
        if weight != 0:
            mst.append((u, weight))

        # Add all the adjacent edges to the min-heap
        for v, w in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v))

    return mst, total_cost


# Graph represented as an adjacency list
# graph[u] = [(v1, weight), (v2, weight), ...]
graph = {
    0: [(1, 4), (2, 3), (3, 6)],  # Node 0 is connected to 1, 2, 3
    1: [(0, 4), (3, 2)],          # Node 1 is connected to 0, 3
    2: [(0, 3), (3, 5)],          # Node 2 is connected to 0, 3
    3: [(0, 6), (1, 2), (2, 5)]   # Node 3 is connected to 0, 1, 2
}

# Start Prim's algorithm from node 0
mst, total_cost = prim_mst(graph, 0)

# Output the MST and its total cost
print("MST edges with their weights:", mst)
print("Total cost of MST:", total_cost)

#Prim's Algorithm is a greedy algorithm used to find a Minimum Spanning Tree (MST) of a connected, undirected graph.
#The MST is a tree that connects all the vertices in the graph with the minimum possible total edge weight.
#The key characteristic of Prim's algorithm is that it starts from any node and grows the MST by adding edges that
#connect the tree to vertices outside it, always choosing the edge with the smallest weight.
