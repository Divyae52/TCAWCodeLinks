# THE COMPUTER ALWAYS WINS
# MIT PRESS
#
# CodeLink 14
# Aiming Darts at Connect Four
# last revised 12/25/24

# This is a complete implementation of the code we built in Chapter Nine.
# We will ultimately use this to create a duel: Connect Four by way of the
# darts algorithm versus Connect Four by way of the full minimax implementation
# from Chapter Six.

# import
import random

# constants for use in the tree
WHO = 0
WHERE = 1
VISITS = 2
WINS = 3
C1 = 4
C2 = 5
C3 = 6
C4 = 7
C5 = 8
C6 = 9
C7 = 10

# other constants
CONTINUE = 9999
INVALID = -99

## FUNCTIONS TO HELP DEBUG THE CODE

def shortTree(tree):
# debug function, nicely prints the first 8 rows of the tree
    for row in range(8):
        print ("%d:" %row, end="")
        for col in range(len(tree[row])):
            print (" ", tree[row][col], end = "")
        print("")
    print ("")

def nicePrint(array):
# debug function, nicely prints any array on screen
    for counter in range(len(array)):
        print (array[counter], end = "")
    print("")
    

## GAME FUNCTIONS FROM PRIOR VERSIONS
    
# print the board nicely
def printBoard(board):

  print()
  print(" 1 2 3 4 5 6 7")

  for row in range(6):
    print (" ", end="")
    for col in range(1,8):
      print(board[row][col],end=" ")
    print()
  print()


# check for a completely filled board
def isFilled(board):

  emptySpaces = 42
  for col in range(1,8):
    emptySpaces -= board[6][col]
  if emptySpaces == 0:
    return True
  else:
    return False


# drop a checker onto the board
def dropChecker(board, symbol, col):

  firstEmptyRow = 5 - board[6][col]

  if firstEmptyRow != -1:
    board[firstEmptyRow][col] = symbol
    board[6][col] += 1

  else:
    print ("ERROR. Cannot drop checker in filled column.")

  return board


# accept only valid responses from the human player
def getPlayerMove(board):

  validChoice = False
  while not validChoice:
    
    response = input("Which column would you like? ")

    validChoice = True

    if response == "":
      validChoice = False
      print ("Please enter a column number.")
      
    else:

      chosenColumn = int(response)

      if chosenColumn not in [1, 2, 3, 4, 5, 6, 7]:
        validChoice = False
        print("That's not one of the options. Choose a number 1-7 please. ")

      elif board[6][chosenColumn] == 6:
        validChoice = False
        print("That column is already full. Please choose another one.")

  return chosenColumn


# score the board
def scoreBoard(board):
    
  # return 1 if the computer won
  # return -1 if the human won
  # return 0 if there are no spaces left
  # otherwise return CONTINUE because this is not a finished board
  
  # check for horizontal four-checker sequences
  for row in range(6):
    for col in range(1,5):
      if board[row][col] == board[row][col + 1] and board[row][col] == board[row][col + 2] and \
         board[row][col] == board[row][col + 3] and board[row][col] != "-":
        if board[row][col] == "C":
          return 1
        else:
          return -1

  # check for vertical four-checker sequences
  for row in range(3):
    for col in range(1,8):
      if board[row][col] == board[row + 1][col] and board[row][col] == board[row + 2][col] and \
         board[row][col] == board[row + 3][col] and board[row][col] != "-":
        if board[row][col] == "C":
          return 1
        else:
          return -1
      
  # check for diagonal four-checker sequences that run top-left to bottom-right
  for row in range(3):
    for col in range(1,5):
      if board[row][col] == board[row + 1][col + 1] and board[row][col] == board[row + 2][col + 2] and \
         board[row][col] == board[row + 3][col + 3] and board[row][col] != "-":
        if board[row][col] == "C":
          return 1
        else:
          return -1

  # check for diagonal four-checker sequences that run top-right to bottom-left
  for row in range(3):
    for col in range(4, 8):
      if board[row][col] == board[row + 1][col - 1] and board[row][col] == board[row + 2][col - 2] and \
         board[row][col] == board[row + 3][col - 3] and board[row][col] != "-":
        if board[row][col] == "C":
          return 1
        else:
          return -1
    
  # now check for a tie
  if isFilled(board):
    return 0

  # play on
  return CONTINUE


## REVISED FUNCTIONS

# generate a test board where we can experiment further
def makeBoard(board, path, tree):

    newBoard = []

    # copy the existing board over
    for row in board:
        newList = []
        for item in row:
            newList.append(item)
        newBoard.append(newList)

    # add any moves made so far
    for move in path:
        if move != 0:
            newBoard = dropChecker(newBoard, tree[move][0], tree[move][1])

    return newBoard


# SIMULATE THE GAME FROM HERE, RANDOMLY
def playRandomly (gameBoard, lastPlayer):

    finished = False
                  
    while not finished:

        # switch players
        if lastPlayer == "C":
            thisPlayer = "R"
        else:
            thisPlayer = "C"

        # randomly drop a checker for this player
        placed = False
        while not placed: 
            column = random.randint(1,7)
            if gameBoard[6][column] < 6:
                placed = True
                gameBoard = dropChecker(gameBoard, thisPlayer, column)

        # check for win, loss or tie
        status = scoreBoard(gameBoard)
        if status != CONTINUE:
            finished = True

        lastPlayer = thisPlayer

    return status
    


# DECIDE WHERE TO SPEND THE NEXT SIMULATION

def chooseChild (currentNode, tree): 

    # store information about the 7 children nodes
    kidNumbers = []
    kidVisits = []
    kidWins = []
    for counter in range(7):
        kidNode = tree[currentNode][C1 + counter]
        if kidNode != INVALID:
            kidNumbers.append(kidNode)
            kidVisits.append(tree[kidNode][VISITS])
            kidWins.append(tree[kidNode][WINS])

    # prepare to look for the next node
    finished = False
    
    # if any of the children have no visits, visit them
    for counter in range(len(kidNumbers)):    
        if kidVisits[counter] == 0:
            finished = True
            bestNode = kidNumbers[counter]

    # if all children have visits, choose based on winrate and visits
    if not finished:
        totalVisits = 0
        for counter in range(len(kidNumbers)):
            totalVisits = totalVisits + kidVisits[counter]

        # initialize first child as best
        bestScore = 10 * kidWins[0]/kidVisits[0] + (totalVisits/kidVisits[0])**0.5
        bestNode = kidNumbers[0]

        # now look to see if any other children are better
        for child in range(1, len(kidNumbers)):
            score = 10 * kidWins[child]/kidVisits[child] + (totalVisits/kidVisits[child])**0.5
            if score > bestScore:
                bestScore = score
                bestNode = kidNumbers[child]

    return bestNode


def findBestMove (board, simulationsMax):
    
    # create the root node
    tree = []
    tree.append(["R",INVALID,0,0,0,0,0,0,0,0,0])
    
    # point to the root
    currentNode = 0
    path = []
    simulationsRun = 0

    # follow the flow chart


    while simulationsRun < simulationsMax:
        
        # add this node to the path
        path.append(currentNode)

        # create the board and evaluate it            
        newBoard = makeBoard(board, path, tree)
        result = scoreBoard(newBoard)
        
        # is this node a dead end?
        if result != CONTINUE:
            
            # update visits and wins along the path
            for priorStep in path:
                tree[priorStep][VISITS] = tree[priorStep][VISITS] + 1       
                if tree[priorStep][WHO] == "C":
                    tree[priorStep][WINS] = tree[priorStep][WINS] + result
                else:
                    tree[priorStep][WINS] = tree[priorStep][WINS] - result

            # reset for the next simulation
            currentNode = 0
            path = []
            simulationsRun = simulationsRun + 1

        elif tree[currentNode][VISITS] == 0:
            # this is our first visit to this node
       
            # which player brought us here?
            whoPlayedLast = tree[currentNode][WHO]

            # it is thus the other player's turn
            if whoPlayedLast == "C":
                whoPlaysNow = "R"
            else:
                whoPlaysNow = "C"

            # add children, but only if the relevant column has space
            lastNode = len(tree)
            for possibleCol in range(1,8):
                if newBoard[6][possibleCol] == 6:
                    tree[currentNode][3+possibleCol] = INVALID
                else:
                    tree[currentNode][3+possibleCol] = lastNode
                    tree.append([whoPlaysNow,possibleCol,0,0,0,0,0,0,0,0,0])
                    lastNode = lastNode + 1
                    
            # now, simulate from this node
            result = playRandomly(newBoard, whoPlayedLast)
            
            # update visits and wins along the path
            for priorStep in path:
                tree[priorStep][VISITS] = tree[priorStep][VISITS] + 1       
                if tree[priorStep][WHO] == "C":
                    tree[priorStep][WINS] = tree[priorStep][WINS] + result
                else:
                    tree[priorStep][WINS] = tree[priorStep][WINS] - result
               
            # reset for the next simulation
            currentNode = 0
            path = []
            simulationsRun = simulationsRun + 1            
            
        else:
            # we already visited this node, so choose a child
            nextNode = chooseChild(currentNode, tree)
            currentNode = nextNode                

    # simulation is over
    # choose the most attractive option

    foundFirst = False
    for child in range(4,11):
        kidNodeNumber = tree[0][child]
        if kidNodeNumber != INVALID:
            if foundFirst == False:
                # this is the first option, so it is the best one so far
                bestRate = tree[kidNodeNumber][WINS]/tree[kidNodeNumber][VISITS]
                bestMove = tree[kidNodeNumber][WHERE]
                foundFirst = True
            else:
                # we have more than one option, so choose the best one
                kidWinRate = tree[kidNodeNumber][WINS]/tree[kidNodeNumber][VISITS]
                if kidWinRate > bestRate:
                    bestRate = kidWinRate
                    bestMove = tree[kidNodeNumber][WHERE]
    
    return bestMove


# ############
# main program
# ############

# this is the starting gameboard
# the bottom numbers count the number of checkers already in that column
# the left-most column is blank, so column 1 is board[x][1] not board[x][0]

board = [
  [" ", "-", "-", "-", "-", "-", "-", "-"],
  [" ", "-", "-", "-", "-", "-", "-", "-"],
  [" ", "-", "-", "-", "-", "-", "-", "-"],
  [" ", "-", "-", "-", "-", "-", "-", "-"],
  [" ", "-", "-", "-", "-", "-", "-", "-"],
  [" ", "-", "-", "-", "-", "-", "-", "-"],
  [ 0,   0,   0,   0,   0,   0,   0,   0 ]
]

gameOver = False
humanTurn = False

print()
print("Let's play Connect Four.")
print()

# ask how many simulations are allowed
simulationsMax = int(input("And how many simulations per move? "))
                     
while gameOver == False:

    printBoard(board)

    if humanTurn:
      humanColumn = getPlayerMove(board)     
      board = dropChecker(board, "R", humanColumn)
      if scoreBoard(board) == -1:
          printBoard(board)
          print("You win, human!")
          gameOver = True
      humanTurn = False

    else:
      print("The computer is thinking.")
      computerColumn = findBestMove(board, simulationsMax)
      print ("Computer chooses column %d." % (computerColumn))
      board = dropChecker(board, "C", computerColumn)
      if scoreBoard(board) == 1:
          printBoard(board)
          print("The computer wins!")
          gameOver = True
      humanTurn = True

    # check for a tie
    if isFilled(board):
      printBoard(board)
      print("Tie game.")
      gameOver = True

