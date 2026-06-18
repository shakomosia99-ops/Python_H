# Task 1

import random
num = [95, 25, 5, 15, 75]

sum = 0
for i in num:
    sum += i

average = sum / len(num)
print("_______________________")
print("Task1")
print(f"Numbers: {num}")
print(f"Sum: {sum}")
print(f"Average: {average}")


# Task 2

lst = ['a', 'b', 2, 4, 2, 'c', 'j', 1, 'b', 'd', 'c', 4, 1]
newlst = []

for j in lst:
    if j not in newlst:
        newlst.append(j)


print("_______________________")
print("Task 2")
print(f"Og list {lst}")
print(f"Unique list: {newlst}")


# Task 3

# rnum = [random.randint(-50,50)]
rnum = []
for _ in range(20):
    rnum.append(random.randint(-50, 50))

enum = []
for e in rnum:
    if e % 2 == 0:
        enum.append(e)

print("_______________________")
print("Task 3")
print(f"Generated numbers: {rnum}")
print(f"Even numbers: {enum}")

# Task 4


print("_______________________")
print("Task 4")

persons = [
    ('Kelly', 'Simpson', 26),
    ('Erika', 'Stephens', 24),
    ('Cheryl', 'Dunn', 30),
    ('Amy', 'Larsen', 49),
    ('Christine', 'Gordon', 23),
    ('Monica', 'Huff', 38),
    ('David', 'Nixon', 36),
    ('Cindy', 'Escobar', 41),
    ('Cindy', 'White', 33),
    ('Joel', 'Hall', 43),
    ('Steven', 'Wilson', 28),
    ('Alex', 'Cole', 68),
    ('Alex', 'Smith', 32),
    ('Alex', 'White', 42),
    ('Brittany', 'Thompson', 18),
    ('Ernest', 'Young', 43),
    ('Traci', 'Wells', 38),
    ('Andrew', 'Flores', 61),
    ('Christopher', 'Lewis', 29),
    ('Kevin', 'Willis', 57),
    ('Kayla', 'Lucas', 28),
    ('Michelle', 'Rush', 43),
    ('Shalva', 'Mosia', 27)
]


while True:
    first_name = input("Please enter your name (stop to exit): ").strip()

    if first_name.lower() == "stop":
        break

    name_found = False
    for person in persons:
        if person[0] == first_name:
            name_found = True
            break

    if not name_found:
        print(f"{first_name} Name not found in list. ")
        continue

    last_name = input("Enter lastname: ").strip()

    if last_name.lower() == "stop":
        break

    person_found = False
    for person in persons:
        if person[0] == first_name and person[1] == last_name:
            print(f"{first_name} {last_name} age is: {person[2]}")
            person_found = True
            break

    if not person_found:
        print(f"{first_name} {last_name} not found")
