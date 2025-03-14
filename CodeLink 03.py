# THE COMPUTER ALWAYS WINS
# MIT PRESS
#
# CodeLink 3
# Sudoku Solver
# last revised 12/25/24
#
# This code demonstrates backtracking in the context of a
# nine-by-nine sudoku puzzle.

# setting
DEBUG = True

# print the board nicely
def printBoard(board):

  for row in range(9):
    if row % 3 == 0:
      for i in range(25):
        print ("-", end = "")
      print()
    for col in range(9):
      if col % 3 == 0:
        print ("| ", end = "")
      print (board[row][col], end = " ")
    print ("| ", end = "")
    print()
  for i in range(25):
    print ("-", end = "")
  print()

# return True if this number can legally be placed at row, col
def isPossible(board, row, col, number):
    
  # find the row and col that start this group of 9 spaces
  startRow = int(row/3)*3
  startCol = int(col/3)*3
  
  # store the values in those 9 spaces
  squareList = []
  for r in range(3):
    for c in range(3):
      squareList.append(board[r+startRow][c+startCol])
  
  # check for conflicts by row, by col, and by 9-space square
  for i in range(9):
    if board[row][i] == number:
      return False
    if board[i][col] == number:
      return False
    if squareList[i] == number:
      return False
  return True

# return True if the board is completely filled
def isFilled(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == "-":
                return False
    return True


# return True if the puzzle has been solved
def solvePuzzle(board, currentRow, currentCol):

    # return True if the board is filled
    if isFilled(board):
        print()
        printBoard(board)
        print()
        return True

    # find the next empty space
    # search left to right, top to bottom
    while board[currentRow][currentCol] != "-":
        if currentCol < 8:
            currentCol = currentCol + 1
        else:
            currentRow = currentRow + 1
            currentCol = 0

    # test every number 1-9
    # if the number fits, recursively solve the rest of the puzzle
    for num in range(1,10):
        
        if isPossible(board, currentRow, currentCol, num):

            # fill in that number
            board[currentRow][currentCol] = num

            # optional output to the screen when adding a number
            if DEBUG:
              printBoard(board)
              next = input("")
              print()

            # make the recursive call
            if solvePuzzle(board, currentRow, currentCol):
              return True
            
    # nothing worked, so backtrack
    board[currentRow][currentCol] = "-"

    # optional output to the screen during backtrack
    if DEBUG:
      printBoard(board)
      next = input("")
      print()

    return False
    
# main program

# create an empty board
board = [
    [ 7 ,"-","-", 6 , 5 ,"-","-", 9 ,"-"],
    [ 2 ,"-","-","-", 7 , 3 , 4 , 5 ,"-"],
    ["-","-","-","-","-","-", 3 ,"-","-"],
    ["-", 5 ,"-","-", 6 , 8 , 9 ,"-","-"],
    [ 1 , 2 ,"-","-", 9 ,"-","-", 6 ,"-"],
    [ 6 , 8 ,"-", 2 ,"-", 4 , 5 , 7 ,"-"],
    ["-","-","-","-","-", 5 , 7 ,"-","-"],
    ["-","-", 5 ,"-", 3 , 2 ,"-","-", 9 ],
    [ 9 ,"-","-","-","-","-","-","-","-"]]
    
print()
print("I will solve this Sudoku puzzle using backtracking.")
print("I will start at the upper left and finish at the lower right.")
print()
print("Hold the ENTER key to watch the process.")
print("Or set DEBUG to False in the code and I will solve on my own.")
print()
printBoard(board)
print()
next = input("")

result = solvePuzzle(board, 0, 0)

if result == True:
    print("I found a solution.")
else:
    print("I did not find a solution.")
    




