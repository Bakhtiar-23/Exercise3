class Person:
    def __init__(self, name, height):
        self.name = name
        self.height = height

class Room:
    def __init__(self):
        self.persons = []

    def add(self, person):
        self.persons.append(person)

    def is_empty(self):
        return len(self.persons) == 0

    def print_contents(self):
        if not self.persons:
            print("The room is empty.")
        else:
            total_height = sum(person.height for person in self.persons)
            print(f"There are {len(self.persons)} persons in the room, and their combined height is {total_height} cm")
            for person in self.persons:
                print(f"{person.name} ({person.height} cm)")

    def shortest(self):
        if not self.persons:
            return None
        shortest_person = min(self.persons, key=lambda x: x.height)
        return shortest_person.name

# Test the Room class
room = Room()

print("Is the room empty?", room.is_empty())
print("Shortest:", room.shortest())

room.add(Person("Lea", 183))
room.add(Person("Kenya", 172))
room.add(Person("Nina", 162))
room.add(Person("Ally", 166))

print()

print("Is the room empty?", room.is_empty())

print()

room.print_contents()


