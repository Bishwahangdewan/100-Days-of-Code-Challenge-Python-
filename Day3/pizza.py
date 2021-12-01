#Pizza Bill calculator
# small pizza = 15 , medium pizza = 20 , large pizza = 25
#peporoni for small pizza = 2 . pep for med and large pizza =3
#extra cheese $ 1

print("--------------Welcome to Python Pizza--------------")

pizza_size = input("Which size do you want ? \n Enter S for small Pizza , M for medium pizza , L for Large Pizza ")

price = 0

if pizza_size == 'S':
    price += 15
elif pizza_size == 'M':
    price += 20
elif pizza_size == 'L':
    price += 25
else:
    print("Please Enter correct size")

pep = input("Do you want pepperoni ? Y or N ")

if pep == 'Y':
    if pizza_size == 'S':
        price += 2
    else:
        price += 3


cheese = input("Do you want extra cheese? Y or N ")

if cheese == 'Y':
    price += 1

print(f"You total bill is ${price}")
