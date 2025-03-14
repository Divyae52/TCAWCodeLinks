# THE COMPUTER ALWAYS WINS
# MIT PRESS
#
# CodeLink 17
# Imitation
# last revised 12/25/24

# There are countless ways to build an imitation engine using the ideas from
# Chapter Ten. I suggest starting with something simple that is easy to debug,
# and then later adding more complicated details.  For instance, maybe start
# by searching the sample text to identify every unique 4-character phrase.
# Then, for each phrase, take note of what characters come next, and how often
# each of those characters is used in the sample text.  Using that information,
# you can generate text that follows patterns similar to the sample's patterns.

# Note that this code will not run as-is.  This is just a framework for your
# program, but this is not actual code that is ready to execute.


import random

# function definitions
# ####################

def makeChain (sample):

    # Use this function to build a chain based on some sample text.
    # Think about how you want to structure the chain so that it has all the info you need.

    chain = []
    
    print ("This function needs to be written.")
    
    return chain
        


def talk (chain, starter):

    # This function receives the chain plus a starter phrase.
    # From there, the function prints one letter at a time, each picked using the chain.
    # For now, stop after 300 letters have been printed to the screen.

    print ("This function also needs to be written.")
    
    
# main program
# ############

# NOTE:
# Use simple sample text for now, again to help us debug.  Later, we can swap out the simple text
# and instead use Taylor Swift lyrics or Shakespearean prose.

# define variables
trainedChain = []
sample = "This dog. This cat. This dog. This horse. This dog. This mouse. This dog. This rat. This dog."

# use the two functions defined above
trainedChain = makeChain(sample)
talk(trainedChain, "This")

print(" ... Enough.")
print()
print()
