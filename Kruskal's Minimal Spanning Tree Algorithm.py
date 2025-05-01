class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))  # Each node is its own parent initially
        self.rank = [0] * n  # Rank is used for union by rank

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u != root_v:
            # Union by rank
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False

def kruskal_mst(n, edges):
    # Initialize the UnionFind structure
    uf = UnionFind(n)
    
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    mst = []
    total_cost = 0
    
    # Iterate over the edges in increasing order
    for u, v, weight in edges:
        if uf.union(u, v):  # If u and v are not in the same set
            mst.append((u, v, weight))
            total_cost += weight
    
    return mst, total_cost

# Graph represented as a list of edges (u, v, weight)
edges = [
    (0, 1, 4),  # Edge between node 0 and node 1 with weight 4
    (0, 2, 3),  # Edge between node 0 and node 2 with weight 3
    (0, 3, 6),  # Edge between node 0 and node 3 with weight 6
    (1, 3, 2),  # Edge between node 1 and node 3 with weight 2
    (2, 3, 5)   # Edge between node 2 and node 3 with weight 5
]

# Number of nodes (vertices) in the graph
n = 4

# Run Kruskal's algorithm
mst, total_cost = kruskal_mst(n, edges)

# Output the MST edges and their total cost
print("MST edges with their weights:", mst)
print("Total cost of MST:", total_cost)
#Kruskal's Algorithm is another greedy algorithm used to find the Minimum Spanning Tree (MST) of a connected,
#undirected graph. It works by selecting the edges with the smallest weights and adding them to the MST,
#ensuring no cycles are formed.
