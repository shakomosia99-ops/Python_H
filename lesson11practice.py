# def get_factorial(n):
#     if n <= 1:
#         return n
#     return n * get_factorial(n-1)


# print(get_factorial())

# def add(a:int,b: int):
#     return a+b

# print(add(1,2))

# from typing import Optional
# from typing import Any

# # email: Optional[str] = None

# # email: str | None = None

# # data: any = 10, "Shako"
# # print(type(data))

# from faker import Faker
# fake = Faker()
# print(fake.first_name())
# print(fake.last_name())
# print(fake.email())
# print(fake.first_name())


from faker import Faker
import random

fake = Faker()


def students(id: int):
    return {
        "ID": id,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "age:": random.randint(18, 90)
    }


def generate_students(n: int):
    return [students(n + 1) for i in range(n)]


num: str = input("Please enter the ID of the student: ")
print(students(num))
