#ROCK PAPER SCISSOR

import random

print("--------WELCOME TO ROCK PAPER SCISSOR GAME --------------")

you = int(input("Choose 0 for Rock 1 for Paper 2 for Scissor "))

if you == 0:
    print("You choose Rock ")
elif you == 1:
    print("You choose Paper")
else:
    print("You choose Scissor")


comp = random.randint(0,2)

if comp == 0:
    print("Computer chooses Rock ")
elif comp == 1:
    print("Computer chooses Paper")
else:
    print("Computer chooses Scissor")


if you == comp:
    print("It's a tie ")
elif you == 0 and comp == 1:
    print("Computer Wins !")
elif you == 0 and comp == 2:
    print("You win !")
elif you == 1 and comp == 0:
    print("You Win !")
elif you == 1 and comp == 2:
    print("Computer wins !")
elif you == 2 and comp == 0:
    print("Computer Wins !")
elif you == 2 and comp == 1:
    print("You win !")
else:
    print("IDK")

