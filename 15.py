# THE COMPUTER ALWAYS WINS
# MIT PRESS
#
# CodeLink 15
# Rock, Paper, Paper
# last revised 12/25/24

# This is a full implementation of the code we wrote in the first
# half of Chapter Ten.  Once you test it out, see if you can gain
# further advantage by adding additional functions like
# isBoring() isSoreLoser().


import random

# set number of games to play
maxGames = 300

# define constants, for readable code
RELUCTANT = 1
BORING = 2
RANDOM = 3

## FUNCTIONS THAT SIMULATE THE VARIOUS TYPES OF HUMAN PLAYERS

def playRandomly():
    # output: a random move
    
    choice = random.randint(1,3)

    if choice == 1:
        return ("ROCK")
    if choice == 2:
        return ("PAPER")
    else:
        return("SCISSORS")


def playReluctantly(priorPlayerMove):
    # output: a move that is unlikely to be the same as the most prior move

    # choose a random number from 1 to 13
    # 6/13 odds for each of two new moves
    # 1/13 odds for repeating this move
    
    currentMove = random.randint(1, 13)
    
    if priorPlayerMove == "ROCK":
        if currentMove in [1]:
            return "ROCK"
        if currentMove in [2, 3, 4, 5, 6, 7]:
            return "PAPER"
        if currentMove in [8, 9, 10, 11, 12, 13]:
            return "SCISSORS"

    if priorPlayerMove == "PAPER":
        if currentMove in [1, 2, 3, 4, 5, 6]:
            return "ROCK"
        if currentMove in [7]:
            return "PAPER"
        if currentMove in [8, 9, 10, 11, 12, 13]:
            return "SCISSORS"

    if priorPlayerMove == "SCISSORS":
        if currentMove in [1, 2, 3, 4, 5, 6]:
            return "ROCK"
        if currentMove in [7, 8, 9, 10, 11, 12]:
            return "PAPER"
        if currentMove in [13]:
            return "SCISSORS"

    
def playBoringly(playerHistory):
    # output is 4/6 chance of being the player's most common prior choice, 1/6 each other choice
    
    numGames = len(playerHistory)
    choices = [0,0,0]
    maxCount = 0

    # find the most-used choice
    for ctr in range(numGames):
        if playerHistory[ctr] == "ROCK":
            choices[0] +=1
            if choices[0] > maxCount:
                maxCount = choices[0]
                mainChoice = "ROCK"
        if playerHistory[ctr] == "PAPER":
            choices[1] +=1
            if choices[1] > maxCount:
                maxCount = choices[1]
                mainChoice = "PAPER"
        if playerHistory[ctr] == "SCISSORS":
            choices[2] +=1
            if choices[2] > maxCount:
                maxCount = choices[2]
                mainChoice = "SCISSORS"

    currentMove = random.randint(1,6)
    
    if mainChoice == "ROCK":
        if currentMove in [1, 2, 3, 4]:
            return "ROCK"
        if currentMove in [5]:
            return "PAPER"
        if currentMove in [6]:
            return "SCISSORS"

    if mainChoice == "PAPER":
        if currentMove in [1]:
            return "ROCK"
        if currentMove in [2, 3, 4, 5]:
            return "PAPER"
        if currentMove in [6]:
            return "SCISSORS"

    if mainChoice == "SCISSORS":
        if currentMove in [1]:
            return "ROCK"
        if currentMove in [2]:
            return "PAPER"
        if currentMove in [3, 4, 5, 6]:
            return "SCISSORS"

  
## FUNCTIONS THAT RESPOND TO VARIOUS HUMAN QUIRKS

def respondReluctant(playerMove):
    # input: the player's most recent move
    # output: the computer's best response if the player will not repeat

    if playerMove == "ROCK":
        return ("SCISSORS")
    if playerMove == "SCISSORS":
        return ("PAPER")
    else:
        return("ROCK")


def respondBoring(playerHistory):
    # input: the player's full move history
    # output: the computer's best response if the player plays the most common prior move

    numGames = len(playerHistory)
    choices = [0,0,0]
    maxCount = 0

    # find the most-used choice
    for ctr in range(numGames):
        if playerHistory[ctr] == "ROCK":
            choices[0] +=1
            if choices[0] > maxCount:
                maxCount = choices[0]
                mostCommon = "ROCK"
        if playerHistory[ctr] == "PAPER":
            choices[1] +=1
            if choices[1] > maxCount:
                maxCount = choices[1]
                mostCommon = "PAPER"
        if playerHistory[ctr] == "SCISSORS":
            choices[2] +=1
            if choices[2] > maxCount:
                maxCount = choices[2]
                mostCommon = "SCISSORS"
    
    if mostCommon == "ROCK":
        return ("PAPER")
    if mostCommon == "PAPER":
        return ("SCISSORS")
    if mostCommon == "SCISSORS":
        return ("ROCK")


## FUNCTIONS THAT DETECT VARIOUS HUMAN QUIRKS
     
def isReluctant (playerHistory):
    # input: the player's full move history
    # output: game results if the computer assumes this player is reluctant to repeat
    
    outcome = 0
    numGames = len(playerHistory)
    
    for ctr in range(1, numGames):
        playerChoice = playerHistory[ctr]
        computerChoice = respondReluctant(playerHistory[ctr-1])
        outcome = outcome + calculateOutcome(playerChoice, computerChoice)

    return(outcome)
    

def isBoring (playerHistory):
    # input: the player's full move history
    # output: game results if computer assumes this player mainly plays the same move

    outcome = 0
    numGames = len(playerHistory)
    partialPlayerHistory = []
    partialPlayerHistory.append(playerHistory[0])

    for ctr in range(1, numGames):
        playerChoice = playerHistory[ctr]
        computerChoice = respondBoring(partialPlayerHistory)
        outcome = outcome + calculateOutcome(playerChoice, computerChoice)
        partialPlayerHistory.append(playerChoice)

    return(outcome)


def isRandom ():
    # output: one third the number of games played, which is the random outcome
    
    numGames = len(playerHistory)
    return (numGames/3)


## THIS FUNCTION LETS THE COMPUTER CHOOSE ITS BEST MOVE
def chooseBestResponseStrategy (playerHistory, computerHistory):
    
    # input is the full history so far between these players
    # output is the computer's best next move based on that history

    numGames = len(playerHistory)
    
    # computer evaluates some possible options
    reluctantScore = isReluctant(playerHistory)
    boringScore = isBoring(playerHistory)
    randomScore = isRandom()

    # computer finds the best strategy
    computerChoice = RELUCTANT
    bestScore = reluctantScore
    if boringScore > bestScore:
        computerChoice = BORING
        bestScore = boringScore
    if randomScore > bestScore:
        computerChoice = RANDOM
        bestScore = randomScore
    
    return computerChoice
   
    
## REPORT BACK WHO WON, OR IF IT WAS A TIE
def calculateOutcome (playerMove, computerMove):
    # input: the moves this round
    # output: 1 if the computer wins, -1 if the computer loses, 0 if tie

    outcome = 0
    
    if playerMove == "ROCK":
        if computerMove == "SCISSORS":
            outcome = -1
        elif computerMove == "PAPER":
            outcome = 1
        else:
            outcome = 0
    
    if playerMove == "SCISSORS":
        if computerMove == "PAPER":
            outcome = -1
        elif computerMove == "ROCK":
            outcome = 1
        else:
            outcome = 0

    if playerMove == "PAPER":
        if computerMove == "ROCK":
            outcome = -1
        elif computerMove == "SCISSORS":
            outcome = 1
        else:
            outcome = 0

    return (outcome)


# main program
# ############

while True:

    # define variables
    playerHistory = []
    computerHistory = []
    computerWins = 0
    playerWins = 0
    ties = 0
    
    # allow user to pick a player type
    print ("")
    print ("Choose a type of player.")
    print ("")
    print ("1 = A player who is reluctant to repeat back-to-back.")
    print ("2 = A boring player who disproportionately plays one move.")
    print ("3 = A truly random player.")
    print ("")
    humanStrategy = int(input("=> "))
        
    # play the game
    for counter in range(maxGames):

        if counter == 0:
            # the first move for both computer and player is random
            computerMove = playRandomly()
            playerMove = playRandomly()

        else:
            if humanStrategy == RELUCTANT:
                playerMove = playReluctantly(playerHistory[counter-1])
            if humanStrategy == BORING:
                playerMove = playBoringly(playerHistory)
            if humanStrategy == RANDOM:
                playerMove = playRandomly()
                
            if counter == 1:
                # the second move for the computer is also random
                computerMove = playRandomly()
            else:
                # starting with the 3rd move, however, the computer can learn
                computerStrategy = chooseBestResponseStrategy(playerHistory, computerHistory)
                if computerStrategy == RELUCTANT:
                    computerMove = respondReluctant(playerHistory[counter-1])
                if computerStrategy == BORING:
                    computerMove= respondBoring(playerHistory)
                if computerStrategy == RANDOM:
                    computerMove = playRandomly()
                     
        result = calculateOutcome (playerMove, computerMove)
        
        if result == 1:
            computerWins = computerWins + 1
        elif result == -1:
            playerWins = playerWins + 1
        else:
            ties = ties + 1

        playerHistory.append(playerMove)
        computerHistory.append(computerMove)
        
    # report final statistics
    if computerStrategy == RELUCTANT:
        description = "RELUCTANT"
    if computerStrategy == BORING:
        description = "BORING"
    if computerStrategy == RANDOM:
        description = "RANDOM"
        
    print ("")
    print ("I just played %d games against this player." % (counter+1))
    print ("In the end, I decided that this is a %s player." %description)
    print ("As I figured that out, I won %2.0f percent of the games." % (100*computerWins/maxGames))
    print ("")
    print ("Let's play again.")
    
