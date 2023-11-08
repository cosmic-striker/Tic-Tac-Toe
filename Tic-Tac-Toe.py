import os

def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in board:
        print(" | ".join(row))
        if row != board[-1]:
            print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]  # Add a closing parenthesis here
    player = "X"

    while True:
        print_board(board)
        move = input(f"Player {player}, enter row and column (e.g., '1 2'): ")
        
        try:
            row, col = map(int, move.split())
            if row < 1 or row > 3 or col < 1 or col > 3 or board[row - 1][col - 1] != " ":
                print("Invalid move! Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input! Please enter row and column numbers.")
            continue

        board[row - 1][col - 1] = player

        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            ender=input("press any key to close th e file")
            exit()
            break
        elif is_full(board):
            print_board(board)
            print("It's a tie!")
            break

        player = "X" if player == "O" else "O"

if __name__ == "__main__":
    main()
