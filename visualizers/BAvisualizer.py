import networkx as nx
import matplotlib.pyplot as plt

# Define the number of nodes and m
n = 50
m = 2

# Create an initial complete graph with m nodes
G = nx.complete_graph(m)

# Visualize the initial graph
pos = nx.spring_layout(G)
plt.figure(figsize=(5,5))
nx.draw(G, pos=pos, with_labels=True)
plt.title('Initial Complete Graph')

# Apply the BA model to add n-m nodes
for i in range(m, n):
    # Calculate the degree distribution of the current graph
    degree_seq = [d for n, d in G.degree()]

    # Choose m nodes to attach to
    nodes = list(range(i))
    chosen = nx.utils.pairwise(nodes, degree_seq)
    targets, degrees = zip(*chosen)

    # Add the new node with edges to the chosen nodes
    G.add_node(i)
    edges = [(i, t) for t in targets]
    G.add_edges_from(edges)

    # Visualize the current graph
    pos = nx.spring_layout(G)
    plt.figure(figsize=(5,5))
    nx.draw(G, pos=pos, with_labels=True, node_color='blue', node_size=100)
    nx.draw_networkx_nodes(G, pos=pos, nodelist=[i], node_color='red', node_size=200)
    plt.title(f'Iteration {i-m+1}')

plt.show()
