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


head = Node(10)
l1 = SinglyLinkedList(head, None)
for i in range(0, 9):
    l1.append_to_tail(random.randint(0, 10))
l1.print_list()
print(l1.get_nth_last_element(1))











