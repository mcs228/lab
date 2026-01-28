def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    # Visit all unvisited neighbors
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
# ---- MAIN PROGRAM ----
if __name__ == "__main__":
    # Graph represented as an adjacency list
    graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
    }
    print("Depth First Search starting from vertex A:")
    dfs(graph, 'A')