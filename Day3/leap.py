#leap year
#year which is didvisible by 4 , except it is divisible by 100 , unless it is divisible by 400

year = int(input("Enter a year "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("It is a leap year")
        else:
            print("It is not a leap year")
    else:
        print("It is a leap year")
else:
    print("It is not a leap year")
