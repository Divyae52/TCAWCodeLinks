# THE COMPUTER ALWAYS WINS
# MIT PRESS
#
# CodeLink 1
# Wordle
# last revised 5/24/25
#
# In this code, the computer guesses randomly.  Not great.
# Can you implement our better algorithm by rewriting guessWord()?
#
# Note that this demo uses only the 18 words from Chapter One. The idea
# is to keep things simple so that we can really see what happens at
# every step. Once you have revised the code, however, feel free to
# replace the wordList with something much longer.

import random

# FUNCTIONS

def scoreGuess(guess, hiddenWord):
    # returns Y for yellow letters, G for green, blank otherwise
    # when you code, you will use this information to pick your next guess

    hiddenLettersUsed = [False, False, False, False, False]
    guessLettersUsed = [False, False, False, False, False]
    colors = ["_", "_", "_", "_", "_"]

    # go through the guess and make any matches green
    for letter in range(5):
        if guess[letter] == hiddenWord[letter]:
            hiddenLettersUsed[letter] = True
            guessLettersUsed[letter] = True
            colors[letter] = "G"

    # then go through the guess and make any remaining matches yellow
    for letter in range(5):
        if guessLettersUsed[letter] == False:
            for possibleMatch in range(5):
                if guessLettersUsed[letter] == False and hiddenWord[possibleMatch] == guess[letter] and \
                        hiddenLettersUsed[possibleMatch] == False:
                    guessLettersUsed[letter] = True
                    hiddenLettersUsed[possibleMatch] = True
                    colors[letter] = "Y"

    return (colors)


def hideWord(availableList):
    # this function randomly chooses one word from the list

    randomChoice = random.randint(0, len(availableList) - 1)
    chosenWord = availableList[randomChoice]

    return chosenWord


def removeDuds(availableList, previousOutcome, previousGuess):
    # remove words that could not have given us the previousOutcome
    # also remove the word that was guessed unsuccessfully

    newList = []

    for word in availableList:
        if scoreGuess(previousGuess, word) == previousOutcome:
            if previousGuess != word:
                newList.append(word)

    return newList


def guessWord(availableList, wordList):
    # this function randomly chooses one word from the words that are still available
    # you will replace this code with a better algorithm
    # in that algorithm, the computer will guess the optimal word out of all the words the computer knows (wordList)
    # and the computer will know that the hidden word is one of the words in availableList
    
    randomChoice = random.randint(0, len(availableList) - 1)
    chosenWord = availableList[randomChoice]

    return chosenWord


# ############
# main program
# ############

# make a list of all the words the computer knows
wordList = ["adept", "after", "agent", "avert", "cater", "eaten", "eater", "extra", "hater", "taken", "taker", "water",
            "great", "treat", "wheat", "taper", "tread", "tweak"]

# make a separate list that will be updated to keep track of which words might still be the hidden word
availableList = []
for word in range(len(wordList)):
    availableList.append(wordList[word])

# initialize other variables
hiddenWord = hideWord(availableList)
guess = ""
counter = 0

print("")
print("The hidden word is %s." % hiddenWord)
print("")

while guess != hiddenWord:
    guess = guessWord(availableList, wordList)
    counter = counter + 1
    print("Computer guesses: ", guess)
    outcome = scoreGuess(guess, hiddenWord)
    availableList = removeDuds(availableList, outcome, guess)
    print("  ", len(availableList), "words remaining.")

    # failsafe to stop infinite loops
    if counter > len(wordList):
        print("Something has gone wrong - try again!")
        break

print("")
print("The computer needed %d guesses." % counter)
