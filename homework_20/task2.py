import json


def add_persons(count):

    with open("persons.json", "r", encoding="utf-8") as file:
        persons = json.load(file)

    if persons:
        last_id = persons[-1]["id"]
    else:
        last_id = 0

    for _ in range(count):
        name = input("enter your name: ")
        age = int(input("enter your age: "))
        last_id += 1
        persons.append({"id": last_id, "name": name, "age": age})

    with open("persons.json", "w", encoding="utf-8") as file:
        json.dump(persons, file, indent=4)


add_persons(2)
