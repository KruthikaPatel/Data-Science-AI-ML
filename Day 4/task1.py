contacts = {
    "Alice": "9876543210",
    "Bob": "9123456780",
    "Charlie": "9001122334"
}

contacts["David"] = "8899776655"
contacts["Bob"] = "9988776655"

print("Safe Lookup Results:")
print("Alice:", contacts.get("Alice", "Contact not found"))
print("Eve:", contacts.get("Eve", "Contact not found"))

print("\nContact List:")
for name, phone in contacts.items():
    print(f"Contact: {name} | Phone: {phone}")