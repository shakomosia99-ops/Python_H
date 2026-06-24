# Task 1

square = {}
for i in range(1, 11):
    square[i] = i ** 2

print("Task 1")
print(square)
print("______________________________________")
# Task 2

products = [
    {"cola": {
        "price": 1.5,
        "quantity": 10
    }},
    {"fanta": {
        "price": 2.5,
        "quantity": 5
    }},
    {"snickers": {
        "price": 3.5,
        "quantity": 12
    }},
    {"water": {
        "price": 4.5,
        "quantity": 8
    }},
    {"beer": {
        "price": 6.5,
        "quantity": 5
    }}
]

print()
print("Task 2")

for product in products:
    for name in product:
        print(name)

total = 0
for product in products:
    for name, info in product.items():
        total += info["price"] * info["quantity"]

print("Total Value:", total)
print("______________________________________")

# Task 3

print()
print("Task 3")

fruits = {}

while True:
    fruit = input("Enter your favourite fruit: ")

    if fruit == "stop":
        break

    if fruit in fruits:
        fruits[fruit] += 1
    else:
        fruits[fruit] = 1

print(fruits)
