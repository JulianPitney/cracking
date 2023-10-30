from random import randint
from queue import Queue

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


def gen_sorted_integer_list(size=10):

    integers = [randint(0, 2**8) for _ in range(0, size)]
    integers.sort()
    return integers



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


def bfs(root: Node, target: Node, visited_nodes: dict):

    queue = Queue()
    visited_nodes[root] = True
    queue.put(root)

    while not queue.empty():
        node = queue.get()

        if node == target:
            return True

        for adjacent_node in node.adjacent_nodes:
            if not adjacent_node in visited_nodes:
                visited_nodes[adjacent_node] = True
                queue.put(adjacent_node)

    return False

def gen_bst(sorted_input_list: list):
    
    bst = None

    for x in list:
        node = Node(x):



def four_point_one():

    graph = gen_directed_graph(size=10)
    print_adjacency_list(graph)

    while 1:
        i1 = int(input("Enter root index: "))
        i2 = int(input("Enter target index: "))
        print(f"BFS Route Found: {bfs(graph[i1], graph[i2], {})}")
        print(f"DFS Route Found: {dfs(graph[i1], graph[i2], {})}")


def four_point_two():
    integers = gen_sorted_integer_list()
    print(integers)



#four_point_one()
four_point_two()
