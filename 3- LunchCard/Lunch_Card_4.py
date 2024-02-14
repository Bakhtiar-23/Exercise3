class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def __str__(self):
        return f"The balance is {self.balance:} euros"

    def eat_ordinary(self):
        price = 2.95
        if self.balance >= price:
            self.balance -= price
        else:
            print("Insufficient balance for ordinary lunch.")

    def eat_luxury(self):
        price = 5.90
        if self.balance >= price:
            self.balance -= price
        else:
            print("Insufficient balance for luxury lunch.")

    def deposit_money(self, amount: float):
        if amount < 0:
            raise ValueError("Amount to deposit cannot be negative")
        self.balance += amount
        
        
peters_card = LunchCard(20)
graces_card = LunchCard(30)

peters_card.eat_luxury()
graces_card.eat_ordinary()

print(f"Peter: {peters_card}")
print(f"Grace: {graces_card}")

peters_card.deposit_money(20)
graces_card.eat_ordinary()

print(f"Peter: {peters_card}")
print(f"Grace: {graces_card}")

peters_card.eat_ordinary()
peters_card.eat_ordinary()
graces_card.deposit_money(50)

print(f"Peter: {peters_card}")
print(f"Grace: {graces_card}")