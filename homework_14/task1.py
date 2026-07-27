def collect_names():
    counter = 1
    with open("names.txt", "w", encoding="utf-8") as file:
        while True:
            first_name = input("Enter your first name: ")
            if first_name == "stop":
                break
            last_name = input("Enter your last name: ")
            file.write(f"{counter}. {first_name} {last_name}\n")
            counter += 1


collect_names()
