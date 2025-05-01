import heapq

def dijkstra(graph, start):
    # Step 1: Set up the distances and priority queue
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]  # (distance, node) tuples
    visited = set()
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)  # Get the node with the smallest distance
        
        # If the node has already been visited, skip it
        if current_node in visited:
            continue
        
        visited.add(current_node)
        
        # Step 2: Update the distances for the neighbors
        for neighbor, weight in graph[current_node]:
            if neighbor in visited:
                continue
            
            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(pq, (new_distance, neighbor))  # Push the neighbor with the updated distance
                
    return distances

# Example graph represented as an adjacency list
graph = {
    'A': [('B', 2), ('D', 1)],
    'B': [('A', 2), ('C', 3)],
    'C': [('B', 3), ('D', 1)],
    'D': [('A', 1), ('C', 1)]
}

# Run Dijkstra's algorithm starting from node 'A'
distances = dijkstra(graph, 'A')

# Output the shortest distances from A to all other nodes
print("Shortest distances from A:", distances)

#Actually, Dijkstra's Algorithm is not typically used for finding a Minimum Spanning Tree (MST).
#Instead, Dijkstra's algorithm is a well-known shortest path algorithm used to find the shortest path
#from a source node to all other nodes in a graph with non-negative edge weights.

#To clarify:

#Dijkstra's Algorithm finds the shortest path from a source vertex to all other vertices in a weighted graph.

#Prim’s Algorithm and Kruskal’s Algorithm are used to find the Minimum Spanning Tree (MST) of a graph.
