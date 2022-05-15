class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    self.prev = None

  def setNext(self, next):
    self.next = next
    next.prev = self
    return next
  
class LinkedList:
  def __init__(self, head):
    self.head = head
    self.last = None

  # Not the same as a book because I'm an absolute vandal
  def appendToTail(self, value):
    node = Node(value)
    if (self.head == None):
      self.head = node
    elif (self.last == None):
        self.head.next = node
        node.prev = self.head
        self.last = node
    else:
      node.prev = self.last
      self.last.next = node
      self.last = node

  def appendToHead(self, val):
    newNode = Node(val)
    newNode.next = self.head
    self.head = newNode

  def print(self):
    current = self.head
    if (current == None):
      print('Empty List')
    else:
      while (current != None):
        print(current.value)
        current = current.next

  def removeNode(self, node):
    if (node == self.head):
      newHead = self.head.next
      del newHead.prev
      self.head = newHead
    elif (node == self.last):
      newLast = self.last.prev
      del newLast.next
      self.last = newLast
    elif (node.next != None and node.prev != None  ):
      node.prev.next = node.next
      node.next.prev = node.prev
      
  def removeDuplicates(self):
    bufferSet = set()

    # Without a buffer, we would need to loop N amount of times within N...O(N^2)
    current = self.head
    while (current != None):
      if (current.value in bufferSet):
        newNext = current.next
        self.removeNode(current)
        current = newNext
      else:
        bufferSet.add(current.value)
        current = current.next

  ## Constraint:
  #  Designed for Singly-linked lists
  def nthToLast(self, n):

    current = self.head
    i = 1
    shiftedN = current # Hang back by N
    while (current != None):

      #after we achieve the nTh lower bound...
      if (i > n):
        shiftedN = shiftedN.next
      current = current.next
      i = i + 1

    return shiftedN if i >= n else None

  def partition(self, xVal):

    leftList = LinkedList(None)
    rightList = LinkedList(None)

    current = self.head
    while (current != None):
      if (current.value < xVal):
        leftList.appendToTail(current.value)
      elif (current.value >= xVal):
        rightList.appendToTail(current.value)
      current = current.next

    # Merge lists
    leftList.last.next = rightList.head
    leftList.last = rightList.last
    self.head = leftList.head
    self.last = leftList.last

  def toIntFromEnd(self):
    intStr = ''
    current = self.head
    while (current != None):
      intStr = str(current.value) + intStr
      current = current.next
    return int(intStr)

  @staticmethod
  def sum(listA, listB):
    intA = listA.toIntFromEnd()
    intB = listB.toIntFromEnd()

    newList = LinkedList(None)

    result = str(intA + intB)

    print(f'A: {intA}, B: {intB}, Result: {result}')
  
    for i in range(1, len(result) + 1):
      newList.appendToTail(int(result[-i]))
    
    return newList

  @staticmethod
  def listFromArray(arr):
    nHead = None
    nLast = None

    for i in arr:
      if (nHead == None):
        nHead = Node(i)
        nLast = nHead
      else:
        nLast = nLast.setNext(Node(i))

    return LinkedList(nHead)
    

list = LinkedList.listFromArray([1, 2, 9, 3, 4, 5, 5, 6, 7, 8, 9, 10])

print('Raw')
list.print()

list.removeDuplicates()

print('\nDuplicates Removed')
list.print()

print('\nnthTolast (4)')
nthToLastList = LinkedList(list.nthToLast(4))
nthToLastList.print()

print('\nnthTolast (100)')
nthToLastList = LinkedList(list.nthToLast(100))
nthToLastList.print()

print('\nPartition around 5')

lsitToPartition = LinkedList.listFromArray([3, 5, 8, 5, 10, 2, 1])
lsitToPartition.partition(5)
lsitToPartition.print()

print('\nPartition around 5 (again)')

lsitToPartition = LinkedList.listFromArray([1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10])
lsitToPartition.partition(5)
lsitToPartition.print()

print('\n Sum Lists')
listA = LinkedList.listFromArray([7, 1, 6])
listB = LinkedList.listFromArray([5, 9, 2])

newList = LinkedList.sum(listA, listB)
newList.print()