import math

def heuristic(node):
    return node

def heuristic_alphabeta(depth, nodeIndex,
                        maximizingPlayer,
                        values, alpha,
                        beta, maxDepth):

    if depth == maxDepth:
        return heuristic(values[nodeIndex])

    if maximizingPlayer:

        best = -math.inf

        for i in range(2):

            val = heuristic_alphabeta(
                depth + 1,
                nodeIndex * 2 + i,
                False,
                values,
                alpha,
                beta,
                maxDepth
            )

            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:

        best = math.inf

        for i in range(2):

            val = heuristic_alphabeta(
                depth + 1,
                nodeIndex * 2 + i,
                True,
                values,
                alpha,
                beta,
                maxDepth
            )

            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best


# Driver Code
values = [3, 5, 6, 9, 1, 2, 0, -1]

height = int(math.log2(len(values)))

result = heuristic_alphabeta(
    0, 0, True,
    values,
    -math.inf,
    math.inf,
    height
)

print("Optimal Value is :", result)
