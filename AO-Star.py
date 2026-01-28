class Graph:
    def __init__ (self, graph, heuristic, start):
        self.graph = graph # AND-OR graph (dictionary)
        self.heuristic = heuristic # Heuristic values of nodes
        self.start = start # Start node
        self.solution_graph = {} # Stores final solution graph
        
    def get_neighbors(self, node):
        return self.graph.get(node, [])
    
    def ao_star(self, node):
        print(f"Processing Node: {node}")
        if node not in self.graph or not self.graph[node]:
            return self.heuristic[node] # Leaf node, return heuristic
        min_cost = float('inf')
        best_child = None
        
        # Evaluate all possible child groups (AND/OR)
        for child_group in self.graph[node]:
            cost = 0
            for child in child_group:
                cost += self.heuristic[child]
            if cost < min_cost:
                min_cost = cost
                best_child = child_group
                
        # Update heuristic with minimal cost found
        self.heuristic[node] = min_cost
        self.solution_graph[node] = best_child
        
        # Recursively apply AO* to the best child group
        for child in best_child:
            self.ao_star(child)
        
        return self.heuristic[node]
    def print_solution(self):
        print("\n--- Optimal Solution Graph ---")
        for node in self.solution_graph:
            print(f"{node} → {self.solution_graph[node]}")

# ---- MAIN PROGRAM ----
if __name__ == "__main__":
    # Graph structure (AND-OR graph)
    # Each node has multiple alternatives (OR)
    # Each alternative may contain one or more children (AND)
    graph = {
    'A': [['B', 'C'], ['D']],
    # A → B and C (AND) OR D (OR)
    'B': [['E'], ['F']],
    'C': [['G'], ['H']],
    'D': [['I']],
    'E': [], 'F': [], 'G': [], 'H': [], 'I': []
    }
    # Heuristic values for each node
    heuristic = {
    'A': 10, 'B': 4, 'C': 6, 'D': 8,
    'E': 3, 'F': 2, 'G': 1, 'H': 5, 'I': 4
    }
    start_node = 'A'
    ao = Graph(graph, heuristic, start_node)
    print("\n--- AO* Algorithm ---")
    ao.ao_star(start_node)
    ao.print_solution()