# prime number
def check_prime(num):
    count = 0
    for i in range(2, num):
        if num % i == 0:
            count += 1

    if count == 0:
        print("Prime")
    else:
        print("not prime")


number = int(input("Enter a number"))
check_prime(number)
