class Box:
    def __init__(self):
        self.present_list = []

    def add_present(self, present):
        self.present_list.append(present)

    def total_weight(self):
        total = sum(present.weight for present in self.present_list)
        return total


class Present:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"{self.name} ({self.weight}g)"


if __name__ == "__main__":
    book = Present("Ta-Nehisi Coates:The Water Dancer", 200)
    box = Box()
    box.add_present(book)
    print(box.total_weight())

    cd = Present("Pink Floyd: Dark Side of the Moon", 50)
    box.add_present(cd)
    print(box.total_weight())
