# password generator project
# random choice function picks a random element from a list
# random shuffle shuffles the list . It does not return anything
# to convert list into string simply use join()

import random


alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
             'Q', 'R', 'S', 'T', 'U','V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['$', '(', ')', '#', '%', '&']

print("------------WELCOME TO PASSWORD GENERATOR----------------------")

no_alpha = range(int(input("How many alphabets do you want? ")))

no_numbers = range(int(input("How many numbers do you want? ")))

no_symbols = range(int(input("How many symbols do you want? ")))

password = ''

for x in no_alpha:
    password += str(random.choice(alphabets))

for y in no_numbers:
    password += str(random.choice(numbers))

for z in no_symbols:
    password += str(random.choice(symbols))

list_password = list(password)
random.shuffle(list_password)
final_password = ""

print(f"Your password is {final_password.join(list_password)}")





