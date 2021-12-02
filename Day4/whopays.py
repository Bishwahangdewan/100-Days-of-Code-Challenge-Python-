# input people and see who pays the bill
#You can do the same thing with lesser code using choice() eg: random.choice(names) gives random name

import random

test_seed = input("Enter seed number ")
random.seed(test_seed)

people = input("Enter the names separated by a ," )
names = people.split(',')

length = len(names)

random_number = random.randint(0,length-1)

print(names)
print(random_number)
print(f"The person who pays the bill is {names[random_number]}")

