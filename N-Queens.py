def print_solution(board):
    n = len(board)
    for i in range(n):
        print(" ".join("Q" if board[i] == j else "." for j in range(n)))
    print("-" * (2 * n))
    
def is_safe(board, row, col):
    for r in range(row):
        c = board[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True

def solve_n_queens_iterative(n):
    board = [-1] * n
    row = 0
    col = 0
    solutions = []
    while row >= 0:
        found_safe = False
        # Try to place a queen in the current row
        while col < n:
            if is_safe(board, row, col):
                board[row] = col
                found_safe = True
                break
            col += 1
        if found_safe:
            if row == n - 1:
                # Found a valid solution
                solutions.append(board[:])
                # Backtrack to find more
                board[row] = -1
                row -= 1
                col = board[row] + 1 if row >= 0 else 0
            else:
                # Move to next row
                row += 1
                col = 0
        else:
            # No valid column in this row, backtrack
            board[row] = -1
            row -= 1
            if row >= 0:
                col = board[row] + 1
    return solutions

# ---- MAIN ----
n = int(input("Enter the value of N (>=4): "))
solutions = solve_n_queens_iterative(n)
print(f"\nTotal solutions for {n}-Queens: {len(solutions)}\n")
for sol in solutions:
    print_solution(sol)