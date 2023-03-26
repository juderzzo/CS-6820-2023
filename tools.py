import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import powerlaw
# import scipy.stats as stats
# negative regression
def neg_exp_fit(G):
    # degree plotting
    degrees = [degree for node, degree in G.degree()]
    plt.hist(np.log(degrees), bins=50, density=True, alpha=0.5, color='blue')

    # degree model fitting

    degree_dist = nx.degree_histogram(G)
    total_nodes = G.number_of_nodes()
    prob_dist = [count / total_nodes for count in degree_dist]

    # Fit the data to an inverse power law model
    #
    fit = powerlaw.Fit(degree_dist)
    fit.plot_pdf(color='r', linewidth=2)

    # Print the regression results

    print('Alpha:', fit.alpha)
    print('xmin:', fit.xmin)

    # Add labels and titles
    plt.xlabel('Log(Degree)')
    plt.ylabel('Frequency')
    plt.title('Degree Distribution')

    plt.show()


def approximate_local_clustering_coefficient(G, node):
    neighbors = tuple(G.neighbors(node))

    k = len(neighbors)
    if k < 2:
        return 0
    edges = 0
    for i, u in enumerate(neighbors):
        for v in neighbors[i+1:]:
            if G.has_edge(u, v):
                edges += 1
    return edges / (k * (k - 1) / 2)


def get_local_clustering_coefficient_dist(G, plot=False):
    ans = []
    # get all the local clustering coefficients
    for node in G.nodes:
        local = approximate_local_clustering_coefficient(G, node)
        print(local)
        ans.append(local)

    if(plot):
        plt.hist(ans)
        plt.show()
    return ans




# Example usage:
