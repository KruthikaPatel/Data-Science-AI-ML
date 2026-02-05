total_bill = float(input("Enter the total bill amount: "))
num_people = int(input("Enter the number of people: "))
share_per_person = total_bill / num_people
print(f"Total Bill: {total_bill}. Each person pays: {share_per_person}")
print("Data types:")
print("total_bill:", type(total_bill))
print("num_people:", type(num_people))
print("share_per_person:", type(share_per_person))