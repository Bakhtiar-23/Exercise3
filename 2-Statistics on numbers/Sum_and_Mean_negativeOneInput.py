# Write your solution here!
class NumberStats:
    def __init__(self):
        self.numbers = []

    def add_number(self, number: int):
        self.numbers.append(number)

    def count_numbers(self):
        return len(self.numbers)

    def get_sum(self):
        return sum(self.numbers)

    def average(self):
        if self.numbers:
            return sum(self.numbers) / len(self.numbers)
        return 0

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

if __name__ == "__main__":
    main()
