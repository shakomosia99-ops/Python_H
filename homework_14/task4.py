import csv

with open("students.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    students = list(reader)
    fieldnames = reader.fieldnames

failed = []
passed = []

for student in students:
    if int(student["Grade"]) < 50:
        failed.append(student)
    else:
        passed.append(student)

with open("failed_students.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(failed)

with open("passed_students.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(passed)
