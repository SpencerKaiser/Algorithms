import networkx as nx
import matplotlib.pyplot as plt
import operator
import copy

total_set_size = 0


def main():
	# Create graph
	num_nodes = 2000
	G = nx.random_geometric_graph(num_nodes, 0.0808)
	original_graph = copy.deepcopy(G)
	# print "Graph Created"

	# Call recursive function with node data
	# print "Starting Recursion"
	mis = create_mis(G, [] )
	global total_set_size 
	total_set_size += len(mis)
	print len(mis)
	# print "Total Set Size: %d" % total_set_size
	# print mis

	# Creating figure
	plt.figure(figsize=(10,10))
	pos = nx.get_node_attributes(original_graph,'pos')

	# Draw original graph
	nx.draw_networkx_edges(original_graph, pos)
	nx.draw_networkx_nodes(original_graph, pos, node_color='w')
	
	plt.savefig('original_graph.png')
	
	# After drawing original graph, remove all nodes but those included in the mis
	for node in nx.nodes(original_graph):
		if node not in mis:
			original_graph.remove_node(node)

	# Graph the maximal independent set on top of the original graph
	pos=nx.get_node_attributes(original_graph,'pos')
	nx.draw_networkx_edges(original_graph, pos)
	nx.draw_networkx_nodes(original_graph, pos, node_color='r')
	
	pos = nx.get_node_attributes(original_graph,'pos')

	plt.savefig('mis.png')

	# Show Graph
	plt.show()


def create_mis(graph, independent_set):
	# Create data dictionary to hold node labels and their degree
	nodes = {}
	for n in nx.nodes(graph):
		nodes[n] = nx.degree(graph,n)
		# print n

	if len(nodes) == 0:
		# print "Base case reached; returning to main"
		return independent_set
	else:
		# Sort data structure by degree
		nodes = sorted(nodes.items(), key=operator.itemgetter(1))
		# print nodes

		# Select vertex of minimum degree (get the label of the pair at index 0)
		min_vertex = nodes[0][0]
		# print "Min Vertex: " + str(min_vertex)

		# Add the vertex to the independent set
		independent_set.append(min_vertex)

		# Select minimum degree vertex's neighbors
		neighbors = nx.neighbors(graph, min_vertex)
		# print neighbors
		
		# Delete its neighbors from the graph
		for n in neighbors:
			graph.remove_node(n)

		# Delete the vertex from the graph
		graph.remove_node(min_vertex)
		# print "Removed min vertex"

		return create_mis(graph, independent_set)


main()

# num_graphs = 10
# for i in range(num_graphs):
# 	main()

# # global total_set_size
# average_set_size = total_set_size / num_graphs
# print "Average Set Size: %d" % average_set_size


