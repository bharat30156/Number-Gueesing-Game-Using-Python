# Number Gueesing Game 
#@author Bharat
# Just for practice 

import random

secret = random.randint(1, 100)
guess  = 0
tries = 0

print("i have a secret for you!")
print("It is a number between 1 to 100! you can guess it.")

# try until they guess it or runs out of turn 
while guess != secret and tries < 6:
    guess = int(input("What's your guess")) # what is the guess of player 
    if guess < secret:
        print("Too low! Better luck next time. ")
    if guess > secret:
        print("Too High! Better Luck nexrt Time>")
    tries = tries + 1

# print the message at the end of the game 
if guess == secret:
    print("your Guess was correct! congrulations.")
else :
    print("No more guesses! Better Luck next Time.")
    print("The secret Number was ", secret)