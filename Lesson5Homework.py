try:
    num1 = float(input("Please enter the first number: "))
    num2 = float(input("Please enter the second number: "))
    calculation = num1 / num2

except ValueError:
    print("Please enter valid number: ")
except ZeroDivisionError:
    print("Cannot be divided by zero! ")
except Exception as e:
    print("Unknown error occured! ")
else:
    print("Result: ", calculation)
finally:
    print("Program completed")
