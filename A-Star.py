from queue import PriorityQueue

def a_star(graph, start, goal, heuristic):
    open_list = PriorityQueue()
    open_list.put((0, start)) # (f(n), node)
    
    g_cost = {node: float('inf') for node in graph}
    g_cost[start] = 0
    
    came_from = {} # To reconstruct path
    
    while not open_list.empty():
        current_f, current = open_list.get()
        print(f"Visiting Node: {current} (f={current_f})")
        
        if current == goal:
            print("\nGoal Reached ✅")
            reconstruct_path(came_from, start, goal)
            return
        
        for neighbor, cost in graph[current]:
            tentative_g = g_cost[current] + cost
            if tentative_g < g_cost[neighbor]:
                came_from[neighbor] = current
                g_cost[neighbor] = tentative_g
                f_cost = tentative_g + heuristic[neighbor]
                open_list.put((f_cost, neighbor))
    print("\nGoal Not Found ❌")
    
def reconstruct_path(came_from, start, goal):
    path = [goal]
    while goal in came_from:
        goal = came_from[goal]
        path.append(goal)
    path.reverse()
    print("Optimal Path:", " → ".join(path))
    
# ---- MAIN PROGRAM ----
if __name__ == "__main__":
    # Graph represented as adjacency list with edge costs
    graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('F', 2)],
    'F': []
    }
    # Heuristic values (estimated distance to goal)
    heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 3,
    'E': 1,
    'F': 0 # Goal node
    }
    start = 'A'
    goal = input("Enter the goal node: ").upper()
    print("\n--- A* Search Algorithm ---")
    a_star(graph, start, goal, heuristic)