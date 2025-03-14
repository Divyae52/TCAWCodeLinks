# THE COMPUTER ALWAYS WINS
# MIT PRESS
#
# CodeLink 16
# Better Tracking for Rock, Paper, Scissors
# last revised 12/25/24

# This version of the code uses our rockHistory, paperHistory,
# and scissorsHistory variables to keep track of prior games.
# Can you update the code so that it considers more complicated
# relationships, like whenRockWon and whenRockLost?

import random

# define constant
maxGames = 500

# create the chains
rockHistory = [0,0,0,0]
paperHistory = [0,0,0,0]
scissorsHistory = [0,0,0,0]


# print the chains to the screen
# ##############################

def printSummary(chain):
    print ("%3d events: %3d rock; %3d paper; %3d scissors." % (chain[0],chain[1],chain[2],chain[3]))
    
def printChains():
    print ("     Rock History: ", end = "")    
    printSummary(rockHistory)
    print ("    Paper History: ", end = "")    
    printSummary(paperHistory)
    print (" Scissors History: ", end = "")    
    printSummary(scissorsHistory)
    print ()

    # dEBUG
    temp = input ("")

# functions that simulate the various types of human players
# ##########################################################

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



def playSorely(priorPlayerMove, priorComputerMove):
    # output: a different choice than prior, if the player lost; otherwise random

    if calculateOutcome(priorPlayerMove, priorComputerMove) == 1:
        # player lost, so he should not repeat his prior choice
        
        currentMove = random.randint(1,2)
        # equally likely to do either of the other moves

        if priorPlayerMove == "ROCK":
            if currentMove == 1:
                return "PAPER"
            else:
                return "SCISSORS"

        if priorPlayerMove == "PAPER":
            if currentMove == 1:
                return "ROCK"
            else:
                return "SCISSORS"
            
        if priorPlayerMove == "SCISSORS":
            if currentMove == 1:
                return "ROCK"
            else:
                return "PAPER"

    else:
        # player won, so plays randomly
        return playRandomly()



   
def playPatterned(priorPlayerMove):
    # output: the next move in the pattern r/p/s

    if priorPlayerMove == "ROCK":
        return ("PAPER")
    if priorPlayerMove == "PAPER":
        return("SCISSORS")
    else:
        return("ROCK")
        

    
# functions that help the computer choose its move
# ################################################

def bestResponseTo (likelyChoiceArray):
    # input is the odds the other player will pick rock, paper, and scissors
    # output is my best response given those odds

    bestOutcome = -1
    bestMove = "ROCK"
    possibleOutcome = 0

    if likelyChoiceArray[0] == 0:
        # no data for the computer to use here
        bestMove = playRandomly()
    else:
        # find the best response
        oddsRock = likelyChoiceArray[1]/likelyChoiceArray[0]
        oddsPaper = likelyChoiceArray[2]/likelyChoiceArray[0]
        oddsScissor = likelyChoiceArray[3]/likelyChoiceArray[0]
    
        for possibleResponse in ["ROCK", "PAPER", "SCISSORS"]:
            possibleOutcome = possibleOutcome + oddsRock * calculateOutcome ("ROCK", possibleResponse)
            possibleOutcome = possibleOutcome + oddsPaper * calculateOutcome ("PAPER", possibleResponse)
            possibleOutcome = possibleOutcome + oddsScissor* calculateOutcome ("SCISSORS", possibleResponse)
            if possibleOutcome > bestOutcome:
                bestOutcome = possibleOutcome
                bestMove = possibleResponse
            possibleOutcome = 0

    return bestMove

                
def chooseBestMove (playerHistory, computerHistory):
    # input is the full history so far between these players
    # output is the computer's best next move based on that history
    
    # check that we have enough data to work with
    numGames = len(playerHistory)
    if numGames < 2:
        return playRandomly()

    # if we have enough data, update the three Markov chains based on prior two games
    twoBackMove = playerHistory[numGames-2]
    oneBackMove = playerHistory[numGames-1]

    # if twoBackMove was Rock, update rockHistory with oneBackMove
    if twoBackMove == "ROCK":
        if oneBackMove == "ROCK":
            rockHistory[1] += 1
        if oneBackMove == "PAPER":
            rockHistory[2] += 1
        if oneBackMove == "SCISSORS":
            rockHistory[3] += 1
        rockHistory[0] += 1

    # if twoBackMove was Paper, update paperHistory with oneBackMove
    if twoBackMove == "PAPER":
        if oneBackMove == "ROCK":
            paperHistory[1] += 1
        if oneBackMove == "PAPER":
            paperHistory[2] += 1
        if oneBackMove == "SCISSORS":
            paperHistory[3] += 1
        paperHistory[0] += 1

    # if twoBackMove was Rock, update scissorsHistory with oneBackMove
    if twoBackMove == "SCISSORS":
        if oneBackMove == "ROCK":
            scissorsHistory[1] += 1
        if oneBackMove == "PAPER":
            scissorsHistory[2] += 1
        if oneBackMove == "SCISSORS":
            scissorsHistory[3] += 1
        scissorsHistory[0] += 1

    # now, choose the best response, using the appropriate chain
    if oneBackMove == "ROCK":
        computerMove = bestResponseTo(rockHistory)
    if oneBackMove == "PAPER":
        computerMove = bestResponseTo(paperHistory)
    if oneBackMove == "SCISSORS":
        computerMove = bestResponseTo(scissorsHistory)
    
    return computerMove


# report back who won
# ###################

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


# MAIN PROGRAM
# ############

# define constants, for readable code
RANDOM = 1
RELUCTANT = 2
BORING = 3
SORE = 4
PATTERNED = 5

# define/reset variables
playerHistory = []
computerHistory = []
computerWins = 0
playerWins = 0
ties = 0

# allow user to pick a player type
print ("")
print ("What type of player should we invite to play?")
print ("1 = Random player.")
print ("2 = Reluctant player.")
print ("3 = Boring player.")
print ("4 = Sore loser.")
print ("5 = R/P/S in that order.")
print ("")
humanStrategy = int(input("=> "))

# play the game
for counter in range(maxGames):

    if counter == 0:
        # the first move for both computer and player is random
        computerMove = playRandomly()
        playerMove = playRandomly()

    else:
        if humanStrategy == RANDOM:
            playerMove = playRandomly()
        if humanStrategy == RELUCTANT:
            playerMove = playReluctantly(playerHistory[counter-1])
        if humanStrategy == BORING:
            playerMove = playBoringly(playerHistory)
        if humanStrategy == SORE:
            playerMove = playSorely(playerHistory[counter-1], computerHistory[counter-1])
        if humanStrategy == PATTERNED:
            playerMove = playPatterned(playerHistory[counter-1])

        computerMove = chooseBestMove(playerHistory, computerHistory)
           
    result = calculateOutcome (playerMove, computerMove)
    if result == 1:
        computerWins = computerWins + 1
    elif result == -1:
        playerWins = playerWins + 1
    else:
        ties = ties + 1

    playerHistory.append(playerMove)
    computerHistory.append(computerMove)

    if result == 1:
        description = "Computer won."
    if result == -1:
        description = "Computer lost."
    if result == 0:
        description = "Tie."
        
    print("Game %d: Player %s, Computer %s. %s" %(counter+1, playerMove, computerMove, description))
            
print ("")
print ("Over %d games, the computer won %2.0f percent." % (maxGames, (100*computerWins/maxGames)))
print ("")
print ("The final chains were:")
printChains()
     
