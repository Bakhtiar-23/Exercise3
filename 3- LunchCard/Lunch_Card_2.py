class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def __str__(self):
        return f"The balance is {self.balance:.1f} euros"

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

# Test main function
def main():
    card = LunchCard(50)
    print(card)

    card.eat_ordinary()
    print(card)

    card.eat_luxury() # Also can print(card) here, but it wasn't in Ex
    #print(card)
    card.eat_ordinary()
    print(card)

if __name__ == "__main__":
    main()
