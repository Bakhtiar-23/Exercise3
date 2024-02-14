class BankAccount:
    def __init__(self, owner, account_number, balance):
        self.__owner = owner
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        self.__service_charge()

    def withdraw(self, amount):
        self.__balance -= amount
        self.__service_charge()

    @property  # Define balance as a property
    def balance(self):
        return self.__balance

    def __service_charge(self):
        self.__balance -= self.__balance * 0.01

if __name__ == "__main__":
    account = BankAccount("Randy Riches", "12345-6789", 1000)
    account.withdraw(100)
    print(account.balance)  # Access balance as a property
    account.deposit(100)
    print(account.balance)  # Access balance as a property
