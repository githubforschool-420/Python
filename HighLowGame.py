# import random

# maxNum = input("What do you want the maximum number to be?\n")

# choice = random.randint(0, int(maxNum))

# guess = input("A number from 1 to " + maxNum + " has been chosen, guess what it is: ")

# if guess == choice:
#     print("Correct! The number was " + str(guess) + "!")
# else:
#     print("Wrong! The number was " + str(choice) + "!")

import random

maxNum = input("What do you want the maximum number to be?\n")
minNum = "1"

choice = random.randint(int(minNum), int(maxNum))
hintValue = int((int(minNum) + int(maxNum)) / 2)

def runTheNumbers():
    hintValue = int((int(minNum) + int(maxNum)) / 2)
    guess = input("\nA number from " + str(minNum) + " to " + str(maxNum) + " has been chosen! Guess if it is 'higher' or 'lower' than " + str(hintValue) + ": \n")
    if guess == "higher" and choice >= hintValue:
        print("\nYes! The number is higher than " + str(hintValue))
        runTheNumbers()
    elif guess == "lower" and choice <= hintValue:
        print("\nYes! The number is lower than " + str(hintValue))
        runTheNumbers()
    elif guess == "higher" and choice <= hintValue:
        print("\nNope! Guess again:")
        runTheNumbers()
    elif guess == "lower" and choice >= hintValue:
        print("\nNope! Guess again:")
        runTheNumbers()

runTheNumbers()