class NumberStats:
    def __init__(self):
        self.num_count = 0

    def add_number(self, number):
        self.num_count += 1

    def count_numbers(self):
        return self.num_count

# Example usage
stats = NumberStats()
stats.add_number(3)
stats.add_number(5)
stats.add_number(1)
stats.add_number(2)
print("Numbers Added:", stats.count_numbers())
