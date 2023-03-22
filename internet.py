
import networkx as nx
import matplotlib.pyplot as plt
# Open the file and read the data
with open('data/as20000102.txt', 'r') as f:
    data = f.read().splitlines()

# Extract the number of nodes and edges from the header
print(data[2].split())
num_nodes = int(data[2].split()[2])
num_edges = int(data[2].split()[4])

# Create an empty graph
G = nx.Graph()

# Add the nodes to the graph
for i in range(num_nodes):
    G.add_node(i)

# Add the edges to the graph
for line in data[4:]:
    nodes = line.split()
    node1 = int(nodes[0])
    node2 = int(nodes[1])
    G.add_edge(node1, node2)

# Print some information about the graph
print(f'Number of nodes: {G.number_of_nodes()}')
print(f'Number of edges: {G.number_of_edges()}')

# Draw the graph (optional)
nx.draw(G, with_labels=True)
plt.show()
#pretty ugly