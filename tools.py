import networkx as nx

def approximate_local_clustering_coefficient(G, node):
    neighbors = G.neighbors(node)
    k = len(neighbors)
    if k < 2:
        return 0
    edges = 0
    for i, u in enumerate(neighbors):
        for v in neighbors[i+1:]:
            if G.has_edge(u, v):
                edges += 1
    return edges / (k * (k - 1) / 2)

# Example usage:
G = nx.karate_club_graph()
node = 0
clustering_coefficient = approximate_local_clustering_coefficient(G, node)
print(f"The local clustering coefficient of node {node} is approximately {clustering_coefficient}")
