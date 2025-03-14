# THE COMPUTER ALWAYS WINS
# MIT PRESS
#
# CodeLink 6
# The Coin Game (Nim)
# last revised 12/25/24

# After you play the game a few times, see if you can edit
# the code to use 15 coins and allow a player to take 1, 2,
# or 3 coins on each turn. Does the computer always win?


# define two constants, to make our code more readable
WIN = 1
LOSE = -1

# FUNCTION DEFINITIONS

def whatHappens(coins, move):
    # do we win or lose if there are COINS left, and we take MOVE of them?
    
    newStatus = coins - move
    
    if newStatus <= 0:
        return WIN

    opponentOutcome = findBestMove(newStatus)[1]
    
    if opponentOutcome == WIN:
        return LOSE
    else:
        return WIN
        

def findBestMove(coins):
# this function takes as input the number of coins
# it returns a suggested move, and a predicted outcome

    outcomeOne = whatHappens(coins, 1)
    outcomeTwo = whatHappens(coins, 2)
  
    if outcomeOne == WIN:
        return [1, outcomeOne]
    else:
        return [2, outcomeTwo]

        
# MAIN PROGRAM

coins = 7
turn = "computer"

print ("Let's play the coin game using 7 coins.")
print ("I'll go first.")

while coins > 0:

    print ("")
    print ("Coins left:", coins)

    if turn == "person":
        playerMove = int(input("  How many will you take? "))
        coins = coins - playerMove
    
        if coins == 0:
            print ("")
            print ("The person wins. Must be luck!")

        turn = "computer"

    else:
        computerMove = findBestMove(coins)[0]
        print ("  Computer takes:", computerMove)
        coins = coins - computerMove
    
        if coins == 0:
            print ("")
            print ("The computer wins, of course.")
            
        turn = "person"
