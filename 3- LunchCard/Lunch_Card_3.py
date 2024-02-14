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

def main():
    card = LunchCard(10)
    print(card)

    card.deposit_money(15)
    print(card)

    card.deposit_money(10)
    print(card)

    card.deposit_money(200)
    print(card)

    try:
        card.deposit_money(-10)
    except ValueError as e:
        print(e)
if __name__ == "__main__":
    main()
