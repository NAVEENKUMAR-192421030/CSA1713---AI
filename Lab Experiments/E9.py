cities = ['A', 'B', 'C', 'D']

distance = {
    'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
}

def tsp_greedy(start):
    visited = [start]
    current = start
    total_distance = 0

    while len(visited) < len(cities):
        next_city = min(
            (city for city in cities if city not in visited),
            key=lambda city: distance[current][city]
        )

        total_distance += distance[current][next_city]
        visited.append(next_city)
        current = next_city

    total_distance += distance[current][start]
    visited.append(start)

    print("Tour:", " -> ".join(visited))
    print("Total Distance:", total_distance)

tsp_greedy('A')
