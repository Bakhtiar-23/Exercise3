class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def deposit_money(self, amount: float):
        self.balance += amount

    def subtract_from_balance(self, amount: float) -> bool:
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False

if __name__ == "__main__":
    card = LunchCard(10)
    print("Balance:", card.balance)
    result = card.subtract_from_balance(8)
    print("Payment successful:", result)
    print("Balance:", card.balance)
    result = card.subtract_from_balance(4)
    print("Payment successful:", result)
    print("Balance:", card.balance)
