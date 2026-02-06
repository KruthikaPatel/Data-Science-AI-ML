raw_logs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]
unique_users = set(raw_logs)
is_ID05_present = "ID05" in unique_users
print("Is ID05 present in unique_users?", is_ID05_present)
print("Original list length:", len(raw_logs))
print("Unique users set length:", len(unique_users))
print("Unique User IDs:", unique_users)