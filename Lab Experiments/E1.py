from collections import deque

def print_puzzle(state):
    for i in range(0, 9, 3):
        print(state[i], state[i+1], state[i+2])
    print()

def solve_8_puzzle(start, goal):
    queue = deque([(start, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state == goal:
            print("Solution found!")
            for step in path + [state]:
                print_puzzle(step)
            return

        if state in visited:
            continue

        visited.add(state)
        blank = state.index(0)
        row = blank // 3
        col = blank % 3

        moves = []

        if row > 0:
            moves.append(blank - 3)   # Up
        if row < 2:
            moves.append(blank + 3)   # Down
        if col > 0:
            moves.append(blank - 1)   # Left
        if col < 2:
            moves.append(blank + 1)   # Right

        for new_blank in moves:
            new_state = list(state)
            new_state[blank], new_state[new_blank] = \
                new_state[new_blank], new_state[blank]

            queue.append((tuple(new_state), path + [state]))

    print("No solution found.")

# Input
print("Enter the initial state:")
print("Use 0 for blank space")

start = tuple(map(int, input().split()))

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

solve_8_puzzle(start, goal)
