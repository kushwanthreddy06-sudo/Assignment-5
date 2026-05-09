import math

def minimax(depth, nodeIndex, maximizingPlayer, values, height):

    # Base Case
    if depth == height:
        return values[nodeIndex]

    # Maximizing Player
    if maximizingPlayer:
        return max(
            minimax(depth + 1, nodeIndex * 2,
                    False, values, height),

            minimax(depth + 1, nodeIndex * 2 + 1,
                    False, values, height)
        )

    # Minimizing Player
    else:
        return min(
            minimax(depth + 1, nodeIndex * 2,
                    True, values, height),

            minimax(depth + 1, nodeIndex * 2 + 1,
                    True, values, height)
        )


# Driver Code
values = [3, 5, 6, 9, 1, 2, 0, -1]

height = int(math.log2(len(values)))

result = minimax(0, 0, True, values, height)

print("Optimal Value is :", result)
