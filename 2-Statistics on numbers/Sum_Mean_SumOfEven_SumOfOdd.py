# Write your solution here!
class NumberStats:
    def __init__(self):
        self.numbers = []
        self.even_numbers = []
        self.odd_numbers = []

    def add_number(self, number: int):
        self.numbers.append(number)
        if number % 2 == 0:
            self.even_numbers.append(number)
        else:
            self.odd_numbers.append(number)

    def count_numbers(self):
        return len(self.numbers)

    def get_sum(self):
        return sum(self.numbers)

    def average(self):
        if self.numbers:
            return sum(self.numbers) / len(self.numbers)
        return 0

    def sum_even_numbers(self):
        return sum(self.even_numbers)

    def sum_odd_numbers(self):
        return sum(self.odd_numbers)

def main():
    stats = NumberStats()

    print("Please type in integer numbers:")
    while True:
        try:
            number = int(input())
            if number == -1:
                break
            stats.add_number(number)
        except ValueError:
            print("Invalid input. Please enter an integer.")

    print("Sum of numbers:", stats.get_sum())
    print("Mean of numbers:", stats.average())
    print("Sum of even numbers:", stats.sum_even_numbers())
    print("Sum of odd numbers:", stats.sum_odd_numbers())

if __name__ == "__main__":
    main()

