# a = 1
# b = 5

# while a <= b:
#     print(a)
#     a += 1
# else:
#     print("A is not less than b")


# print("end of program")

# a = 1
# b = 5

# while a < b:
#     print(a)
#     a += 1
# print("End of Program")


# counter = 1
# c = "Hello world"
# while counter < 7:
#     print(c)
#     counter += 1


# print("end of progam")


# password = "admin123"

# while True:
#     user_password = input("Please enter your password: ")
#     if user_password == password:
#         print("Correct")
#         break
#     else:
#         print("Invalid password! ")

# attempts = 3
# password = "admin123"
# while attempts > 0:
#     user_password = input("Please enter your password: ")

#     if user_password == password:
#         print("Welcome! ")
#         break
#     else:
#         attempts -= 1
#         print(f"Invalid password, you have {attempts} attempts left! ")
# else:
#     print("Access denied! ")


# attempts = 3
# password = "admin123"
# while attempts > 0:
#     user_password = input("Please enter your password: ")

#     if user_password == password:
#         print("Welcome! ")
#         break
#     else:
#         if user_password == "":
#             print("Blank password is not allowed")
#             print(f"You have {attempts} attempts left")
#             continue

#         attempts -= 1
#         print(f"Invalid password, you have {attempts} attempts left! ")
# else:
#     print("Access denied! ")


# text = "Noom"

# # for chatacter in text:
# #     print(chatacter)

# iterator = iter(text)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# for char in "Python":
#     print("Hello world")


# for i in range(11):
#     print(i)

# for _ in range(5): _ - არის მიღებული შეთანხმება
#   print("hello world")

# for _ in range(5):
#     print("Hi")

# for _ in range(5):
#     number = int(input("Please enter the number: "))

# for i in range(1, 11):
#     print(i)

# for i in range(1, 11, 2):
#     print(i)

# for i in range(10, 0, -1):
#     print(i)

# for i in range(1, 6):
#     for j in range(1,6):
#         print(f"i = {i}, j = {j}")


# print(random.randint(1, 100))

# print(random.random())
# print(random.randrange(1,10))
# from  random import randint

import random


program_number = random.randint(1, 100)
attempt = 10
print("Guess number from 1-100! ")

while attempt > 0:
    try:
        Playernum = int(input("Please enter you guess: "))
    except ValueError:
        print("Please enter actual number! ")
        continue

    if Playernum == program_number:
        print("Correct, Congradulations! ")
        break

    elif Playernum < program_number:
        print("Wrong, too low, try again! ")

    elif Playernum > program_number:
        print("Wrong, too high, try again! ")

    if Playernum == "":
        print("You have to enter actual number! ")

    attempt -= 1

    print(f"You have {attempt} attempts left! ")
else:
    print(f"Out of attempts! :( The Number was {program_number}.")
