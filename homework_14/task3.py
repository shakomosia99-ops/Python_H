import csv


def collect_persons(count):
    with open("people.csv", "w", encoding="utf-8", newline="") as file:
        fieldnames = ["ID", "first_name", "last_name", "age"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(1, count + 1):
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")

            while True:
                try:
                    age = int(input("Enter age: "))
                    break
                except ValueError:
                    print("Please enter a valid number!")

            writer.writerow({
                "ID": i,
                "first_name": first_name,
                "last_name": last_name,
                "age": age
            })


collect_persons(3)
