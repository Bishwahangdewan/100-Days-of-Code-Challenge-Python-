#Fizzbuzz take numbers 1-100
#if the no is divided by 3 print fizz , if divisible by 5 print buzz, if divisible by both print fizzbuzz

for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
    elif number % 5 == 0:
        print("buzz")
    elif number % 3 == 0:
        print("fizz")
    else:
        print(number)



