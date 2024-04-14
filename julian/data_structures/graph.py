from random import randint
from queue import Queue
from dataclasses import dataclass

class Node:

    def __init__(self, data):

        self.data = data
        self.adjacent_nodes = []

class BSTNode (Node):

    def __init__(self, data):
        super().__init__(data)
        self.left  = None
        self.right = None


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

    if not sorted_input_list:
        return None

    middle_index = len(sorted_input_list) // 2
    root = BSTNode(sorted_input_list[middle_index])

    root.left = gen_bst(sorted_input_list[:middle_index])
    root.right = gen_bst(sorted_input_list[middle_index + 1:])
    return root




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
    bst = gen_bst(integers)


# Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth.
# e.g if you have a tree with depth D, you'll have D linked lists.
def four_point_three(root_node: BSTNode = None):
    

    # List of node lists
    linked_lists = [[]]
    # Queue for level order traversal
    traversal_queue = []

    # Wrapper to attach depth information to nodes
    class DepthInfoNode:

        def __init__(self, node: BSTNode, depth: int):
            self.node = node
            self.depth = depth

    root_node = DepthInfoNode(root_node, 0)
    traversal_queue.append(root_node)

    while traversal_queue:

        node = traversal_queue.pop(0)

        
        # If no list exists yet for this depth, create it.
        if node.depth > len(linked_lists) - 1:
            linked_lists.append([])

        linked_lists[node.depth].append(node.node.data)

        # Wrap left and right child nodes and enqueue them.
        if node.node.left is not None:
            left_node = DepthInfoNode(node.node.left, node.depth + 1)
            traversal_queue.append(left_node)
        if node.node.right is not None:
            right_node = DepthInfoNode(node.node.right, node.depth + 1)
            traversal_queue.append(right_node)


    return linked_lists
# 1. Traverse entire BST 1 level at a time 
#     - level order traversal using queue 
# 2. Wrap nodes in struct that holds 
# 2. For each node, add to linked list at index equal to depth of node
# 3. If linked list at index does not exist, create it
# 4. Error handling
# 5. Unit testing
# 6. Docstring

#four_point_one()
#four_point_two()

integers = gen_sorted_integer_list()
print(integers)
root_node = gen_bst(integers)
linked_lists = four_point_three(root_node)
for l in linked_lists:
    print(l)