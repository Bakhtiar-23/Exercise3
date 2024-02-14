from Lunchcard_Payment_T1 import LunchCard

class PaymentTerminal:
    def __init__(self):
        self.funds = 1000
        self.lunches = 0
        self.specials = 0

    def eat_lunch(self, payment: float) -> float:
        price = 2.50
        if payment >= price:
            self.funds += price
            self.lunches += 1
            return payment - price
        else:
            return payment

    def eat_special(self, payment: float) -> float:
        price = 4.30
        if payment >= price:
            self.funds += price
            self.specials += 1
            return payment - price
        else:
            return payment

    def eat_lunch_lunchcard(self, card: LunchCard) -> bool:
        price = 2.50
        if card.balance >= price:
            card.balance -= price
            self.lunches += 1
            return True
        else:
            return False

    def eat_special_lunchcard(self, card: LunchCard) -> bool:
        price = 4.30
        if card.balance >= price:
            card.balance -= price
            self.specials += 1
            return True
        else:
            return False

if __name__ == "__main__":
    exactum = PaymentTerminal()

    change = exactum.eat_lunch(10)
    print("The change returned was", change)

    card = LunchCard(7)

    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)
    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)
    result = exactum.eat_lunch_lunchcard(card)
    print("Payment successful:", result)

    print("Funds available at the terminal:", exactum.funds)
    print("Regular lunches sold:", exactum.lunches)
    print("Special lunches sold:", exactum.specials)
    
