
# Alpha-Beta Pruning Algorithm

tree = [
    [3, 5],
    [2, 9]
]

def alpha_beta(node, maximizing, alpha, beta):
    if not isinstance(node, list):
        return node

    if maximizing:
        value = float('-inf')

        for child in node:
            value = max(
                value,
                alpha_beta(child, False, alpha, beta)
            )
            alpha = max(alpha, value)

            if alpha >= beta:
                print("Branch pruned")
                break

        return value

    else:
        value = float('inf')

        for child in node:
            value = min(
                value,
                alpha_beta(child, True, alpha, beta)
            )
            beta = min(beta, value)

            if beta <= alpha:
                print("Branch pruned")
                break

        return value

result = alpha_beta(
    tree, True, float('-inf'), float('inf')
)

print("Best value:", result)
