import networkx as nx
import matplotlib.pyplot as plt
from functions import *


def main(starting_node=3, run_time=200, new_edges=2):
    G = initialize()
    G.add_nodes_from(range(starting_node))
    edge_list = []
    for n in G.nodes():
        for k in G.neighbors(n):
            edge_list.append(n)
    for i in range(starting_node, run_time + starting_node):
        edges = increment(G, i, edge_list, new_edges)
        for m in range(new_edges):
            edge_list.append(i)
        for edge in edges:
            edge_list.append(edge)
    plt.figure()
    nx.draw(G, with_labels=True)
    plt.show()


if __name__ == "__main__":
    main()

