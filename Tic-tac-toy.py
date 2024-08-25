def display_board(board):
    for i, row in enumerate(board):
        print(f" {row[0]} | {row[1]} | {row[2]} ")
        if i < 3:
            print("-----------")

def check_victory(board, symbol):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == symbol for j in range(3)) or  all(board[j][i] == symbol for j in range(3)):
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == symbol or board[0][2] == board[1][1] == board[2][0] == symbol:
        return True
    return False

def is_draw(board):
    return all(cell != " " for row in board for cell in row)

def get_move(player):
    while True:
        try:
            row = int(input(f"Player {player}, enter row (1-3): ")) - 1 # -1 to convert to 0-based index
            col = int(input(f"Player {player}, enter column (1-3): ")) - 1 # -1 to convert to 0-based index
            if 0 <= row <= 2 and 0 <= col <= 2:
                return row, col
            else:
                print("Invalid input. Row and column must be between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter numbers.")

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    while True:
        display_board(board)
        current_player = players[turn % 2]
        row, col = get_move(current_player)

        if board[row][col] == " ":
            board[row][col] = current_player
            if check_victory(board, current_player):
                display_board(board)
                print(f"Player {current_player} wins!")
                break
            elif is_draw(board):
                display_board(board)
                print("It's a draw!")
                break
            turn += 1
        else:
            print("That position is already occupied. Try again.")

if __name__ == "__main__":
    tic_tac_toe()
