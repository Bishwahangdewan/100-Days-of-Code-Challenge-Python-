class Coins:
    def __init__(self):
        self.quarter = 0
        self.dime = 0
        self.nickle = 0
        self.penny = 0

    def calculate_total_amount(self):
        total = (self.quarter * 0.25) + (self.dime * 0.10) + (self.nickle * 0.05) + (self.penny * 0.01)
        return total
