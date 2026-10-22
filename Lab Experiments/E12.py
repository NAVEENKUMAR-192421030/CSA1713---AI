
# Tic-Tac-Toe Game

board = [' '] * 9

def display_board():
    print()
    for i in range(0, 9, 3):
        print(" " + " | ".join(board[i:i+3]))
        if i < 6:
            print("---+---+---")
    print()

def check_winner():
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in wins:
        if board[a] == board[b] == board[c] != ' ':
            return board[a]

    return None

print("TIC-TAC-TOE")
print("Positions:")
print("1 | 2 | 3")
print("--+---+--")
print("4 | 5 | 6")
print("--+---+--")
print("7 | 8 | 9")

player = 'X'

while True:
    display_board()

    try:
        position = int(input(
            "Player " + player + ", enter position (1-9): "
        ))
    except ValueError:
        print("Enter a valid number.")
        continue

    if position < 1 or position > 9:
        print("Choose a position from 1 to 9.")
        continue

    if board[position - 1] != ' ':
        print("Position already occupied. Try again.")
        continue

    board[position - 1] = player

    winner = check_winner()

    if winner:
        display_board()
        print("Player", winner, "wins!")
        break

    if ' ' not in board:
        display_board()
        print("The game is a draw!")
        break

    player = 'O' if player == 'X' else 'X'
