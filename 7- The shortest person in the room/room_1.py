class Person:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def __str__(self):
        return f"{self.name} ({self.height} cm)"


class Room:
    def __init__(self):
        self.persons = []

    def add(self, person):
        self.persons.append(person)

    def is_empty(self):
        return len(self.persons) == 0

    def print_contents(self):
        if self.is_empty():
            print("The room is empty.")
        else:
            print(f"There are {len(self.persons)} persons in the room, and their combined height is {sum(person.height for person in self.persons)} cm")
            for person in self.persons:
                print(person)


if __name__ == "__main__":
    room = Room()
    print("Is the room empty?", room.is_empty())
    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Ally", 166))
    room.add(Person("Nina", 162))
    room.add(Person("Dorothy", 155))
    print("Is the room empty?", room.is_empty())
    room.print_contents()
