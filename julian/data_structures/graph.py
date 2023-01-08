from random import randint


class Node:

    def __init__(self, data):

        self.data = data
        self.adjacent_nodes = []


def gen_directed_graph(size=10):

    # gen some nodes
    nodes = []

    for i in range(0, size):
        nodes.append(Node(randint(0, 100)))

    # make random connections between the nodes, following some constraints:
    # 1. A node may not connect to itself
    # 2. An edge connecting any given source and target node may only occur once.

    # gen connections for each node
    connections = []
    for i in range(0, size):

        num_connections = randint(1, 3)
        x = 0
        while x < num_connections:

            connection = (i, randint(0, size - 1))
            if connection == (i, i):
                continue
            elif connection in connections:
                continue
            else:
                connections.append(connection)
                x += 1

    # form connections using generated connections list
    for connection in connections:
        source = nodes[connection[0]]
        target = nodes[connection[1]]

        source.adjacent_nodes.append(target)

    return nodes


nodes = gen_directed_graph()


for i in range(0, 1000):
    nodes = gen_directed_graph()

#for node in nodes:
#    print(f"Node: {id(node)}")
#    for anode in node.adjacent_nodes:
#        print(f"Adjacent Node: {id(anode)}")
#    print("\n")
