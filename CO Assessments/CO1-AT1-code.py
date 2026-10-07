from collections import deque

ROWS = 5
COLS = 5

START = (1, 1)
GOAL = (5, 5)

BLOCKED = {
    (2, 2),
    (2, 3),
    (3, 3),
    (4, 2),
    (4, 4)
}

MOVES = [
    ("Down", (1, 0)),
    ("Right", (0, 1)),
    ("Up", (-1, 0)),
    ("Left", (0, -1))
]


def valid_cell(state):
    r, c = state

    return (1 <= r <= ROWS and
            1 <= c <= COLS and
            state not in BLOCKED)


def get_neighbors(state):
    neighbors = []

    for action, (dr, dc) in MOVES:

        next_state = (
            state[0] + dr,
            state[1] + dc
        )

        if valid_cell(next_state):
            neighbors.append((next_state, action))

    return neighbors


def reconstruct_path(parent, state):

    path = []

    while state is not None:
        path.append(state)
        state = parent[state]

    path.reverse()

    return path


def bfs():

    queue = deque([START])

    parent = {
        START: None
    }

    expansion = 0

    print("\nBREADTH-FIRST SEARCH")

    while queue:

        print("\nQueue before expansion:")
        print(queue)

        current = queue.popleft()

        expansion += 1

        print("Expanded:", current)

        if current == GOAL:

            path = reconstruct_path(parent, current)

            print("\nGoal reached!")
            print("BFS Path:")
            print(path)

            print("BFS Cost:")
            print(len(path) - 1)

            print("BFS Nodes Expanded:")
            print(expansion)

            return path

        for next_state, action in get_neighbors(current):

            if next_state not in parent:

                parent[next_state] = current

                queue.append(next_state)

                print("Added:", next_state, "using", action)

        print("Queue after expansion:")
        print(queue)

    return None


def dfs():

    stack = [START]

    parent = {
        START: None
    }

    expansion = 0

    print("\nDEPTH-FIRST SEARCH")

    while stack:

        print("\nStack before expansion:")
        print(stack)

        current = stack.pop()

        expansion += 1

        print("Expanded:", current)

        if current == GOAL:

            path = reconstruct_path(parent, current)

            print("\nGoal reached!")
            print("DFS Path:")
            print(path)

            print("DFS Cost:")
            print(len(path) - 1)

            print("DFS Nodes Expanded:")
            print(expansion)

            return path

        neighbors = get_neighbors(current)

        for next_state, action in reversed(neighbors):

            if next_state not in parent:

                parent[next_state] = current

                stack.append(next_state)

                print("Pushed:", next_state, "using", action)

        print("Stack after expansion:")
        print(stack)

    return None


bfs_path = bfs()

dfs_path = dfs()


print("\nFINAL COMPARISON")

if bfs_path:

    print("\nBFS Path:")
    print(bfs_path)

    print("BFS Total Cost:")
    print(len(bfs_path) - 1)

else:

    print("\nBFS found no path.")


if dfs_path:

    print("\nDFS Path:")
    print(dfs_path)

    print("DFS Total Cost:")
    print(len(dfs_path) - 1)

else:

    print("\nDFS found no path.")
