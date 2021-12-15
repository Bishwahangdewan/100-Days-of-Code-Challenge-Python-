class Calculate:

    def __init__(self, resources, coffee_menu):
        self.resources = resources
        self.money = 0.0
        self.coffee_menu = coffee_menu
        self.make = ''

    def show_report(self):
        print(f"you have {self.resources['water']} water")
        print(f"you have {self.resources['milk']} milk")
        print(f"you have {self.resources['coffee']} coffee")
        print(f"you have $ {self.money}")

    def check_resources(self):
        if self.resources['water'] > self.coffee_menu[self.make]['ingredients']['water']:
            if self.resources['coffee'] > self.coffee_menu[self.make]['ingredients']['coffee']:
                if self.resources['milk'] > self.coffee_menu[self.make]['ingredients']['milk']:
                    return 1
                else:
                    return 0
            else:
                return 0
        else:
            return 0
