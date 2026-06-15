# Task 1

player_number = int(input("Please enter the number: "))
factorial = 1
for _ in range(1, player_number + 1):
    factorial *= _
print(f"Factorial of {player_number} = {factorial} ")


print("____________________________________________________")

# Task 2
print()

print(input("Press any key to continue"))

for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i}*{j} = {i*j}")

print("____________________________________________________")


# Task 3

print()


total_amount = 50

print("Please pay 50$, Only accaptable banknotes are: 20, 10 ,5. ")


while True:
    payable_amount = int(input("Please enter the banknote: "))

    if payable_amount != 20 and payable_amount != 10 and payable_amount != 5:
        print("Invalid banknote!")
        continue
    if total_amount < payable_amount:
        print(
            f"You entered exceeded {payable_amount}$ . Please enter proper amount! ")
        continue

    total_amount -= payable_amount
    print(f"Remining {total_amount}$ to pay. ")

    if total_amount == 0:
        print("Payment is fully complete, Thank you!")
        break
