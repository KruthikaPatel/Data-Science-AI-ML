import csv

with open("students.csv", mode="r") as file:
    reader = csv.DictReader(file)

    print("Students who passed:")
    for row in reader:
        if row["Status"] == "Pass":
            print(row["Name"])
