import math

# Initialize the board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)
        
def check_winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
        
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

def is_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

# MINIMAX FUNCTION
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == 'O': # AI wins
        return 1
    elif winner == 'X': # Human wins
        return -1
    elif is_full(board):
        return 0
    
    if is_maximizing: # AI's turn
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else: # Human's turn
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score
    
# AI MOVE FUNCTION
def best_move(board):
    best_score = -math.inf
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
        move = (i, j)
    return move

#MAIN GAME LOOP
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("You are X, AI is O")
    print_board(board)
    while True:
        # Human move
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter col (0-2): "))
        except ValueError:
            print("Please enter valid integers!")
            continue
        if row not in [0,1,2] or col not in [0,1,2] or board[row][col] != ' ':
            print("Invalid move! Try again.")
            continue
        board[row][col] = 'X'
        if check_winner(board) == 'X':
            print_board(board)
            print("You win! 🎉")
            break
        elif is_full(board):
            print_board(board)
            print("It's a draw!")
            break
        # AI move
        ai_row, ai_col = best_move(board)
        board[ai_row][ai_col] = 'O'
        print("\nAI played:")
        print_board(board)
        if check_winner(board) == 'O':
            print("AI wins! 🤖")
            break
        elif is_full(board):
            print("It's a draw!")
            break
        
# Run the game
if __name__ == "__main__":
    play_game()