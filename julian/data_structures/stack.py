import math

# 3.1 - Three in One


class ThreeInOne:

    def __init__(self, arr_size):

        assert (arr_size >= 3), "Array must be size 3 or greater!"

        self.arr = [None] * arr_size
        self.s1_start = 0
        self.s1_top = self.s1_start
        self.s2_start = math.floor(arr_size * (1 / 3))
        self.s2_top = self.s2_start
        self.s3_start = math.floor(arr_size * (2 / 3))
        self.s3_top = self.s3_start

    def push_s1(self, data):

        if self.s1_start == self.s1_top and self.arr[self.s1_start] is None:
            self.arr[self.s1_start] = data
            return True

        elif self.s1_top >= self.s2_start - 1:
            print("S1 is full. Aborting push!")
            return False

        self.s1_top += 1
        self.arr[self.s1_top] = data
        return True

    def push_s2(self, data):

        if self.s2_start == self.s2_top and self.arr[self.s2_start] is None:
            self.arr[self.s2_start] = data
            return True

        if self.s2_top >= self.s3_start - 1:
            print("S2 is full. Aborting push!")
            return False

        self.s2_top += 1
        self.arr[self.s2_top] = data
        return True

    def push_s3(self, data):

        if self.s3_start == self.s3_top and self.arr[self.s3_start] is None:
            self.arr[self.s3_start] = data
            return True

        if self.s3_top >= len(self.arr) - 1:
            print("S3 is full. Aborting push!")
            return False

        self.s3_top += 1
        self.arr[self.s3_top] = data
        return True

'''
test = ThreeInOne(3)
print(test.arr)
test.push_s1("eggs")
print(test.arr)
test.push_s2("bagels")
print(test.arr)
test.push_s2("snakes")
print(test.arr)
test.push_s3("lemons")
print(test.arr)
test.push_s3("flies")
print(test.arr)
'''

# 3.2 - Stack Min

class StackNode:

    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.min_substack = self


class Stack:

    def __init__(self, top=None):
        self.top = top
        self.min_node = top

    def print_stack(self):
        temp = self.top

        while temp is not None:
            print(temp.data)
            temp = temp.next

    def push(self, data):

        node = StackNode(data)

        if self.top is None:
            self.top = node
            node.min_substack = node
            self.min_node = node
            return True

        node.next = self.top

        if self.top.min_substack.data > node.data:
            node.min_substack = node
            self.min_node = node
        else:
            node.min_substack = self.top.min_substack

        self.top = node

        return True

    def pop(self):

        if self.top is None:
            return None

        if self.top.next is None:
            self.min_node = None
            temp = self.top
            self.top = None
            return temp

        if self.min_node == self.top:
            self.min_node = self.top.next.min_substack

        temp = self.top
        self.top = self.top.next
        return temp

    def get_min(self):
        return self.min_node


node1 = StackNode(10)
s1 = Stack(node1)
s1.push(5)
s1.push(11)
s1.push(0)
s1.push(900)
s1.push(-1000)
s1.pop()
s1.pop()
s1.pop()
s1.pop()
s1.pop()
s1.pop()
s1.print_stack()
if s1.min_node is not None:
    print(f'min: {s1.min_node.data}')






