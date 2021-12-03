# find the total od all even numbers from 1-100
# the range function helps us loop through a given range of numbers

evensum = 0

for number in range(1,101):
    if number % 2 == 0:
        evensum += number

print(f"Sum of all even numbers is {evensum}")