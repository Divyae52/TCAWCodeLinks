# THE COMPUTER ALWAYS WINS
# MIT PRESS
#
# CodeLink 19
# Regret-Based Rock, Paper, Scissors
# last revised 12/25/24

# As you look at the output, do you see the computer improving its strategy as
# it plays more games?  And do things stabilize after 50 games? 100? More?
# Does the code work regardless of what starting strategy you use?

# function definitions
# ####################

def score(myStrategy, yourStrategy):

    points = 0.0

    points = points + 0 * (myStrategy[0]*yourStrategy[0])   # rock, rock
    points = points - 1 * (myStrategy[0]*yourStrategy[1])   # rock, paper
    points = points + 1 * (myStrategy[0]*yourStrategy[2])   # rock, scissors
    points = points + 1 * (myStrategy[1]*yourStrategy[0])   # paper, rock
    points = points + 0 * (myStrategy[1]*yourStrategy[1])   # paper, paper
    points = points - 1 * (myStrategy[1]*yourStrategy[2])   # paper, scissors
    points = points - 1 * (myStrategy[2]*yourStrategy[0])   # scissors, rock
    points = points + 1 * (myStrategy[2]*yourStrategy[1])   # scissors, paper
    points = points + 0 * (myStrategy[2]*yourStrategy[2])   # scissors, scissors

    return points


# main program
# ############

# define constants
ROCK = 0
PAPER = 1
SCISSORS = 2
playRock = [1,0,0]
playPaper = [0,1,0]
playScissors = [0,0,1]

# define variables
computer1Strategy = [0.3,0.2,0.5]   # arbitrary starting strategy
computer2Strategy = [0.0,0.4,0.6]   # arbitrary starting strategy
computer1Regret = [0,0,0]
computer2Regret = [0,0,0]

# Computer1 has a strategy.
# Computer2 has a strategy.
# So now let's update them.

iterations = 0

while iterations < 200:

    # FIRST, LOOK AT COMPUTER1'S EXPERIENCE
    
    # how does computer1 currently do?
    expectedOutcome = score(computer1Strategy, computer2Strategy)
        
    # had computer1 chosen to play Rock, would computer1 have done better?
    possibleOutcome = score(playRock, computer2Strategy)
    if possibleOutcome > expectedOutcome:
        regret = possibleOutcome - expectedOutcome
        computer1Regret[ROCK] = computer1Regret[ROCK] + regret

    # now the same analysis but for Paper
    possibleOutcome = score(playPaper, computer2Strategy)
    if possibleOutcome > expectedOutcome:
        regret = possibleOutcome - expectedOutcome
        computer1Regret[PAPER] = computer1Regret[PAPER] + regret

    # then Scissors
    possibleOutcome = score(playScissors, computer2Strategy)
    if possibleOutcome > expectedOutcome:
        regret = possibleOutcome - expectedOutcome
        computer1Regret[SCISSORS] = computer1Regret[SCISSORS] + regret

    # calculate total regret so far
    totalRegret = computer1Regret[ROCK] + computer1Regret[PAPER] + computer1Regret[SCISSORS]

    # and update computer1's strategy
    if totalRegret != 0:
        computer1Strategy[ROCK] = computer1Regret[ROCK]/totalRegret
        computer1Strategy[PAPER] = computer1Regret[PAPER]/totalRegret
        computer1Strategy[SCISSORS] = computer1Regret[SCISSORS]/totalRegret    

    # NOW, DO THE SAME THING FOR COMPUTER2
    
    # how does computer2 currently do?
    expectedOutcome = score(computer2Strategy, computer1Strategy)
        
    # had computer2 chosen to play Rock, how much would computer2 have done better?
    possibleOutcome = score(playRock, computer1Strategy)

    if possibleOutcome > expectedOutcome:
        regret = possibleOutcome - expectedOutcome
        computer2Regret[ROCK] = computer2Regret[ROCK] + regret

    # had computer2 chosen to play Paper, how much would computer2 have done better?
    possibleOutcome = score(playPaper, computer1Strategy)

    if possibleOutcome > expectedOutcome:
        regret = possibleOutcome - expectedOutcome
        computer2Regret[PAPER] = computer2Regret[PAPER] + regret

    # had computer2 chosen to play Scissors, how much would computer2 have done better?
    possibleOutcome = score(playScissors, computer1Strategy)

    if possibleOutcome > expectedOutcome:
        regret = possibleOutcome - expectedOutcome
        computer2Regret[SCISSORS] = computer2Regret[SCISSORS] + regret

    # now, update Computer 2's strategy
    totalRegret = computer2Regret[ROCK] + computer2Regret[PAPER] + computer2Regret[SCISSORS]
    
    if totalRegret != 0:
        computer2Strategy[ROCK] = computer2Regret[ROCK]/totalRegret
        computer2Strategy[PAPER] = computer2Regret[PAPER]/totalRegret
        computer2Strategy[SCISSORS] = computer2Regret[SCISSORS]/totalRegret    

    # THAT IS ONE FULL ITERATION
    iterations = iterations + 1

    # REPORT BACK SOME INFORMATION AS THE COMPUTER WORKS
    if iterations%10 == 0:
        print ("")
        print ("After %d games:" % iterations)
        print ("Computer 1: %0.2f %0.2f %0.2f." %(computer1Strategy[0], computer1Strategy[1], computer1Strategy[2]))
        print ("Computer 2: %0.2f %0.2f %0.2f." %(computer2Strategy[0], computer2Strategy[1], computer2Strategy[2]))

print("")
print("")





