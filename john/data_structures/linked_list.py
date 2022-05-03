
class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

  def setNext(self, next):
    self.next = next
    return next
  
class LinkedList:
  def __init__(self, head, last):
    self.head = head
    self.last = last

  def print(self):
    current = head
    while (current != None):
      print(current.value)
      current = current.next

head = None
last = None

for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
  if (head == None):
    head = Node(i)
    last = head
  else:
    last = last.setNext(Node(i))


list = LinkedList(head, last)

list.print()