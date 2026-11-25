import random
import math

n = 4

def conflicts(board):
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                count += 1
    return count

board = [random.randint(0, n - 1) for i in range(n)]

temperature = 100

while temperature > 0.1:
    if conflicts(board) == 0:
        break

    new_board = board[:]
    row = random.randint(0, n - 1)
    new_board[row] = random.randint(0, n - 1)

    old_cost = conflicts(board)
    new_cost = conflicts(new_board)

    if new_cost < old_cost:
        board = new_board
    else:
        probability = math.exp((old_cost - new_cost) / temperature)
        if random.random() < probability:
            board = new_board

    temperature *= 0.95

print("Final Board:")

for i in range(n):
    for j in range(n):
        if board[i] == j:
            print("Q", end=" ")
        else:
            print(".", end=" ")
    print()

print("Conflicts:", conflicts(board))

if conflicts(board) == 0:
    print("Solution Found")
else:
    print("Solution Not Found")
