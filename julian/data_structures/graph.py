from random import randint
from queue import Queue
from dataclasses import dataclass

class Node:

    def __init__(self, data):

        self.data = data
        self.adjacent_nodes = []

class BTNode (Node):

    def __init__(self, data):
        super().__init__(data)
        self.left  = None
        self.right = None
        self.parent = None

    def __repr__(self):

        output = f"ID: {id(self)}\nParent: {id(self.parent)}\nLeft: {id(self.left)}\nRight: {id(self.right)}\nData: {self.data}\n"
    
        if self.left is not None:
            output += f"Left Data: {self.left.data}\n"
        if self.right is not None:
            output += f"Right Data: {self.right.data}\n"

        output = output.replace(str(id(None)), "None")
        return output
    
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
    root = BTNode(sorted_input_list[middle_index])

    root.left = gen_bst(sorted_input_list[:middle_index])
    root.right = gen_bst(sorted_input_list[middle_index + 1:])
    return root



def gen_bst_with_parent_links(sorted_input_list: list):

    if not sorted_input_list:
        return None

    middle_index = len(sorted_input_list) // 2
    root = BTNode(sorted_input_list[middle_index])

    root.left = gen_bst_with_parent_links(sorted_input_list[:middle_index])
    root.right = gen_bst_with_parent_links(sorted_input_list[middle_index + 1:])

    if root.left is not None:
        root.left.parent = root 
    if root.right is not None:
        root.right.parent = root 

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
def gen_ll_from_btree_level_order(root_node: BTNode = None):
    

    # List of node lists
    linked_lists = [[]]
    # Queue for level order traversal
    traversal_queue = []

    # Wrapper to attach depth information to nodes
    class DepthInfoNode:

        def __init__(self, node: BTNode, depth: int):
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

def four_point_three():
    integers = gen_sorted_integer_list()
    print(integers)
    root_node = gen_bst(integers)
    linked_lists = gen_ll_from_btree_level_order(root_node)
    for l in linked_lists:
        print(l)


def get_subtree_height(node: BTNode):
    
    if node is None:
        return 0
    
    lh = get_subtree_height(node.left)
    rh = get_subtree_height(node.right)
    return max(lh, rh) + 1

    
        

def is_balanced(node: BTNode):

    if node is None:
        return True
    
    balanced = abs(get_subtree_height(node.left) - get_subtree_height(node.right)) <= 1
    left_balanced = is_balanced(node.left)
    right_balanced = is_balanced(node.right)

    return (balanced and left_balanced and right_balanced)
    
    

def is_bst(root_node: BTNode) -> bool:

    if root_node is None:
        return True
    
    if root_node.left is not None:
        if root_node.left.data >= root_node.data:
            return False
        
    if root_node.right is not None:
        if root_node.right.data < root_node.data:
            return False 
        
    
    left_result = is_bst(root_node.left)
    right_result = is_bst(root_node.right)
    
    return left_result and right_result    





# 1. Write a function to calculate the height of any subtree
# 2. Recursively visit every node.
# 3. For every node -> if (height(left_subtree) - height(right_subtree)) > 1: return false
# 
#        *
#       / \
#      /   \ 
#     *     *   
#    / \   / \
#   *   * *   * 
# Implement a function to check if a binary tree is balanced. 
# For the purposes of this question a balanced tree is defined 
# to be a tree such that the heights of the two subtress of any 
# node never differ by more than one.
def four_point_four():
    root_node = gen_bst([1,2,3])
    root_node.left.left = BTNode(0)
    balanced = is_balanced(root_node)
    print(balanced)
    return balanced
    

# Implement a fuction to check if a binary tree is a binary search tree.
def four_point_five():
    # 1. A BT is a BST if for the value of every node, the left child's value is less and the right child's value is greater than or equal to. 
    # 2. Traverse the entire tree using dfs or bfs
    # 3. Check this condition for every node. Return false if the check ever fails.  

    integers = gen_sorted_integer_list()
    print(integers)
    bst_root_node = gen_bst(integers)
    bt_root_node = BTNode(0)
    bt_root_node.left = BTNode(-5)
    bt_root_node.right = BTNode(11)
    bt_root_node.left.right = BTNode(-2)
    bt_root_node.left.left = BTNode(15) # failure case
    bt_root_node.right.right = BTNode(57)
    bt_root_node.right.left = BTNode(6)

    # should be true
    print(is_bst(bst_root_node))
    # should be false
    print(is_bst(bt_root_node))




def print_btree(root_node: BTNode):

    if root_node is None:
        return None
    

    print(root_node)
    print_btree(root_node.left)
    print_btree(root_node.right)

    return None




def get_in_order_successor(node: BTNode) -> BTNode:

    if node.right is None:
        if node.parent is None:
            return None
        else:
            if node.parent.left is node:
                return node.parent    
            elif node.parent.parent is not None and node.parent.parent.left is node.parent:
                return node.parent.parent 
            else:
                return None
    else:
        node = node.right
        while node.left is not None:
            node = node.left
        return node 


def test_in_order_successor_with_dft(root_node: BTNode):

    if root_node is None:
        return None
    
    print("\n\n\nNode: \n")
    print(root_node)
    print("Successor: \n")
    print(get_in_order_successor(root_node))
    print("\n\n\n")
    test_in_order_successor_with_dft(root_node.left)
    test_in_order_successor_with_dft(root_node.right)

# Write an algorithm to find the "next" node (i.e., in-order successor) of a given
# node in a binary search tree. You may assume that each node has a link to it's parent.
def four_point_six():
    integers = gen_sorted_integer_list()
    print(integers)
    bst_root_node = gen_bst_with_parent_links(integers)
    print_btree(bst_root_node)
    print("------------------------------------------------------------------------------------------")
    test_in_order_successor_with_dft(bst_root_node)
    



# You are given a list of projects and a list of dependencies (which is a list of pairs of projects, where the second project is dependent
# on the first project). All of a project's dependencies must be built before the project is. Find a build order that will allow the projects to 
# be built. If there is no valid build order, return an error.
def four_point_seven():
    pass 

# Design an algorithm and write code to find the first common acestor of two nodes in a binary tree.
# Avoid storing additional nodes in a data structure. NOTE: This is not necessarily a binary search tree. 
def four_point_eight():
    pass

# A binary search tree was created by traversing through an array from left to right
# and inserting each element. Given a binary search tree with distinct elements, print all possible
# arrays that could have led to this tree. 
def four_point_nine():
    pass 

# T1 and T2 are two very large binary trees, with T1 much bigger than T2. Create an algorithm to determine if T2 is a subtree of T1.
# A tree T2 is a subtree of T1 is there exists a node <n> in T1 such that the subtree of n is identical to T2.
# That is, if you cut off the tree at node n, the two trees would be identical.
def four_point_ten():
    pass 

# You are implementing a binary tree class from scratch which, in addition to insert, find, and delete, has a method getRandomNode()
# which returns a random node from the tree. All nodes should be equally likely to be chosen. Design and implement an algorithm
# for getRandomNode, and explain how you would implement the rest of the methods.
def four_point_eleven():
    pass 

# You are given a binary tree in which each node contains an integer value (which might be positive or negative)
# Design an algorithm to count the number of paths that sum to a given value. The path does not  need to start 
# or end at the root or a leaf, but it must go downwards (traveling) only from parents nodes to child nodes. 
def four_point_twelve():
    pass 




#four_point_one()
#four_point_two()
#four_point_three()
#four_point_four()
#four_point_five()
four_point_six()
print