import networkx as nx
import random


def increment(graph, node, weights, m=2):
    """
    Adds a new node with m connections to other random nodes.
    The graph must have at least m nodes already in it.
    """
    if len(graph.nodes()) < m:
        raise ValueError(
            'Must have at least as many existing nodes as edges added!')
    random.seed()
    graph.add_node(node)
    new_edges = random.sample(weights, m)
    graph.add_edges_from([(node, n) for n in new_edges])
    return new_edges

def initialize(n=3):
    graph = nx.Graph()
    for x in range(n):
        graph.add_node(n)
    for x in range(n):
        for y in range(n):
            if y != x:
                graph.add_edge(x, y)
    return graph
