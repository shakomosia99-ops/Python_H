# Task 1

weight = float(input("Please enter your weight: "))
height = float(input("Please enter your height: "))

bmi = (weight // height**2)

if bmi <= 19:
    print("Underweight")

elif bmi > 19 and bmi <= 25:
    print("Normal weight")

elif bmi > 25:
    print("Overweight")


print("BMI: ", bmi)


# Task 2


number1 = int(input("Please enter the first number: "))
number2 = int(input("Please enter the second number: "))
arithmetic_operator = input("Please enter arithemic operator: ")

if arithmetic_operator == "+":
    print(number1+number2)
elif arithmetic_operator == "-":
    print(number1-number2)
elif arithmetic_operator == "*":
    print(number1*number2)
elif arithmetic_operator == "/":
    if num2 != 0:
    print(number1/number2)
else:
    print("Error)
elif arithmetic_operator == "%":
    print(number1 % number2)
elif arithmetic_operator == "**":
    print(number1**number2)


# Task 3

num1 = int(input("Please entrer first number: "))
num2 = int(input("Please enter second number: "))
num3 = int(input("Please enter third number: "))

if num1 == num2 or num2 == num3 or num1 == num3:
    print("Number match detected, Please enter different numbers")
else:
    biggestnum = num1

    if biggestnum < num2:
        biggestnum = num2

    if biggestnum < num3:
        biggestnum = num3

    print("Biggest number is:", biggestnum)
