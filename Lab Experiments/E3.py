from collections import deque

def water_jug(jug1, jug2, goal):
    queue = deque()
    queue.append((0, 0, []))

    visited = set()

    while queue:
        a, b, path = queue.popleft()

        if (a, b) in visited:
            continue

        visited.add((a, b))

        path = path + [(a, b)]

        if a == goal or b == goal:
            print("Solution found:")

            for state in path:
                print("Jug 1 =", state[0],
                      "Jug 2 =", state[1])

            return

        next_states = [
            (jug1, b),                  
            (a, jug2),                  
            (0, b),                     
            (a, 0),                     

            
            (a - min(a, jug2 - b),
             b + min(a, jug2 - b)),

            
            (a + min(b, jug1 - a),
             b - min(b, jug1 - a))
        ]

        for state in next_states:
            if state not in visited:
                queue.append((state[0], state[1], path))

    print("No solution found.")


water_jug(4, 3, 2)
