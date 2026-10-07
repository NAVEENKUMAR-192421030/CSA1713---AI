
from collections import deque

def is_valid(state):
    ML, CL, MR, CR, boat = state

    if ML < 0 or CL < 0 or MR < 0 or CR < 0:
        return False

    if ML > 3 or CL > 3 or MR > 3 or CR > 3:
        return False

    if ML > 0 and ML < CL:
        return False

  
    if MR > 0 and MR < CR:
        return False

    return True


def get_next_states(state):
    ML, CL, MR, CR, boat = state

    moves = [
        (2, 0), 
        (0, 2),  
        (1, 1), 
        (1, 0),  
        (0, 1)   
    ]

    next_states = []

    for m, c in moves:
        if boat == 0:
          
            new_state = (
                ML - m,
                CL - c,
                MR + m,
                CR + c,
                1
            )
        else:
          
            new_state = (
                ML + m,
                CL + c,
                MR - m,
                CR - c,
                0
            )

        if is_valid(new_state):
            next_states.append(new_state)

    return next_states


def solve():
    start = (3, 3, 0, 0, 0)
    goal = (0, 0, 3, 3, 1)

    queue = deque()
    queue.append((start, [start]))

    visited = set()
    visited.add(start)

    while queue:
        state, path = queue.popleft()

        if state == goal:
            print("Solution Found:")
            print()

            for i, s in enumerate(path):
                ML, CL, MR, CR, boat = s

                if boat == 0:
                    boat_side = "Left"
                else:
                    boat_side = "Right"

                print("Step", i, ":",
                      "Left(M,C) =", (ML, CL),
                      "Right(M,C) =", (MR, CR),
                      "Boat =", boat_side)

            return

        for next_state in get_next_states(state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [next_state]))

    print("No solution found.")


solve()
