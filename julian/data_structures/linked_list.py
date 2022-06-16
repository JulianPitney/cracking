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

    @staticmethod
    def sum_lists(list1, list2):

        sum = 0
        multiplier = 1

        while list1 is not None:
            sum += (multiplier * list1.data)
            multiplier *= 10
            list1 = list1.next

        multiplier = 1
        while list2 is not None:
            sum += (multiplier * list2.data)
            multiplier *= 10
            list2 = list2.next

        # This is the math way of getting digits from an int. An easier and
        # probably more performant way is to just convert the int to a string
        # and read the digits using string indexes then convert them back to ints.
        previous_divisor = 1
        divisor = 10
        digit = (sum % divisor) / previous_divisor
        sum -= digit
        divisor *= 10
        previous_divisor *= 10
        output_head = Node(int(digit))
        output_tail = output_head
        temp_node = output_head

        while sum > 0:

            digit = (sum % divisor)
            sum -= digit
            digit /= previous_divisor
            divisor *= 10
            previous_divisor *= 10
            temp_node.next = Node(int(digit))
            temp_node = temp_node.next
            output_tail = temp_node

        return output_head, output_tail




head1 = Node(7)
l1 = SinglyLinkedList(head1, None)
for i in range(0, 3):
    l1.append_to_tail(random.randint(0, 9))
head2 = Node(5)
l2 = SinglyLinkedList(head2, None)
for i in range(0, 3):
    l2.append_to_tail(random.randint(0, 9))

print("l1")
l1.print_list()
print("l2")
l2.print_list()

l3_head, l3_tail = SinglyLinkedList.sum_lists(l1.head, l2.head)
l3 = SinglyLinkedList(Node(0), None)
l3.head = l3_head
l3.tail = l3_tail
print("summed list")
l3.print_list()














