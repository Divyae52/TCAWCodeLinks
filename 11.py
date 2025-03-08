# THE COMPUTER ALWAYS WINS
# MIT PRESS
#
# CodeLink 11
# 2048
# last revised 12/25/24

# This is a full implementation of the darts strategy for playing 2048.
# Watch as the computer tilts, analyzes, and tilts again.  Does the computer
# make any painfully ridiculous moves?  Does the computer reliably reach the
# target number, 2048?


import random

def findBestMove (board):
    
    simulationCount = 50

    # test up
    testUp = tiltUp(board)
    total = 0
    for i in range(simulationCount):
        total += playRandomly(testUp)
    upAverage = total / simulationCount
    
    # test down
    testDown = tiltDown(board)
    total = 0
    for i in range(simulationCount):
        total += playRandomly(testDown)
    downAverage = total / simulationCount

    # test left
    testLeft = tiltLeft(board)
    total = 0
    for i in range(simulationCount):
        total += playRandomly(testLeft)
    leftAverage = total / simulationCount
    
    # test right
    testRight = tiltRight(board)
    total = 0
    for i in range(simulationCount):
        total += playRandomly(testRight)
    rightAverage = total / simulationCount

    scores = [upAverage, downAverage, leftAverage, rightAverage]

    # pick the best outcome
    bestResult = -999
    for counter in range(4):
        if scores[counter] > bestResult:
            bestMove = counter
            bestResult = scores[counter]

    return bestMove

    

def inDeadlock(board):
   # test to see if the board is filled
    
  upBoard = tiltUp(board)
  if board != upBoard:
    return False

  rightBoard = tiltRight(board)
  if board != rightBoard:
    return False

  downBoard = tiltDown(board)
  if board != downBoard:
    return False

  leftBoard = tiltLeft(board)
  if board != leftBoard:
    return False

  return True


def playRandomly(board):

    while not inDeadlock(board):

        # place a random 2 or 4
        board = placeRandomTile(board)      

        # randomly choose the next tilt
        chosenMove = random.randint(0, 3)

        if chosenMove == 0:
          board = tiltUp(board)

        elif chosenMove == 1:
          board = tiltDown(board)
          
        elif chosenMove == 2:
          board = tiltLeft(board)

        else:
          board = tiltRight(board)

    return scoreBoard(board)


def scoreBoard(board):
    total = 0
    for row in board:
        for col in row:
            if col != 0:
                total = total + col*col
    return total

    
def placeRandomTile(board):
    
    newBoard = [[0,0,0,0],
             [0,0,0,0],
             [0,0,0,0],
             [0,0,0,0]]

    for row in range(4):
        for col in range(4):
            newBoard[row][col] = board[row][col]

    emptySpaces = []

    for row in range(4):
        for col in range(4):
            if board[row][col] == 0:
                emptySpaces.append([row, col])

    if len(emptySpaces) > 0:
        chosenSpace = random.randint(0, len(emptySpaces)-1)
    else:
        chosenSpace = -1

    chosenValue = random.randint(1, 10)

    if chosenValue == 1:
        value = 4
    else:
        value = 2

    if chosenSpace != -1:
        newBoard[emptySpaces[chosenSpace][0]][emptySpaces[chosenSpace][1]] = value

    return newBoard


def printBoard(board):

    for row in range(0,4):
        for col in range(0,4):
            print("%5d" % board[row][col], end="")
        print()
    print()



def tiltRight(board):
 
    newBoard = [
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]]

    for row in range(0,4):
        
        # first slide through any spaces
        loading = 3    
        for col in range(3,-1,-1):
            if board[row][col] != 0:
                newBoard[row][loading] = board[row][col]
                loading = loading - 1
        
        # do resulting columns 3 and 2 match?
        if (newBoard[row][3] == newBoard[row][2]):

            # combine and slide
            newBoard[row][3] = newBoard[row][3] * 2
            newBoard[row][2] = newBoard[row][1]
            newBoard[row][1] = newBoard[row][0]
            newBoard[row][0] = 0

            # do resulting 2 and 1 match?
            if (newBoard[row][2] == newBoard[row][1]):

                # combine and slide, then finished
                newBoard[row][2] = newBoard[row][2] * 2
                newBoard[row][1] = newBoard[row][0]
                newBoard[row][0] = 0

            elif (newBoard[row][1] == newBoard[row][0]):

                # combine and slide, then finished
                newBoard[row][1] = newBoard[row][1] * 2
                newBoard[row][0] = 0

        elif (newBoard[row][2] == newBoard[row][1]):

            # combine and slide, then finished
            newBoard[row][2] = newBoard[row][2] * 2
            newBoard[row][1] = newBoard[row][0]
            newBoard[row][0] = 0

        elif (newBoard[row][1] == newBoard[row][0]):

            # combine and slide, then finished
            newBoard[row][1] = newBoard[row][1] * 2
            newBoard[row][0] = 0
      
    return newBoard


def tiltLeft(board):

    newBoard = [
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]]

    for row in range(0,4):
        
        # first slide through any spaces
        loading = 0  
        for col in range(0, 4):
            if board[row][col] != 0:
                newBoard[row][loading] = board[row][col]
                loading = loading + 1
        
        # do resulting columns 0 and 1 match?
        if (newBoard[row][0] == newBoard[row][1]):

            # combine and slide
            newBoard[row][0] = newBoard[row][0] * 2
            newBoard[row][1] = newBoard[row][2]
            newBoard[row][2] = newBoard[row][3]
            newBoard[row][3] = 0

            # do resulting 1 and 2 match?
            if (newBoard[row][1] == newBoard[row][2]):

                # combine and slide, then finished
                newBoard[row][1] = newBoard[row][1] * 2
                newBoard[row][2] = newBoard[row][3]
                newBoard[row][3] = 0

            elif (newBoard[row][2] == newBoard[row][3]):

                # combine and slide, then finished
                newBoard[row][2] = newBoard[row][2] * 2
                newBoard[row][3] = 0

        elif (newBoard[row][1] == newBoard[row][2]):

            # combine and slide, then finished
            newBoard[row][1] = newBoard[row][1] * 2
            newBoard[row][2] = newBoard[row][3]
            newBoard[row][3] = 0

        elif (newBoard[row][2] == newBoard[row][3]):

            # combine and slide, then finished
            newBoard[row][2] = newBoard[row][2] * 2
            newBoard[row][3] = 0

    return newBoard


def tiltUp(board):

    newBoard1 = [
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]]

    newBoard2 = [[0,0,0,0],
             [0,0,0,0],
             [0,0,0,0],
             [0,0,0,0]]


    # rotate the board to the left
    loading = 0
    for col in range(3,-1,-1):
        for row in range(0,4):
            newBoard1[loading][row] = board[row][col]
        loading = loading + 1

    # tilt the resulting board left
    newBoard1 = tiltLeft(newBoard1)

    # rotate the board back to the right
    for col in range(0, 4):
        loading = 0
        for row in range(3,-1,-1):
            newBoard2[col][loading] = newBoard1[row][col]
            loading = loading + 1
    
    return newBoard2


def tiltDown(board):

    newBoard1 = [
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]]

    newBoard2 = [[0,0,0,0],
             [0,0,0,0],
             [0,0,0,0],
             [0,0,0,0]]

    # rotate the board to the right
    for col in range(0, 4):
        loading = 0
        for row in range(3,-1,-1):
            newBoard1[col][loading] = board[row][col]
            loading = loading + 1
    
    # tilt the resulting board left
    newBoard1 = tiltLeft(newBoard1)

    # rotate the board back to the left
    loading = 0
    for col in range(3,-1,-1):
        for row in range(0,4):
            newBoard2[loading][row] = newBoard1[row][col]
        loading = loading + 1
    
    return newBoard2



# main program

moves = 0

mainBoard = [[0,0,0,0],
             [0,0,0,0],
             [0,0,0,0],
             [0,0,0,0]]

mainBoard = placeRandomTile(mainBoard)
mainBoard = placeRandomTile(mainBoard)

print("")
print("The starting board: ")
printBoard(mainBoard)

while not inDeadlock(mainBoard):
    
    bestMove = findBestMove(mainBoard)

    if bestMove == 0:
        mainBoard = tiltUp(mainBoard)
        print ("Tilting up.")
    elif bestMove == 1:
        mainBoard = tiltDown(mainBoard)
        print ("Tilting down.")
    elif bestMove == 2:
        mainBoard = tiltLeft(mainBoard)
        print ("Tilting left.")
    else:
        mainBoard = tiltRight(mainBoard)
        print ("Tilting right.")

    moves = moves + 1
    printBoard(mainBoard)
    print("Adding a random tile.")
    
    mainBoard = placeRandomTile(mainBoard)
    printBoard(mainBoard)

    print("Hit ENTER to continue.")
    print("")
    temp = input("")
    
printBoard(mainBoard)
print ("Total moves: ", moves)

