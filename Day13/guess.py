# number guessing game
import random

print("-----WELCOME TO NUMBER GUESSING GAME ------")
print("-----I'm thinking of a number between 1 to 100 ------")
difficulty = input("Choose a Difficulty: Easy or Hard\n")

correct_number = random.randint(0, 100)


# give attempts to the user
def pick_attempts(difficulty):
    if difficulty == 'easy':
        return 10
    elif difficulty == 'hard':
        return 5
    else:
        return 0


attempts = pick_attempts(difficulty)


# check the number
def check_number(your_num, attemp):
    if your_num == correct_number:
        print(f"YAY ! You guessed the correct number. {correct_number} was the number I was thinking of.")
        attemp = -1
    elif your_num > correct_number:
        print("You guessed it too high! ")
        attemp -= 1
    elif your_num < correct_number:
        print("You guessed it too low! ")
        attemp -= 1

    return attemp


while (attempts > 0):
    print(f"You have {attempts} attempts to guess the number")
    your_number = int(input("Pick a random number from 0 to 100\n"))

    new_attempt = check_number(your_number, attempts)
    attempts = new_attempt


if attempts == 0:
    print(f"YOU DONT HAVE ANY ATTEMPTS LEFT . THE CORRECT NUMBER WAS {correct_number}")
    print("GAME_OVER")

