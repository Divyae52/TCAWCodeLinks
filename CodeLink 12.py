# THE COMPUTER ALWAYS WINS
# MIT PRESS
#
# CodeLink 12
# Throwing Darts Blackjack
# last revised 12/25/24
#
# Chapter Eight develops an aim-the-darts Blackjack implementation, so we
# need to first build a throw-the-darts version that we can use to evaluate
# the revised algorithm. Thus, the code here is a lot like last chapter's 2048
# code in that it uses random simulations but does not think much about which
# simulations to run.


import random

# global definitions
hidden = True           # there is a hidden card on the table
final = True            # this is a final hand, not a hand in progress
numSimulations = 500    # how many simulations are allowed for each move type
gamesTotal = 1000       # how many rounds of BlackJack to play
STAND = 0               # a constant
TAKE = 1                # a constant


# compare computer's move to optimal
def optimalMove (computerHand, dealerCard):

    computerValue = valueHand(computerHand)
    
    if 1 in computerHand:
        if computerValue < 18:
            return TAKE
        if computerValue == 18:
            if dealerCard in [9, 10, 11, 12, 13, 1]:
                return TAKE
            else:
                return STAND
        if computerValue > 18:
            return STAND
 
    if computerValue < 12:
        return TAKE

    if computerValue == 12:
        if dealerCard in [4, 5, 6]:
            return STAND
        else:
            return TAKE
 
    if computerValue > 12 and computerValue < 17:
        if dealerCard in [7, 8, 9, 10, 11, 12, 13, 1]:
            return TAKE
        else:
            return STAND

    if computerValue > 16:
        return STAND
    
    

# printing functions

def nicePrintArray (values):

    for item in values:
        print ("%6d " %item, end="")
    print ("")
    
def nicePrintCard (card):

    if card == 1:
        print("A ", end="")
    elif card == 11:
        print ("J ", end="")
    elif card == 12:
        print ("Q ", end="")
    elif card == 13:
        print ("K ", end="")
    else:
        print ("%d " %card, end="")

def nicePrintHand (hand):

    for card in hand:
        nicePrintCard(card)
    print ("")

    
# card handling functions
    
def newCard(deck):
    # receives deck of cards as an array, using positions 1 through 13, with possibly some removed
    # returns the array number of the card to offer (1=Ace, 11=Jack, 12=Queen, 13=King)

    # count how many cards are left in the deck

    cardsLeft = 0
    for counter in range(1,14):
        cardsLeft = cardsLeft + deck[counter]

    # choose one ## CONFIRM THIS RANGE DOUG
    nextCard = random.randint(1,cardsLeft)

    # identify it; for example, if there are 4 aces then card 5 is a 2
    cardsSeen = 0
    position = 1
    while (cardsSeen + deck[position]) < nextCard:
        cardsSeen = cardsSeen + deck[position]
        position += 1

    # remove that card from the deck
    deck[position] = deck[position] - 1

    return position
            
            
def valueHand(hand):
    # score the hand
     
    value = 0
    hasAce = False

    for card in hand:
        if card == 1:
            hasAce = True           
        else:
            if card >= 10:
                value = value + 10
            else:
                value = value + card

    if hasAce == True:
        # treat an ace as 11, unless that causes a bust
        
        if (value + 11) > 21:
            value = value + 1
        else:
            value = value + 11

    return value



def makeHand(cards):
    # create a copy of the hand so that the code can experiment with it

    hand = []

    for counter in range(len(cards)):
        hand.append(cards[counter])

    return hand


def makeDeck(computerCards, dealerCards, isHidden):
    # create a copy of the deck so that the code can experiment with it
    # be sure to remove cards that are already known to be used
    # during simulations, the hidden card is not known and so not removed
    
    # create a new 52-card deck
    deck = []
    deck.append(0)              # don't use the 0 location
    for counter in range(1,14):
        deck.append(4)

    for card in computerCards:
        deck[card] = deck[card]-1

    if isHidden:
        # remove only the revealed card from the deck
        revealedCard = dealerCards[0]
        deck[revealedCard] = deck[revealedCard] - 1
    else:
        # remove all used cards
        for card in dealerCards:
            deck[card] = deck[card]-1
 
    return deck



def scoreGame(computerHand, dealerHand):
    # return 1 if computer won
    # return -1 if dealer won
    # return 0 otherwise

    computerScore = valueHand(computerHand)
    dealerScore = valueHand(dealerHand)

    if computerScore > 21:
        return -1

    if dealerScore > 21:
        return 1

    if computerScore > dealerScore:
        return 1

    if dealerScore > computerScore:
        return -1
    
    else:
        return 0
    


def playRandomly (computerCards, dealerCards):

    # make local copy of hand to experiment with
    computerHand = makeHand(computerCards)
        
    # computer is done if reached 21, or busted
    if (valueHand(computerHand) > 20):
        finished = True
    else:
        finished = False

    while not finished:

        # make a deck to work with; note: the dealer has a hidden card
        deck = makeDeck(computerHand, dealerCards, hidden)
     
        # randomly choose to take(0) or stand(1)
        chosenMove = random.randint(0,1)

        if chosenMove == 0:
            # take
            drawnCard = newCard(deck)
            computerHand.append(drawnCard)

        else:
            # stand
            finished = True

        if valueHand(computerHand)>20:
            finished = True

    # create a  local version of the dealer's hand to experiment with
    dealerHand = makeHand(dealerCards)
    
    # the dealer plays until 17 in response
    dealerHand = playTo17(computerHand, dealerHand, hidden)

    return scoreGame(computerHand, dealerHand)


def playTo17(computerCards, dealerCards, isHidden):
    # computer plays until 17 or more

    # make local hand and deck to experiment with
    dealerHand = makeHand(dealerCards)
    
    if isHidden:
        # simulate as if the hidden card is not in the dealer's hand
        deck = makeDeck (computerCards, dealerHand, hidden)
        hiddenCard = dealerCards[1]
        dealerHand.remove(hiddenCard)
                
    else:
        # actually playing now, so hidden card is known
        deck = makeDeck(computerCards, dealerCards, not hidden)
        
    dealerScore = valueHand(dealerHand)

    while dealerScore < 17:
        drawnCard = newCard(deck)
        dealerHand.append(drawnCard)
        dealerScore = valueHand(dealerHand)
        deck[drawnCard]-= 1

    return dealerHand
    

def findBestMove (computerCards, dealerCards):
    
    # create the deck of cards
    deck = makeDeck(computerCards, dealerCards, hidden)

    # create sample hand to experiment with
    computerHand = makeHand(computerCards)

    # prepare to track wins from taking a card
    totalWins = 0
    
    for counter in range(numSimulations):
        # draw a card
        drawnCard = newCard(deck)
        computerHand.append(drawnCard)

        # randomly simulate the computer's moves
        totalWins += playRandomly(computerHand, dealerCards)

        # reset to simulate again
        computerHand.remove(drawnCard)
        deck = makeDeck(computerHand, dealerCards, hidden)

    # how did we do by taking at least one card?
    takeAverage = totalWins / numSimulations
    
    # prepare to track wins from standing
    totalWins = 0

    # create sample dealer hand to experiment with
    dealerHand = makeHand(dealerCards)

    for counter in range(numSimulations):
        # play against the computer's original cards until 17 or more
        dealerHand = playTo17(computerCards, dealerHand, hidden)
        totalWins += scoreGame(computerCards, dealerHand)

    # and how do we do by standing?
    holdAverage = totalWins / numSimulations
    
    # choose the better move
    if takeAverage > holdAverage:
        return TAKE
    else:
        return STAND
    


# ############
# main program
# ############

# initialize the variables for the big run of games

# the baseline variables
computerWins = 0
computerTies = 0
gamesPlayed = 0

print ("")
print ("I am simulating %d games of blackjack." % gamesTotal)
       
while gamesPlayed < gamesTotal:

    # no one has cards yet
    computerHand = []
    dealerHand = []
      
    # create a new 52-card deck
    deck = makeDeck(computerHand, dealerHand, not hidden)

    # give the computer one card
    takeCard = newCard(deck)
    computerHand.append(takeCard)
    deck[takeCard] -=1

    # give the dealer their revealed card
    takeCard = newCard(deck)
    dealerHand.append(takeCard)
    deck[takeCard] -=1

    # give the computer their second card
    takeCard = newCard(deck)
    computerHand.append(takeCard)
    deck[takeCard] -=1

    # give the dealer their secret card
    takeCard = newCard(deck)
    dealerHand.append(takeCard)
    deck[takeCard] -=1

    # let the computer play
    finished = False
    while not finished:

        if (findBestMove(computerHand, dealerHand) == TAKE):
            takeCard = newCard(deck)
            deck[takeCard] -= 1
            computerHand.append(takeCard)
        else:
            finished = True

        # check to see if we should stop
        if valueHand(computerHand) > 20:
            finished = True

    # dealer now can take more cards, up to 17        
    dealerHand = playTo17(computerHand, dealerHand, not hidden)

    # see who won
    result = scoreGame(computerHand, dealerHand)
    if result == 1:
        computerWins = computerWins + 1
    if result == 0:
        computerTies = computerTies + 1

    gamesPlayed = gamesPlayed + 1


# report summary statistics
computerLosses = gamesPlayed - computerWins - computerTies
print ("Games played:    %5d" % gamesPlayed)
print ("Computer wins:   %5d" % computerWins)
print ("Computer losses: %5d" % computerLosses)
print ("Tie games:       %5d" % computerTies)
print ("")
