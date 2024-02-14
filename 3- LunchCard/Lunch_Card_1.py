class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def __str__(self):
        rounded_balance = round(self.balance, 1)
        return f"The balance is {rounded_balance} euros"

card = LunchCard(50)
print(card)
