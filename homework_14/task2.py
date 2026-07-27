with open("persons.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

under_50 = []
over_50 = []

for line in lines:
    parts = line.strip().split(", ")
    age = int(parts[1])
    if age < 50:
        under_50.append(line)
    else:
        over_50.append(line)

with open("under_50.txt", "w", encoding="utf-8") as file:
    file.writelines(under_50)

with open("over_50.txt", "w", encoding="utf-8") as file:
    file.writelines(over_50)
