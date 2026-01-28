if __name__ == "__main__":
    # Graph represented as adjacency list with edge costs
    graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [],
    'E': [('F', 1)],
    'F': []
    }
    # Heuristic values (estimated distance to goal)
    heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 2,
    'E': 1,
    'F': 0 # Goal node
    }
    start = 'A'
    goal = input("Enter the goal node: ").upper()
    print("\n--- Iterative Deepening A* (IDA*) Algorithm ---")
    ida_star(start, goal, graph, heuristic)