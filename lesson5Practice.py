try:
    age = int(input("Please enter your age: "))

    if age < 0:
        raise ValueError("Enter positive number! ")

except ValueError:
    print("Pleae enter the number")


else:
    if age < 18:
        print("Minor")
    else:
        print("Adult")
