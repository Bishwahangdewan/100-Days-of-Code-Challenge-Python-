# head or tail
# One cool thing about random seed is that if you add the same seed number its going to output same random number

import random

test_seed = int(input("Create a Seed Number "))
random.seed(test_seed)

toss = random.randint(1, 2)

if toss ==1:
    print("Heads")
else:
    print("Tails")



