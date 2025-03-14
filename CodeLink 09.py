# THE COMPUTER ALWAYS WINS
# MIT PRESS
#
# CodeLink 9
# Depth-Limited Connect Four
# last revised 12/25/24
#
# This is a fully functioning implementation of the code discussed
# in Chapter Five.  Once you play with it, see if you can write a
# version that plays TicTacToe but with limits on depth.


# import
import random

# constants
COMPUTERWINS = 1000
PLAYERWINS = -1000
TIE = 0

# function definitions

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

  
# score the board
def scoreBoard(board):

  # return COMPUTERWINS if the computer won
  # return PLAYERWINS if the human won
  # return TIE if there are no spaces left
  # otherwise score the unfinished board
  
  # check for horizontal four-checker sequences
  for row in range(6):
    for col in range(1,5):
      if board[row][col] == board[row][col + 1] and board[row][col] == board[row][col + 2] and \
         board[row][col] == board[row][col + 3] and board[row][col] != "-":
        if board[row][col] == "C":
          return COMPUTERWINS
        else:
          return PLAYERWINS

  # check for vertical four-checker sequences
  for row in range(3):
    for col in range(1,8):
      if board[row][col] == board[row + 1][col] and board[row][col] == board[row + 2][col] and \
         board[row][col] == board[row + 3][col] and board[row][col] != "-":
        if board[row][col] == "C":
          return COMPUTERWINS
        else:
          return PLAYERWINS
      
  # check for diagonal four-checker sequences that run top-left to bottom-right
  for row in range(3):
    for col in range(1,5):
      if board[row][col] == board[row + 1][col + 1] and board[row][col] == board[row + 2][col + 2] and \
         board[row][col] == board[row + 3][col + 3] and board[row][col] != "-":
        if board[row][col] == "C":
          return COMPUTERWINS
        else:
          return PLAYERWINS

  # check for diagonal four-checker sequences that run top-right to bottom-left
  for row in range(3):
    for col in range(4, 8):
      if board[row][col] == board[row + 1][col - 1] and board[row][col] == board[row + 2][col - 2] and \
         board[row][col] == board[row + 3][col - 3] and board[row][col] != "-":
        if board[row][col] == "C":
          return COMPUTERWINS
        else:
          return PLAYERWINS
    
  # now check for a tie
  if isFilled(board):
    return TIE

  # assign a numeric score to this in-progress board
  # + 10 points if a group of four positions has 3 of one type, 0 of the other
  # + 5 points if a group of four positions has 2 of one type, 0 of the other
  # + 3 points for each checker in column 4 (board[x][3])

  playerScore = 0
  computerScore = 0

  # evaluate horizontal groups of four positions
  for row in range(6):
    for col in range(1, 5):
      playerCount = 0
      computerCount = 0
      blankCount = 0
      for nextSpace in range(4):
        if board[row][col + nextSpace] == "P":
          playerCount += 1
        elif board[row][col + nextSpace] == "C":
          computerCount += 1
        else:
          blankCount += 1

      if (playerCount == 3) and (blankCount == 1):
        playerScore += 10
      if (playerCount == 2) and (blankCount == 2):
        playerScore += 5
      if (computerCount == 3) and (blankCount == 1):
        computerScore += 10
      if (computerCount == 2) and (blankCount == 2):
        computerScore += 5
      
  # evaluate vertical groups of four positions
  for row in range(3):
    for col in range(1, 8):
      playerCount = 0
      computerCount = 0
      blankCount = 0
      for nextSpace in range(4):
        if board[row + nextSpace][col] == "P":
          playerCount += 1
        elif board[row + nextSpace][col] == "C":
          computerCount += 1
        else:
          blankCount += 1

      if (playerCount == 3) and (blankCount == 1):
        playerScore += 10
      if (playerCount == 2) and (blankCount == 2):
        playerScore += 5
      if (computerCount == 3) and (blankCount == 1):
        computerScore += 10
      if (computerCount == 2) and (blankCount == 2):
        computerScore += 5

  # evaluate top-left to bottom-right diagonals
  for row in range(3):
    for col in range(1, 5):
      playerCount = 0
      computerCount = 0
      blankCount = 0
      for nextSpace in range(4):
        if board[row + nextSpace][col + nextSpace] == "P":
          playerCount += 1
        elif board[row + nextSpace][col + nextSpace] == "C":
          computerCount += 1
        else:
          blankCount += 1

      if (playerCount == 3) and (blankCount == 1):
        playerScore += 10
      if (playerCount == 2) and (blankCount == 2):
        playerScore += 5
      if (computerCount == 3) and (blankCount == 1):
        computerScore += 10
      if (computerCount == 2) and (blankCount == 2):
        computerScore += 5

  # evaluate top-right to bottom-left diagonals
  for row in range(3):
    for col in range(4, 8):
      playerCount = 0
      computerCount = 0
      blankCount = 0
      for nextSpace in range(4):
        if board[row + nextSpace][col - nextSpace] == "P":
          playerCount += 1
        elif board[row + nextSpace][col - nextSpace] == "C":
          computerCount += 1
        else:
          blankCount += 1

      if (playerCount == 3) and (blankCount == 1):
        playerScore += 10
      if (playerCount == 2) and (blankCount == 2):
        playerScore += 5
      if (computerCount == 3) and (blankCount == 1):
        computerScore += 10
      if (computerCount == 2) and (blankCount == 2):
        computerScore += 5

  # evaluate column 4 of the gameboard
  for row in range(6):
      if board[row][4] == "P":
          playerScore += 3
      elif board[row][4] == "C":
          computerScore += 3

  # if the calculated score will be 0, nudge the score up to 0.0001
  # otherwise, the code will return 0 and wrongly imply that the board is filled

  if (computerScore - playerScore == 0):
    computerScore = computerScore + 0.0001    

  return computerScore - playerScore


# generate a test board where we can test a proposed move
def generateTestBoard(board, col, player):

  # copy the board
  newBoard = []
  for oldRow in board:
    copiedRow = []
    for entry in oldRow:
      copiedRow.append(entry)
    newBoard.append(copiedRow)
    
  # put the correct mark at the proposed position
  newBoard = dropChecker(newBoard, player, col)
  
  return newBoard


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


# decide what happens if this player makes this move

def whatHappens(board, column, player, depth):

    # make a test board
    testBoard = generateTestBoard(board, column, player)
    outcome = scoreBoard(testBoard)

    # stop the analysis if we are at max depth
    if depth == 0:
      return outcome

    # also stop if we have a winner
    if (outcome == COMPUTERWINS) or (outcome == PLAYERWINS):
        return outcome

    # or if we have a filled board
    if (outcome == TIE):
        return outcome

    # if none of that,
    # recursively explore the next move
    # until we have a win, tie, or hit max depth
    
    if player == "C":
        player = "P"
    else:
        player = "C"

    opponentInfo = findBestMove(testBoard, player, depth-1)

    # return the result
    return opponentInfo[1]
  

# find the best move for this player
def findBestMove(board, player, depth):

  # set currentBest to ensure that some move is picked
  if player == "C":
    currentBestOutcome = PLAYERWINS-1
  if player == "P":
    currentBestOutcome = COMPUTERWINS+1

  # loop through every column
  for col in range(1,8):

    # test any column that has an empty space
    if board[6][col] < 6:
      
      possibleOutcome = whatHappens(board, col, player, depth)

      # the computer prefers larger scores
      if player == "C":
        if possibleOutcome > currentBestOutcome:
          currentBestMove = col
          currentBestOutcome = possibleOutcome

      # the player prefers smaller scores
      if player == "P":
        if possibleOutcome < currentBestOutcome:
          currentBestMove = col
          currentBestOutcome = possibleOutcome

  return [currentBestMove, currentBestOutcome]



# ############
# main program

# this is the starting gameboard
# the bottom numbers count the number of checkers already in that column
# the left-most column is blank, so players use column numbers 1-7

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
humanTurn = True

print()
print("Let's play Connect Four.")
print("But let's limit depth.")
print()

# ask for a depth limit
depth = int(input("What maximum depth? "))

while gameOver == False:

    printBoard(board)

    if humanTurn:
      humanColumn = getPlayerMove(board)     
      board = dropChecker(board, "P", humanColumn)
      if scoreBoard(board) == PLAYERWINS:
          printBoard(board)
          print("You win, human!")
          gameOver = True
      humanTurn = False

    else:
      print("The computer is thinking.")
      computerColumn = findBestMove(board, "C", depth)[0]
      print ("Computer chooses column %d." % (computerColumn))
      board = dropChecker(board, "C", computerColumn)
      if scoreBoard(board) == COMPUTERWINS:
          printBoard(board)
          print("The computer wins!")
          gameOver = True
      humanTurn = True

    # check for a tie
    if isFilled(board):
      printBoard(board)
      print("Tie game.")
      gameOver = True
