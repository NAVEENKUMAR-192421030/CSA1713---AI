
# Map Coloring using Constraint Satisfaction Problem

regions = ['A', 'B', 'C', 'D']
colors = ['Red', 'Green', 'Blue']

neighbors = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

assignment = {}

def is_safe(region, color):
    for neighbor in neighbors[region]:
        if neighbor in assignment:
            if assignment[neighbor] == color:
                return False
    return True

def map_coloring(index):
    if index == len(regions):
        return True

    region = regions[index]

    for color in colors:
        if is_safe(region, color):
            assignment[region] = color

            if map_coloring(index + 1):
                return True

            del assignment[region]

    return False

if map_coloring(0):
    print("Map Coloring Solution:")
    for region in regions:
        print(region, ":", assignment[region])
else:
    print("No solution exists")
