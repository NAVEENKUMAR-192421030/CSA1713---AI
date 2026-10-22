def astar(graph, heuristic, start, goal):
    open_list = [(heuristic[start], 0, start, [start])]
    visited = set()

    while open_list:
        open_list.sort()
        f, g, node, path = open_list.pop(0)

        if node == goal:
            print("Path:", path)
            print("Total Cost:", g)
            return

        if node in visited:
            continue

        visited.add(node)

        for neighbor, cost in graph[node].items():
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]
                open_list.append(
                    (new_f, new_g, neighbor, path + [neighbor])
                )

    print("No path found")


graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 3, 'E': 1},
    'C': {'F': 5},
    'D': {'G': 2},
    'E': {'G': 5},
    'F': {'G': 2},
    'G': {}
}

heuristic = {
    'A': 6,
    'B': 5,
    'C': 4,
    'D': 2,
    'E': 4,
    'F': 2,
    'G': 0
}

astar(graph, heuristic, 'A', 'G')
