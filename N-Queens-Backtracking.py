def print_solution(board):
    """Prints the chessboard configuration."""
    n = len(board)
    for i in range(n):
        row = ""
        for j in range(n):
            if board[i] == j:
                row += "Q "
            else:
                row += ". "
        print(row)
    print("-" * (2 * n))

def is_safe(board, row, col):
    """Check if placing a queen at (row, col) is safe."""
    for r in range(row):
        c = board[r]
        # Check same column or diagonal attack
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True

def solve_n_queens(board, row, n, solutions):
    """Recursive backtracking function."""
    if row == n:
        # Found a valid placement for all rows
        solutions.append(board[:])
        return
    # Try placing a queen in each column of the current row
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_n_queens(board, row + 1, n, solutions)
            # Backtrack automatically when the function returns
            
def n_queens(n):
    """Driver function to find all solutions."""
    board = [-1] * n
    solutions = []
    solve_n_queens(board, 0, n, solutions)
    return solutions

# ---- MAIN PROGRAM ----
n = int(input("Enter the value of N (>=4): "))
solutions = n_queens(n)
print(f"\nTotal solutions for {n}-Queens: {len(solutions)}\n")
for sol in solutions:
    print_solution(sol)