# higher Lower Game

from data import compare_data
from random import randint


def compare(A, B):
    print(f"Compare A : {A['name']}, {A['description']}, {A['country']}")
    print("VS")
    print(f"Against B : {B['name']}, {B['description']}, {B['country']}")
    choice = input("Who has more Followers? Type A or B : ")
    winner = {}
    loser = {}

    # compare
    if A['follower_count'] > B['follower_count']:
        winner = A
        loser = B
        winner['label'] = 'A'
    else:
        winner = B
        loser = A
        winner['label'] = 'B'

    # check if my input is equal to winner
    if choice == winner['label']:
        print(f"You are Correct")
        print(f"{winner['name']} has {winner['follower_count']} "
              f"followers whereas  {loser['name']} has {loser['follower_count']} followers")
        return winner

    else:
        print("You are wrong")
        print(f"{loser['name']} has {loser['follower_count']} "
              f"followers but  {winner['name']} has {winner['follower_count']} followers")
        return 0


score = 0
data_length = len(compare_data)
index_a = randint(0, data_length - 1)
index_b = randint(0, data_length - 1)

A = compare_data[index_a]
B = compare_data[index_b]
print(A)
print(B)

print("-----WELCOME TO HIGHER LOWER GAME------- \n \n")


def continue_program(A, B, your_score):
    result = compare(A, B)
    if result:
        A = result
        newIndex = randint(0, data_length - 1)
        B = compare_data[newIndex]
        your_score += 1
        print(f"Your score is {your_score}")
        continue_program(A, B, your_score)
    else:
        print(f"Your score is {your_score}")
        print(f"Game Over")


continue_program(A, B, score)
