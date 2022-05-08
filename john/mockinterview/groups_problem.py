

# True = Grass -- Veritcally or horizontall adjacent patches signify a single 'group'
# False = Dirt

matrix = [[True, False, True, True], [False, True, False, False], [False, True, False, False]]

matrix2 = [[True, False, True, False], [False, False, True, False], [False, True, True, True], [False, False, True, False]]


# Horizontally adjacent = next at same index == True or next index True

def getFarms(iterable):

  def evaluateFarmFromNode(idxA, idxB):

    iterable[idxA][idxB] = False

    rightValueHorizontal = False
    leftValueHorizontal = False
    downValueVertical = False
    upValueVertical = False

    try:
      rightValueHorizontal = iterable[idxA][max(0, idxB + 1)]
    except IndexError:
      pass

    try:
      leftValueHorizontal = iterable[idxA][max(0, idxB - 1)]
    except IndexError:
      pass

    try:
      downValueVertical = iterable[max(0, idxA + 1)][idxB]
    except IndexError:
      pass

    try:
      upValueVertical = iterable[max(0, idxA - 1)][idxB]
    except IndexError:
      pass

    # Horizontal
    if (rightValueHorizontal == True):
      evaluateFarmFromNode(idxA, idxB + 1)

    if (leftValueHorizontal == True):
      evaluateFarmFromNode(idxA, idxB - 1)

    # Vertical
    if (downValueVertical == True):
      evaluateFarmFromNode(idxA + 1, idxB)

    if (upValueVertical == True):
      evaluateFarmFromNode(idxA - 1, idxB)

  fieldMap = dict()

  # Map each node to the dictionary

  farmCount = 0

  for xRowIndex, xRow in enumerate(iterable):
    for iColIndex, iCol in enumerate(xRow):
      if (iCol == True):
        farmCount = farmCount + 1
        evaluateFarmFromNode(xRowIndex, iColIndex)

  print(farmCount)

getFarms(matrix)

getFarms(matrix2)
