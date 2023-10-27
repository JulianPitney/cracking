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
        for _ in range(0, num_connections):

            connection = (i, randint(0, size - 1))
            if connection == (i, i) or connection in connections:
                continue
            else:
                connections.append(connection)

    # form connections using generated connections list
    for connection in connections:

        source = nodes[connection[0]]
        target = nodes[connection[1]]
        source.adjacent_nodes.append(target)

    return nodes

def find_index_from_id(graph, nodeID):

    for i, node in enumerate(graph):

        if nodeID == id(node):
            return i

    return None


def print_adjacency_list(graph):

    for i, node in enumerate(graph):
        print(f"Node{i}:")
        for adjacent_node in node.adjacent_nodes:
            print(f"    -> {find_index_from_id(graph, id(adjacent_node))}")




def dfs(root: Node, target: Node, visited_nodes: dict):

    visited_nodes[root] = True

    for node in root.adjacent_nodes:

        if node == target:
            return True

        if node in visited_nodes:
            continue
        else:
            visited_nodes[node] = True
            if dfs(node, target, visited_nodes):
                return True
            
    return False        



graph = gen_directed_graph(size=10)
print_adjacency_list(graph)

while 1:
    i1 = int(input("Enter root index: "))
    i2 = int(input("Enter target index: "))
    print(f"Route Found: {dfs(graph[i1], graph[i2], {})}")
