import matplotlib.pyplot as plt
import networkx as nx
import tools
from os import listdir
import os
from os.path import isfile, join


OUTFILE = "output.csv"

def createGraph(file):
# Open the file and read the data
    with open(file, 'r') as f:
        data = f.read().splitlines()

    # Extract the number of nodes and edges from the header
    num_nodes = int(data[2].split()[1].split(":")[1])
    #num_nodes = int(data[2].split()[2])
    num_edges = int(data[2].split()[3])

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
    
    print(f"size of graph: {G.number_of_nodes()}")
    # get largest connected component
    Gcc = sorted(nx.connected_components(G), key=len, reverse=True)
    G0 = G.subgraph(Gcc[0])
    print(f"new size: {G0.number_of_nodes()}")

    return G0

def addMetricsCSV(graph, year, month, day):
    clustering = tools.global_clustering_coefficient(graph)
    print('clustering')
    expansion = tools.approx_expansion(graph)
    print("expansion")
    with open(OUTFILE, "a") as out:
        out.write(f"{year},{month},{day},{graph.number_of_nodes()}{clustering},{expansion}\n")


print(os.getcwd())
files = [f for f in listdir("data/") if isfile(join("data", f))]
files = [f for f in files if f.endswith(".txt")]


with open(OUTFILE, "a") as out:
    out.write("year,month,day,nodes,clustering,expansion\n")

for file in files:
    year = file[2:6]
    month = file[6:8]
    day = file[8:10]
    graph = createGraph('data/' + file)
    addMetricsCSV(graph, year, month, day)
    print(f"added file {file}")


# Print some information about the graph
# print(f'Number of nodes: {G.number_of_nodes()}')
# print(f'Number of edges: {G.number_of_edges()}')

# tools.get_local_clustering_coefficient_dist(G, plot=True)
# print(tools.global_clustering_coefficient(G))


