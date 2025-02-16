# THE COMPUTER ALWAYS WINS
# MIT PRESS
#
# CodeLink 2
# Maze Solver
# last revised 12/25/24
#
# This code demonstrates backtracking in the context of the maze
# program explained in Chapter Two.


# FUNCTIONS

# print the maze nicely
def printMaze(maze):
    for row in maze:
        for item in row:
            print(item, end=" ")
        print()
    print()

print()


def isLegal (maze, possibleRow, possibleColumn):
# return True if this space is on the board and available

    if possibleColumn<0 or possibleColumn>4:
        return False

    if possibleRow<0 or possibleRow>4:
        return False

    if maze[possibleRow][possibleColumn] != 0:
        return False

    return True


def isExit(maze, possibleRow, possibleColumn):
# return True if this is the exit

    if possibleRow == 4 and possibleColumn == 4:
        return True
    else:
        return False
    

def solveMaze (maze, currentRow, currentColumn):
# return True if the exit can be reached

    # mark this position as visited
    maze[currentRow][currentColumn] = "*"
    printMaze(maze)
    next = input("")
    
    # return True if this is the exit
    if isExit(maze, currentRow, currentColumn):
        return True
    
    # if down is legal, move down and search recursively
    if isLegal(maze, currentRow+1, currentColumn):
        if solveMaze(maze, currentRow+1, currentColumn):
            return True

    # if up is legal, move up and search recursively
    if isLegal(maze, currentRow-1, currentColumn):
        if solveMaze(maze, currentRow-1, currentColumn):
            return True

    # if right is legal, move right and search recursively
    if isLegal(maze, currentRow, currentColumn+1):
        if solveMaze(maze, currentRow, currentColumn+1):
            return True

    # if left is legal, move left and search recursively
    if isLegal(maze, currentRow, currentColumn-1):
        if solveMaze(maze, currentRow, currentColumn-1):
            return True

    # nothing worked, so return to the previous position (backtrack)
    maze[currentRow][currentColumn] = 0
    printMaze(maze)
    next = input("")
    return False


# main

maze = [
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0]]

print()
printMaze(maze)
print("I will solve this maze using backtracking.")
print("I will start at the upper left and exit at the lower right.")
print("1 is a wall, 0 is a path.")
print()
print("Hit enter to allow me to advance.")
print()
next = input("")

result = solveMaze(maze, 0, 0)

if result == True:
    print("I found a path.")
else:
    print("I did not find a path.")
    

