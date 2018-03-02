from model import *
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import collections

m_values = [1, 2, 3, 4, 5]

colors = ['red', 'blue', 'green', 'purple', 'orange']

edge_lists = []

patches = []

plt.figure()

for m, c in zip(m_values, colors):
    edge_list, node_list = build_network(
        starting_node=m + 1, new_edges=m, run_time=100000)
    distributions = []
    edge_counter = collections.Counter(edge_list)
    for node in node_list:
        distributions.append(edge_counter[node])
    distribution_counter = collections.Counter(distributions)
    frequencies = []
    for i in range(max(distributions)):
        frequencies.append((i, distribution_counter[i]))
    patches.append(mpatches.Patch(color=c, label='m=' + str(m)))
    total_nodes = sum([row[1] for row in frequencies])
    plt.plot([row[0] for row in frequencies], [(row[1] / total_nodes) * 100 for row in frequencies], color=c)


plt.xlabel('Number of Connections (k)')
plt.ylabel('Percent of Nodes (%)')

plt.legend(handles=patches)

plt.savefig("degree_distribution.png")
