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

  # not intended for doubly-linked lists...
  def appendNodeToTail(self, node):
    if (self.head == None):
      self.head = list.head
    else:
      self.last.next = node
    
    # iterate down any potential attachments to the node to set the 'last'...
    current = node
    while (current != None):
      if (current.next == None):
        self.last = current
      current = current.next

  def appendToHead(self, val):
    newNode = Node(val)
    newNode.next = self.head
    self.head = newNode

  def print(self):

    concatString = ''

    current = self.head
    if (current == None):
      print('Empty List')
    else:
      while (current != None):
        concatString = concatString + str(current.value) + (',' if current.next != None else '')
        current = current.next
      print(concatString)

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

  def getNthNode(self, n):

    current = self.head
    for x in range(0, n):
      if (current == None):
        return None
      else:
        current = current.next

    return current
      
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

  # Thoughts:
  # If we're maintaining a 'length' property,
  # we could eliminate n/2 iterations across the board,
  # by checking where we are in the list on each iteration and breakin
  # at the middle.
  def isPalindrome(self):


    isPalindrome = True

    currentFromEnd = self.last
    currentFromStart = self.head

    while currentFromStart != None:

      if (currentFromStart.value != currentFromEnd.value):
        isPalindrome = False
        break

      currentFromEnd = currentFromEnd.prev
      currentFromStart = currentFromStart.next
      
    return isPalindrome



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

    nList = LinkedList(nHead)
    nList.last = nLast
    return nList

  @staticmethod
  def getIntersection(listA, listB):

    aSet = set()
    bSet = set()

    aCurrent = listA.head
    bCurrent = listB.head

    intersectedNode = None

    currPos = 0

    while (aCurrent != None or bCurrent != None):
      currPos += 1

      aRef = None
      bRef = None

      if (aCurrent != None):
        aRef = id(aCurrent)
        aSet.add(aRef)
        aCurrent = aCurrent.next

      if (bCurrent != None):
        bRef = id(bCurrent)
        bSet.add(bRef)
        bCurrent = bCurrent.next

      if (aRef != None and aRef in bSet):
        print ('\nIntersect found @ position: ' + str(currPos))
        return aCurrent.prev

      if (bRef != None and bRef in aSet):
        print ('\nIntersect found @ position: ' + str(currPos))
        return bCurrent.prev

      

list = LinkedList.listFromArray([1, 2, 9, 3, 4, 5, 5, 6, 7, 8, 9, 10])

print('Raw')
list.print()

list.removeDuplicates()

print('\nDuplicates Removed')
list.print()

print('\n-----------')
print('nTh To Last')
print('-----------')

print('\nnthTolast (4)')
nthToLastList = LinkedList(list.nthToLast(4))
nthToLastList.print()

print('\nnthTolast (100)')
nthToLastList = LinkedList(list.nthToLast(100))
nthToLastList.print()

print('\n------------')
print('Partitioning')
print('------------')

print('\nPartition around 5')

lsitToPartition = LinkedList.listFromArray([3, 5, 8, 5, 10, 2, 1])
lsitToPartition.partition(5)
lsitToPartition.print()

print('\nPartition around 5 (again)')

lsitToPartition = LinkedList.listFromArray([1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10])
lsitToPartition.partition(5)
lsitToPartition.print()

print('\n---------')
print('Sum Lists')
print('---------')
listA = LinkedList.listFromArray([7, 1, 6])
listB = LinkedList.listFromArray([5, 9, 2])

newList = LinkedList.sum(listA, listB)
newList.print()


print('\n--------------------')
print('Check for Palindrome')
print('--------------------')
nonPalindrome = LinkedList.listFromArray([1, 2, 3, 4, 5, 4, 3, 1])
palindrome = LinkedList.listFromArray([1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1])
funnyDrome = LinkedList.listFromArray([1, 2, 3, 3, 3, 3, 3, 3, 2, 1])

print('\nChecking List:')
nonPalindrome.print()
print('\nList palindrome status: ' + str(nonPalindrome.isPalindrome()))

print('\nChecking List:')
palindrome.print()
print('\nList palindrome status: ' + str(palindrome.isPalindrome()))

print('\nChecking List:')
funnyDrome.print()
print('List palindrome status: ' + str(funnyDrome.isPalindrome()))

print('\n-----------------------')
print('Check for intersections')
print('-----------------------')

intersectList = LinkedList.listFromArray([12, 23, 45, 56, 78, 90, 91, 92, 93, 94, 95])
targetIntersect = intersectList.getNthNode(2) # 56

print('\nIntersected Addr should be: ' + str(hex(id(targetIntersect))))

intersectListA = LinkedList.listFromArray([1, 2])
intersectListA.appendNodeToTail(targetIntersect)

intersectListB = LinkedList.listFromArray([9, 8, 7, 1, 5, 4, 3, 2, 3, 5, 1, 2, 3])
intersectListB.appendNodeToTail(targetIntersect)

foundIntersect = LinkedList.getIntersection(intersectListA, intersectListB)

print('\nFound intersect addr: ' + str(hex(id(foundIntersect))))