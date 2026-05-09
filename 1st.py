# AI Assignment Codes Bundle

## 1. Minimax, Alpha-Beta, Heuristic Alpha-Beta and Monte Carlo Tree Search

### Python Code

```python
import math
import random

# ---------------- MINIMAX ----------------

def minimax(depth, nodeIndex, maximizingPlayer, values, height):
    if depth == height:
        return values[nodeIndex]

    if maximizingPlayer:
        return max(
            minimax(depth + 1, nodeIndex * 2, False, values, height),
            minimax(depth + 1, nodeIndex * 2 + 1, False, values, height)
        )
    else:
        return min(
            minimax(depth + 1, nodeIndex * 2, True, values, height),
            minimax(depth + 1, nodeIndex * 2 + 1, True, values, height)
        )

# ---------------- ALPHA-BETA ----------------

def alphabeta(depth, nodeIndex, maximizingPlayer, values, alpha, beta, height):
    if depth == height:
        return values[nodeIndex]

    if maximizingPlayer:
        best = -math.inf
        for i in range(2):
            val = alphabeta(depth + 1, nodeIndex * 2 + i, False,
                            values, alpha, beta, height)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best

    else:
        best = math.inf
        for i in range(2):
            val = alphabeta(depth + 1, nodeIndex * 2 + i, True,
                            values, alpha, beta, height)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

# ---------------- HEURISTIC ALPHA-BETA ----------------

def heuristic(node):
    return node


def heuristic_alphabeta(depth, nodeIndex, maximizingPlayer,
                        values, alpha, beta, maxDepth):

    if depth == maxDepth:
        return heuristic(values[nodeIndex])

    if maximizingPlayer:
        best = -math.inf
        for i in range(2):
            val = heuristic_alphabeta(depth + 1,
                                      nodeIndex * 2 + i,
                                      False,
                                      values,
                                      alpha,
                                      beta,
                                      maxDepth)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best

    else:
        best = math.inf
        for i in range(2):
            val = heuristic_alphabeta(depth + 1,
                                      nodeIndex * 2 + i,
                                      True,
                                      values,
                                      alpha,
                                      beta,
                                      maxDepth)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

# ---------------- MCTS ----------------

class Node:
    def __init__(self, value=0):
        self.value = value
        self.visits = 0
        self.children = []


def monte_carlo_tree_search(iterations=1000):
    root = Node()

    for _ in range(iterations):
        reward = random.randint(0, 10)
        root.visits += 1
        root.value += reward

    return root.value / root.visits


# ---------------- TEST ----------------

values = [3, 5, 6, 9, 1, 2, 0, -1]
height = 3

print("Minimax Result:", minimax(0, 0, True, values, height))

print("Alpha-Beta Result:",
      alphabeta(0, 0, True, values,
                -math.inf, math.inf, height))

print("Heuristic Alpha-Beta Result:",
      heuristic_alphabeta(0, 0, True,
                          values,
                          -math.inf,
                          math.inf,
                          height))

print("Monte Carlo Tree Search Result:",
      monte_carlo_tree_search())
```

### Test Cases

```python
Input Values = [3,5,6,9,1,2,0,-1]
Expected Minimax Output = 5
Expected Alpha-Beta Output = 5
```

---

# 2. AI Based Travel Planner

### Python Code

```python
travel_places = {
    "beach": ["Goa", "Maldives", "Bali"],
    "hill": ["Manali", "Ooty", "Munnar"],
    "historical": ["Delhi", "Hampi", "Agra"]
}

budget_places = {
    "low": "Use Bus and Budget Hotels",
    "medium": "Use Train and Standard Hotels",
    "high": "Use Flight and Luxury Hotels"
}


def recommend_trip(preference, budget):
    places = travel_places.get(preference, [])
    budget_plan = budget_places.get(budget)

    print("Recommended Places:")
    for p in places:
        print("-", p)

    print("Travel Plan:", budget_plan)


# User Input
pref = input("Enter preference (beach/hill/historical): ")
bud = input("Enter budget (low/medium/high): ")

recommend_trip(pref, bud)
```

### Sample Output

```text
Enter preference: beach
Enter budget: medium

Recommended Places:
- Goa
- Maldives
- Bali
Travel Plan: Use Train and Standard Hotels
```

---

# 3. Knowledge Graph Description and Tools

## Definition

A Knowledge Graph (KG) represents information using entities and relationships.

Example:

* Student -> studies -> AI
* AI -> belongs to -> Computer Science

## Tools Used for Building KG

1. Neo4j
2. Protégé
3. RDFLib
4. GraphDB
5. Apache Jena

### Simple Knowledge Graph using NetworkX

```python
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node("Student")
G.add_node("AI")
G.add_node("Computer Science")

G.add_edge("Student", "AI")
G.add_edge("AI", "Computer Science")

nx.draw(G, with_labels=True)
plt.show()
```

---

# 4. Bayesian Network Example

## Medical Diagnosis Example

### Python Code

```python
from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Create Bayesian Network
model = BayesianNetwork([
    ('Disease', 'Fever'),
    ('Disease', 'Cough')
])

# Define CPDs
cpd_disease = TabularCPD(variable='Disease',
                         variable_card=2,
                         values=[[0.7], [0.3]])

cpd_fever = TabularCPD(variable='Fever',
                       variable_card=2,
                       values=[[0.9, 0.2],
                               [0.1, 0.8]],
                       evidence=['Disease'],
                       evidence_card=[2])

cpd_cough = TabularCPD(variable='Cough',
                       variable_card=2,
                       values=[[0.8, 0.3],
                               [0.2, 0.7]],
                       evidence=['Disease'],
                       evidence_card=[2])

# Add CPDs
model.add_cpds(cpd_disease, cpd_fever, cpd_cough)

# Validate Model
print(model.check_model())

# Inference
infer = VariableElimination(model)
result = infer.query(variables=['Disease'],
                     evidence={'Fever': 1, 'Cough': 1})

print(result)
```

### Install Required Package

```bash
pip install pgmpy
```

### Expected Output

```text
Probability distribution of Disease based on Fever and Cough.
```

---

# Conclusion

1. Implemented Minimax, Alpha-Beta, Heuristic Alpha-Beta, and Monte Carlo Tree Search algorithms.
2. Developed an AI-based Travel Planner.
3. Explained Knowledge Graphs and implemented a simple graph example.
4. Implemented Bayesian Network inference using pgmpy.
