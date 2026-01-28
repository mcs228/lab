# Depth-Limited Search (DLS) - helper function
def dls(graph, node, goal, depth):
    print(f"Visiting Node: {node}, Depth Remaining: {depth}")
    if node == goal:
        return True
    if depth <= 0:
        return False
    for neighbor in graph.get(node, []):
        if dls(graph, neighbor, goal, depth - 1):
            return True
    return False

# Iterative Deepening DFS (IDDFS)
def iddfs(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        print(f"\nDepth Limit: {depth}")
        if dls(graph, start, goal, depth):
            print(f"\nGoal '{goal}' found at depth {depth} ✅")
            return True
    print(f"\nGoal '{goal}' not found within depth limit {max_depth} ❌")
    return False

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
    start = 'A'
    goal = input("Enter the goal node: ").upper()
    max_depth = int(input("Enter maximum depth limit: "))
    print("\n--- Iterative Deepening Depth First Search ---")
    iddfs(graph, start, goal, max_depth)