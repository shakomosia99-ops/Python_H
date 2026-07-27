class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person: ({self.name}, {self.age})"


def serialize(person):
    return f"Name: {person.name}, Age: {person.age}"


def deserialize(line):
    name_part, age_part = line.split(", ")
    name = name_part.split(": ")[1]
    age = int(age_part.split(": ")[1])
    return Person(name, age)


def write_person_to_file(person, filename):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(serialize(person))


def read_person_from_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        line = file.readline().strip()
    return deserialize(line)


p1 = Person("Shalva", 27)

write_person_to_file(p1, "person.txt")

p2 = read_person_from_file("person.txt")
print(p2)
print(type(p2))
print(p2.name, p2.age)
