#!/usr/bin/python3

def print_board(board):
    """Prints the current state of the Tic Tac Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    """Checks if there is a winner on the board."""
    # Check rows
    for row in board:
        if row[0] != " " and row.count(row[0]) == len(row):
            return True

    # Check columns
    for col in range(len(board[0])):
        if (board[0][col] == board[1][col] == board[2][col] and
                board[0][col] != " "):
            return True

    # Check diagonals
    if (board[0][0] == board[1][1] == board[2][2] and
            board[0][0] != " "):
        return True

    if (board[0][2] == board[1][1] == board[2][0] and
            board[0][2] != " "):
        return True

    return False


def tic_tac_toe():
    """Main game loop for Tic Tac Toe."""
    board = [[" "] * 3 for _ in range(3)]
    player = "X"
    moves_played = 0  # to detect draw (max 9 moves)

    while True:
        print_board(board)

        # --- Get valid input from user ---
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
        except ValueError:
            print("Invalid input. Please enter numeric values (0, 1, or 2).")
            continue

        # Check bounds
        if row not in [0, 1, 2] or col not in [0, 1, 2]:
            print("Row and column must be 0, 1, or 2. Try again.")
            continue

        # Check if spot is free
        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        # Place the move
        board[row][col] = player
        moves_played += 1

        # Check for winner
        if check_winner(board):
            print_board(board)
            print("Player " + player + " wins!")
            break

        # Check for draw
        if moves_played == 9:
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        player = "O" if player == "X" else "X"


tic_tac_toe()
