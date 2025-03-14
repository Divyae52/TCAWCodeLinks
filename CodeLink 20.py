# THE COMPUTER ALWAYS WINS
# MIT PRESS
#
# CodeLink 20
# Colonel Blotto
# last revised 12/25/24

# We made it! This is the final CodeLink from the book: an implementation of the
# regret algorithm for the game Blotto.  Be sure to play with the code to see how
# things change when you alter the number of allowed iterations, when you set
# different starting strategies, and so on.  Then, as the chapter suggests, see
# if you can build versions of the code that give each battlefield a different
# value or allow different troop deployments.  Do you agree with the computer's
# strategies for even these more complicated versions of the game?

# function definitions
# ####################

def nicePrint(theArray):

    for counter in range(len(theArray)):
        print ("%d : " %counter, end="")
        print(theArray[counter])


def score(myStrategy, yourStrategy, possibleDeployments):

    numPossible = len(possibleDeployments)
    totalPoints = 0.0
    
    # consider all possible deployment combinations
    for myMove in range(1, numPossible):
        for yourMove in range(1, numPossible):

            battlesWon = 0
            oddsThisCombo = myStrategy[myMove] * yourStrategy[yourMove]

            # evaluate the three fields
            for field in range(3):
                mySoldiers = possibleDeployments[myMove][field]
                yourSoldiers = possibleDeployments[yourMove][field]
                if mySoldiers > yourSoldiers:
                    battlesWon = battlesWon + 1
                if mySoldiers < yourSoldiers:
                    battlesWon = battlesWon - 1
                    
            totalPoints = totalPoints + oddsThisCombo * battlesWon
            
    return totalPoints


# main program
# ############

# variable definitions
numSoldiers = 5
numPossibleDeployments = 0
possibleDeployments = []
possibleDeployments.append([0,0,0])     # we will not be using possibleDeployments[0]

# generate the list of possibleDeployments in this context
for field1Soldiers in range(0,numSoldiers+1):
    for field2Soldiers in range(0,numSoldiers+1):
        for field3Soldiers in range(0,numSoldiers+1):
            if (field1Soldiers + field2Soldiers + field3Soldiers == numSoldiers):
                numPossibleDeployments += 1
                possibleDeployments.append([field1Soldiers, field2Soldiers, field3Soldiers])


# variables with length based on numPossibleDeployments
computer1Strategy = []
computer2Strategy = []
computer1Regret = []
computer2Regret = []
testStrategy = []

# establish those variables, skipping the [0] location
computer1Strategy.append(0.0)
computer2Strategy.append(0.0)
computer1Regret.append(0.0)
computer2Regret.append(0.0)
testStrategy.append(0.0)

for counter in range(numPossibleDeployments):
    computer1Strategy.append(1/numPossibleDeployments)  # start by treating all deployments the same
    computer2Strategy.append(1/numPossibleDeployments)  
    testStrategy.append(0.0)
    computer1Regret.append(0.0)
    computer2Regret.append(0.0)


# main loop
iterations = 0

while iterations < 1000:

    # how does computer1 currently do?
    currentOutcome = score(computer1Strategy, computer2Strategy, possibleDeployments)

    # loop through all the possible strategies the computer could have played
    
    for counter in range(1, numPossibleDeployments+1):
        for counter2 in range(1, numPossibleDeployments+1):
            testStrategy[counter2] = 0.0
        testStrategy[counter] = 1.0

        # had computer1 chosen this testStrategy, would computer1 have done better?
        alternativeOutcome = score(testStrategy, computer2Strategy, possibleDeployments)

        if alternativeOutcome > currentOutcome:
            regret = alternativeOutcome - currentOutcome
        else:
            regret = 0

        # keep track of the regret
        computer1Regret[counter] = computer1Regret[counter] + regret

    # after all deployments have been considered, update computer1's strategy
    totalRegret = 0

    for counter in range(1, numPossibleDeployments+1):
        totalRegret = totalRegret + computer1Regret[counter]

    if totalRegret != 0:
        for counter in range(1, numPossibleDeployments+1):
            computer1Strategy[counter] = computer1Regret[counter]/totalRegret
              
    # how does computer2 currently do?
    currentOutcome = score(computer2Strategy, computer1Strategy, possibleDeployments)
        
    # had computer2 chosen other strategies, by how much would computer2 have done better?
    for counter in range(1, numPossibleDeployments+1):
    # counter is the pure strategy we would pick
    # the hybrid would zero all others except this one

        for counter2 in range(1, numPossibleDeployments+1):
            testStrategy[counter2] = 0.0
        testStrategy[counter] = 1.0
        
        alternativeOutcome = score(testStrategy, computer1Strategy, possibleDeployments)

        if alternativeOutcome > currentOutcome:
            regret = alternativeOutcome - currentOutcome
        else:
            regret = 0
            
        computer2Regret[counter] = computer2Regret[counter] + regret

    # update player 2's strategy
    totalRegret = 0
    for counter in range(1, numPossibleDeployments+1):
        totalRegret = totalRegret + computer2Regret[counter]

    if totalRegret != 0:
        for counter in range(1, numPossibleDeployments+1):
            computer2Strategy[counter] = computer2Regret[counter]/totalRegret
            
    iterations = iterations + 1

print ("")
print (" RESULTS FOR PLAYER 1")
print ("**********************")
print (" Pattern   Frequency")
for counter in range(1, numPossibleDeployments+1):
    print(possibleDeployments[counter], end="")
    print ("     %2.2f" % computer1Strategy[counter])
print ("")

print (" RESULTS FOR PLAYER 2")
print ("**********************")
print (" Pattern   Frequency")
for counter in range(1, numPossibleDeployments+1):
    print(possibleDeployments[counter], end="")
    print ("     %2.2f" % computer2Strategy[counter])




