from queue import PriorityQueue

def best_first_search(graph, start, goal, heuristic):
    visited = set()
    pq = PriorityQueue() # Priority Queue for selecting best node
    pq.put((heuristic[start], start)) # (priority, node)
    print("Best First Search Path:")
    
    while not pq.empty():
        cost, current = pq.get()
        print(current, end=" ")
        if current == goal:
            print("\nGoal Reached ✅")
            return
        visited.add(current)
        # Explore neighbors
        for neighbor in graph[current]:
            if neighbor not in visited:
                pq.put((heuristic[neighbor], neighbor))
    print("\nGoal Not Found ❌")

# ---- MAIN PROGRAM ----
if __name__ == "__main__":
# Graph represented as adjacency list
    graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
    }
    # Heuristic values (lower is better)
    heuristic = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 7,
    'E': 2,
    'F': 0
    # Goal node has 0 heuristic value
    }
    start = 'A'
    goal = input("Enter the goal node: ").upper()
    print("\n--- Best First Search ---")
    best_first_search(graph, start, goal, heuristic)