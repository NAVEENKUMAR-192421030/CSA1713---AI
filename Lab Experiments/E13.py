
# Minimax Algorithm

# Game tree:
# MAX root has two MIN children.
# Each MIN child has two terminal scores.

game_tree = [
    [3, 5],
    [2, 9]
]

def minimax(tree, maximizing):
    if all(not isinstance(x, list) for x in tree):
        return max(tree) if maximizing else min(tree)

    if maximizing:
        best = float('-inf')
        for child in tree:
            if isinstance(child, list):
                value = minimax(child, False)
            else:
                value = child
            best = max(best, value)
        return best

    best = float('inf')
    for child in tree:
        if isinstance(child, list):
            value = minimax(child, True)
        else:
            value = child
        best = min(best, value)
    return best

# Evaluate each possible first move for MAX.
values = []

for child in game_tree:
    value = minimax(child, False)
    values.append(value)
    print("Move value:", value)

best_move = values.index(max(values)) + 1

print("Best move: Move", best_move)
print("Best guaranteed value:", max(values))
