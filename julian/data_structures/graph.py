from random import randint


class Node:

    def __init__(self, data):

        self.data = data
        self.adjacent_nodes = []
        self.visited = False

#TODO: The nodes can be connected to themselves and can make multiple connections to the same node.
# this is not desired lol.
def gen_undirected_ternary_graph(size=10):

    # gen some nodes
    nodes = []

    for i in range(size):
        nodes.append(Node(randint(0, 100)))

    # connect em all up
    for node in nodes:

        # keep trying to hook node up if it isn't fully connected yet
        while len(node.adjacent_nodes) < 3:

            # try a random node:
            random_node_index = randint(0, size - 1)
            # if random node also isn't fully connected, form a connection.
            if len(nodes[random_node_index].adjacent_nodes) < 3:
                node.adjacent_nodes.append(nodes[random_node_index])
                nodes[random_node_index].adjacent_nodes.append(node)

    return nodes


def print_undirected_ternary_graph(graph):

    for node in graph:
        print(f"Node addr:{id(node)}")
        print(id(node.adjacent_nodes[0]))
        print(id(node.adjacent_nodes[1]))
        print(id(node.adjacent_nodes[2]))
        print("\n")

graph = gen_undirected_ternary_graph()
print_undirected_ternary_graph(graph)
