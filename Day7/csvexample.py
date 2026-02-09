import csv
with open(r"C:\Users\Lenovo\OneDrive\Desktop\Company_Data.csv", mode="r") as file:
    csv_file=csv.reader(file)
    for lines in csv_file:
        print(lines)
