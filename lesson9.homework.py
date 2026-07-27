# Task1
print("Task 1")
print("__________________________")


def text(user_text):
    c = 0
    for character in user_text:
        if character.isupper():
            c = c+1
    print("Upper case quantity:", c)
    print("Upper case text:", user_text.upper())


user_input = input("Please enter the text: ")
text(user_input)

print()

# Task 2

print("__________________________")
print("Task 2")


def camel_snake(text):
    result = ""
    for character in text:
        if character.isupper():
            result += "_" + character.lower()
        else:
            result += character
    return result


print(camel_snake("firstName"))
print(camel_snake("name"))
print(camel_snake("preferredFirstName"))
print(camel_snake("lastName"))
