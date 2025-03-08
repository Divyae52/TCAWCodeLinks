# THE COMPUTER ALWAYS WINS
# MIT PRESS
#
# CodeLink 7
# MiniMax TicTacToe
# last revised 12/26/24

# This is a full working version of our minimax tic-tac-toe code.
# Add print statements inside the various functions to see if you
# can keep track of what the computer is doing.  Does the computer
# follow the analysis we sketched in Chapter Four?

# constants
WIN = 1
TIE = 0
LOSS = -1
INCOMPLETE = 99

# print the board nicely
def printBoard(board):
  print()
  print("   1  2  3 ")
  counter = 1
  for row in board:
    print(counter, end = " ")
    for item in row:
      print(" " + item, end = " ")
    print()
    counter += 1
  print()

# score the board
def scoreBoard(board):

    # return WIN if the most recent move led to three in a row  
    if (board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][2] != "_") or \
       (board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][2] != "_") or \
       (board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][2] != "_") or \
       (board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[2][0] != "_") or \
       (board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[2][1] != "_") or \
       (board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[2][2] != "_") or \
       (board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[2][2] != "_") or \
       (board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[2][0] != "_"):
        return WIN

    # return TIE if there are no empty spaces
    emptySpaces = 0
    for row in range(3):
        for col in range(3):
            if board[row][col] == "_":
                emptySpaces = emptySpaces + 1
    if emptySpaces == 0:
        return TIE

    # otherwise, keep playing
    return INCOMPLETE

# generate a test board where we can test a proposed move
def generateTestBoard(board, row, col, player):

    # copy the board
    newBoard = []
    for oldRow in board:
        copiedRow = []
        for position in oldRow:
            copiedRow.append(position)
        newBoard.append(copiedRow)
    
    # put the correct mark at the proposed position
    newBoard[row][col] = player

    return newBoard


# decide what happens if this player makes this move
def whatHappens(board, row, col, player):

    # make a test board
    testBoard = generateTestBoard(board, row, col, player)
    outcome = scoreBoard(testBoard)

    if (outcome == WIN) or (outcome == TIE):
        return outcome

    # if this move triggered neither a win nor a tie
    # we need to now consider the opponent's response

    if player == "C":
        player = "P"
    else:
        player = "C"

    opponentInfo = findBestMove(testBoard, player)

    # return the result from the calling player's perspective
    if opponentInfo[1] == WIN:
        return LOSS
    elif opponentInfo[1] == LOSS:
        return WIN
    else:
        return TIE


# find the best move for this player
def findBestMove(board, player):

    # DEBUG IDEA
    # Turn the below conditional to True and you can watch the algorithm as it runs.

    if False:
      print("Looking at this board for %s:" %player)
      printBoard(board)
      temp = input("Next?")
        
    currentBestMove = [-99, -99]
    currentBestOutcome = -99

    for row in range(3):
        for col in range(3):
            
            if board[row][col] == "_":

                possibleOutcome = whatHappens(board, row, col, player)

                if possibleOutcome > currentBestOutcome:        
                    currentBestMove[0] = row
                    currentBestMove[1] = col
                    currentBestOutcome = possibleOutcome

    return [currentBestMove, currentBestOutcome]


# ############
# main program

# make a blank 3 by 3 board for this game
board = [["_","_","_"],["_","_","_"],["_","_","_"]]

gameOver = False
humanTurn = True

print("Let's play Tic Tac Toe.")
print("")

while gameOver == False:

    printBoard(board)

    if humanTurn:
        humanRow = int(input("What row? [1-3] ")) - 1
        humanCol = int(input("What col? [1-3] ")) - 1
        board[humanRow][humanCol] = "P"
        if scoreBoard(board) == WIN:
            print("You win, human!")
            gameOver = True
        humanTurn = False

    else:
        print("The computer is plotting.")
        computerMove = findBestMove(board, "C")
        board[computerMove[0][0]][computerMove[0][1]] = "C"
        if scoreBoard(board) == WIN:
            printBoard(board)
            print("The computer wins!")
            gameOver = True
        humanTurn = True

    if scoreBoard(board) == TIE:
        printBoard(board)
        print("Tie game.")
        gameOver = True




