import networkx as nx
import matplotlib.pyplot as plt

# Create Graph
G = nx.Graph()

# Add Nodes
G.add_node("Student")
G.add_node("Artificial Intelligence")
G.add_node("Computer Science")

# Add Relationships
G.add_edge("Student", "Artificial Intelligence")
G.add_edge("Artificial Intelligence", "Computer Science")

# Draw Graph
nx.draw(G, with_labels=True)

plt.show()
