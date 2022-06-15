import random


class Node:

    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data


class SinglyLinkedList:

    def __init__(self, head, tail):

        self.head = head
        self.tail = tail
        self.head.next = tail

    def print_list(self):
        n = self.head
        print(f"{n.data},", end='')
        while n.next is not None:
            n = n.next
            print(f"{n.data},", end='')
        print('')

    def append_to_tail(self, data):

        new_node = Node(data)
        temp_node = self.head

        while temp_node.next is not None:
            temp_node = temp_node.next

        temp_node.next = new_node
        self.tail = new_node

    def remove_dups(self):

        n = self.head
        seen = {n.data}

        while n.next is not None:
            if n.next.data in seen:
                n.next = n.next.next
                continue
            else:
                seen.add(n.next.data)

            if n.next is None:
                break
            else:
                n = n.next

    # return nth last element
    def get_nth_last_element(self, nth):

        list_len = 1
        n = self.head
        while n.next is not None:
            n = n.next
            list_len += 1

        n = self.head
        for i in range(0, list_len - nth):
            n = n.next

        return n.data

    def remove_middle_node(self, node):

        if node is self.head or node is self.tail:
            print("Node not in middle")
            return 0

        temp1 = node
        temp2 = node.next
        while temp2 is not None:

            temp1.data = temp2.data

            if temp2.next is None:
                break
            else:
                temp1 = temp1.next
                temp2 = temp2.next

        temp1.next = None

    def partition_around_x(self, x):

        temp = self.head
        less = []
        greater = []

        while temp is not None:

            if temp.data < x:
                less.append(temp)

            elif temp.data >= x:
                greater.append(temp)

            temp = temp.next

        less.extend(greater)

        self.head = less[0]
        temp = less[0]
        for i in range(1, len(less)):
            temp.next = less[i]
            temp = less[i]
        temp.next = None
        self.tail = temp




















head = Node(10)
l1 = SinglyLinkedList(head, None)
for i in range(0, 9):
    l1.append_to_tail(random.randint(0, 10))
l1.print_list()
l1.partition_around_x(5)
l1.print_list()












