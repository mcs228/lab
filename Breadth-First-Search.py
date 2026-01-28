from collections import deque

def bfs(graph, start):
    visited = []
    queue = deque([start])
    # List to keep track of visited nodes
    # Initialize a queue with the start node
    while queue:
        node = queue.popleft() # Dequeue a node
        if node not in visited:
            print(node, end=" ") # Process the node (e.g., print it)
            visited.append(node)
            # Enqueue all unvisited neighbors
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# ---- MAIN PROGRAM ----
if __name__ == "__main__":
    # Representing the graph as an adjacency list
    graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
    }
    print("Breadth First Search starting from vertex A:")
    bfs(graph, 'A')