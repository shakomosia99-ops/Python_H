from functools import reduce

# Task 1


def sum_numbers(n=5):
    total = 0
    for i in range(n):
        num = int(input(f"Please enter the number ({i+1} / {n}): "))
        total += num
    return total


print("Task 1")
print(f"Sum is {sum_numbers()}")
print("___________________________________________")
print(input("Press any key to continue"))


# Task 2

def sep(*args):
    even = [n for n in args if n % 2 == 0]
    odd = [n for n in args if n % 2 != 0]
    return even, odd


even_list, odd_list = sep(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print("Task 2")
print("even", even_list)
print("odd", odd_list)

print("___________________________________________")
print(input("Press any key to continue"))

# Task 3


def word_count(sentence):
    words = sentence.lower().replace(".", "").replace(",", "").split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


print("Task 3")
sentance = input("Please enter the sentance: ")
print(word_count(sentance))


print("___________________________________________")
print(input("Press any key to continue"))


# Task 4


products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 15},
    {"name": "Keyboard", "price": 25},
    {"name": "Monitor", "price": 150},
    {"name": "Power", "price": 100},
    {"name": "Pad", "price": 10},
]


print("Task 4")

cheap = list(filter(lambda p: p["price"] < 100, products))
print("Cheaper than 100$: ", cheap)

names = list(map(lambda p: f"{p["name"]}: ${p["price"]}", products))
print("Products: ", names)

sortedp = sorted(products, key=lambda p: p["price"])
print("Sorted: ", sortedp)

total_price = reduce(lambda acc, p: acc + p["price"], products, 0)
print("Sum: ", total_price)


print("___________________________________________")
print(input("Press any key to continue"))

# Task 5


def recursive_sum(n):
    if n <= 1:
        return n
    return n + recursive_sum(n - 1)


print("Task 5")
print(recursive_sum(10))
print(recursive_sum(5))
