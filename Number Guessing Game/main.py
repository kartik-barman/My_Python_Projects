# Number Guessing Game In random Function or Method

import random

randomNumber = random.randrange(1,10);
# print(randomNumber)

print("Number Guessing Game\n")

userInput = int(input("Enter Your Guessing Number : "))

if ( userInput > randomNumber ):
    print("Guessing Number is Too High", randomNumber)
elif ( userInput < randomNumber ):
    print("Guessing Number is too Low", randomNumber)
else:
    print("You have Won.🏆\nYour Guessing Number Is Match")