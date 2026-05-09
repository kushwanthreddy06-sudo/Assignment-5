import math

MAX = 1000
MIN = -1000

def alphabeta(depth, nodeIndex, maximizingPlayer,
              values, alpha, beta, height):

    # Base Case
    if depth == height:
        return values[nodeIndex]

    # Maximizing Player
    if maximizingPlayer:

        best = MIN

        for i in range(2):

            val = alphabeta(depth + 1,
                            nodeIndex * 2 + i,
                            False, values,
                            alpha, beta, height)

            best = max(best, val)
            alpha = max(alpha, best)

            # Alpha Beta Pruning
            if beta <= alpha:
                break

        return best

    # Minimizing Player
    else:

        best = MAX

        for i in range(2):

            val = alphabeta(depth + 1,
                            nodeIndex * 2 + i,
                            True, values,
                            alpha, beta, height)

            best = min(best, val)
            beta = min(beta, best)

            # Alpha Beta Pruning
            if beta <= alpha:
                break

        return best


# Driver Code
values = [3, 5, 6, 9, 1, 2, 0, -1]

height = int(math.log2(len(values)))

result = alphabeta(0, 0, True,
                   values, MIN, MAX, height)

print("Optimal Value is :", result)
