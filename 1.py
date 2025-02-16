# THE COMPUTER ALWAYS WINS
# MIT PRESS
#
# CodeLink 1
# Wordle
# last revised 12/25/24
#
# In this code, the computer guesses randomly.  Not great.
# Can you implement our better algorithm by rewriting guessWord()?
# You might need to add some other functions also.  For instance,
# as you make guesses, you will want to eliminate incorrect words
# from the wordList.
#
# Note that this demo uses only the 18 words from Chapter One, so that
# the code runs quickly.  Once you have revised the code, feel free to
# replace the wordList with something much longer.


import random

# FUNCTIONS

def makeGreen (letter):
    return "G"

def makeYellow (letter):
    return "Y"

def scoreGuess(guess, hiddenWord):
    # returns Y for yellow letters, G for green, blank otherwise
    # when you code, you will use this information to pick your next guess

    hiddenLettersUsed = [False, False, False, False, False]
    guessLettersUsed = [False, False, False, False, False]
    colors = ["_", "_", "_", "_", "_"]
    
    # go through the guess and makeGreen any matches
    for letter in range(5):
        if guess[letter] == hiddenWord[letter]:
            hiddenLettersUsed[letter] = True
            guessLettersUsed[letter] = True
            colors[letter] = makeGreen(guess[letter])

    # then go through the guess and makeYellow any remaining matches
    for letter in range(5):
        if guessLettersUsed[letter] == False:
            for possibleMatch in range(5):
                if guessLettersUsed[letter] == False and hiddenWord[possibleMatch] == guess[letter] and hiddenLettersUsed[possibleMatch] == False:
                    guessLettersUsed[letter] = True
                    hiddenLettersUsed[possibleMatch] = True
                    colors[letter] = makeYellow(guess[letter])

    return(colors)
    
def hideWord(availableWords):
    # this function randomly chooses one word from the list

    randomChoice = random.randint(0,len(availableWords)-1)
    chosenWord = availableWords[randomChoice]

    return chosenWord

def guessWord(availableWords):

    # this function randomly choose one word from the list
    # you will replace this code with your better algorithm

    randomChoice = random.randint(0,len(availableWords)-1)
    chosenWord = availableWords[randomChoice]

    return chosenWord
   
# ############
# main program
# ############

wordList = ["adept","after","agent","avert","cater","eaten","eater","extra","hater","taken","taker","water","great","treat","wheat","taper","tread","tweak"]

# initialize variables
hiddenWord = hideWord(wordList)
guess = ""
counter = 0

print("")
print("The hidden word is %s." % hiddenWord)
print ("")

while guess != hiddenWord:

    guess = guessWord(wordList)
    counter = counter + 1
    print ("Computer guesses: ", guess)

print ("")
print ("The computer needed %d guesses." % counter)
