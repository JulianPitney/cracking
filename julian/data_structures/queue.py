
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










