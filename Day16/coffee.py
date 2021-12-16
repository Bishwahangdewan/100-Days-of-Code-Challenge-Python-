# Coffee Machine Code

from menu import Menu
from calc import Calculate
from coins import Coins

coffee_maker_menu = Menu()
coffee_menu = coffee_maker_menu.coffee_menu
resources = coffee_maker_menu.resources

calculate_coffee = Calculate(resources, coffee_menu)
calculate_coins = Coins()

should_continue = True

while should_continue:

    your_option = input("What Would you like (espresso / latte / cappuccino) ? ")

    if your_option == 'report':
        calculate_coffee.show_report()
    else:
        calculate_coffee.make = your_option
        # check for resources
        can_make_coffee = calculate_coffee.check_resources()
        if can_make_coffee:
            calculate_coins.quarter = int(input("How Many Quarters (1 Quarter = $0.25)?  "))
            calculate_coins.dime = int(input("How Many Dimes (1 Dime = $0.10)?  "))
            calculate_coins.nickle = int(input("How Many Nickles (1 Nickle = $0.05)?  "))
            calculate_coins.cent = int(input("How Many Cents (1 Cent = $0.01)?  "))

            total_amount = calculate_coins.calculate_total_amount()

            if total_amount > coffee_menu[your_option]['cost']:
                change = total_amount - coffee_menu[your_option]['cost']
                print(f"Here's your {your_option}")
                print(f"Here's your Change $ {change}")
            else:
                print("You don't have enough money to make coffee ")
