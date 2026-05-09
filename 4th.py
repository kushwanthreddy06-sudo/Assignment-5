import random

class Node:

    def __init__(self):
        self.visits = 0
        self.score = 0

def monte_carlo_tree_search(iterations):

    root = Node()

    for i in range(iterations):

        # Simulated Random Reward
        reward = random.randint(1, 10)

        root.visits += 1
        root.score += reward

    average_score = root.score / root.visits

    return average_score


# Driver Code
result = monte_carlo_tree_search(1000)

print("Average Score :", result)
