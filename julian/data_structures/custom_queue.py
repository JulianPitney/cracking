# 3.4 - Queue Via Stacks
# Queue with stacks is a shit idea when we could just use a double linked list
# but let's keep with the spirit of the question.
# We can do it with 1 stack with dequeue being O(n).
# Can't think of a way to beat O(n) dequeue using another stack...

class QueueNode:

    def __init__(self, data):
        self.next = None
        self.data = data


class MyQueue:

    def __init__(self, head):

        self.top = head
        self.shortcut_nodes = None

    def print_queue(self):

        temp = self.top
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def enqueue(self, data):

        node = QueueNode(data)
        node.next = self.top
        self.top = node

    # This is shit cause dequeue shouldn't be O(n)
    #
    def dequeue(self):

        if self.top is None:
            return None

        temp1 = self.top
        temp2 = self.top.next

        # 1 item in the queue
        if temp2 is None:
            self.top = None
            return temp1

        while temp2 is not None:

            if temp2.next is None:
                temp1.next = None
                return temp2
            else:
                temp1 = temp2
                temp2 = temp2.next

"""
init_node = QueueNode(10)
q1 = MyQueue(init_node)
q1.enqueue("aids")
q1.enqueue("bees")
q1.enqueue(-15)
q1.print_queue()
print("\n\n")
q1.dequeue()
q1.dequeue()
q1.dequeue()
q1.dequeue()
q1.dequeue()
q1.print_queue()
"""

# 3.6 - Animal Shelter

class AnimalNode:

    def __init__(self, animal_type):
        self.data = animal_type
        self.next = None
        self.prev = None


class AnimalQueue:

    def __init__(self, head, tail):

        self.head = head
        self.tail = tail

    def print_queue(self):

        if self.head is None:
            print("Empty Queue")
        else:
            iter_node = self.head
            while iter_node is not None:
                print(f'{iter_node.data}')
                iter_node = iter_node.next


    def enqueue(self, animal):

        node = AnimalNode(animal)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def dequeue_any(self):

        if self.head is None:
            print("Queue is empty")
            return None
        elif self.head.next is None:
            temp = self.head
            self.tail = None
            self.head = None
            return temp
        else:
            temp = self.tail
            self.tail.prev.next = None
            self.tail = self.tail.prev
            return temp

    # this is so ugly but whatever
    def dequeue_animal(self, animal_type):

        if self.head is None:
            print("queue is empty")
        elif self.head.next is None:

            if self.head.data == animal_type:
                temp = self.head
                self.head = None
                self.tail = None
                return temp
            else:
                print(f"no {animal_type}s in the shelter")
        else:
            iter_node = self.tail
            while iter_node is not None:
                if iter_node.data == animal_type:
                    if iter_node is self.head:
                        iter_node.next.prev = None
                        self.head = iter_node.next
                    elif iter_node is self.tail:
                        iter_node.prev.next = None
                        self.tail = iter_node.prev
                    else:
                        iter_node.next.prev = iter_node.prev
                        iter_node.prev.next = iter_node.next
                    return iter_node
                else:
                    iter_node = iter_node.prev


aminal = AnimalNode("cat")
test = AnimalQueue(aminal, aminal)
test.enqueue("dog")
test.enqueue("cat")
test.print_queue()
print('\n\n')
test.dequeue_animal('cat')
test.dequeue_animal('cat')
test.dequeue_animal('cat')
test.dequeue_animal('dog')
test.dequeue_animal('dog')
test.print_queue()
print('\n\n')
test.enqueue('cat')
test.enqueue('cat')
test.enqueue('dog')
test.print_queue()
test.dequeue_any()
test.dequeue_animal('dog')
print('\n\n')
test.print_queue()




