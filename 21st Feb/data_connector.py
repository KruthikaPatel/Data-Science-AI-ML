import sqlite3
import pandas as pd

# 1️⃣ Connect to Database
conn = sqlite3.connect("internship.db")
cursor = conn.cursor()

# 2️⃣ Create Tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS interns (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    track TEXT,
    stipend INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS mentors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mentor_name TEXT,
    track TEXT
)
""")

# 3️⃣ Clear Old Data (Important to avoid duplicates)
cursor.execute("DELETE FROM interns")
cursor.execute("DELETE FROM mentors")
conn.commit()

# 4️⃣ Insert Intern Data
cursor.executemany("""
INSERT INTO interns (name, track, stipend)
VALUES (?, ?, ?)
""", [
    ("Aisha", "Data Science", 15000),
    ("Rahul", "Web Dev", 12000),
    ("Meera", "Data Science", 16000),
    ("Arjun", "Cyber Security", 14000),
    ("Priya", "Web Dev", 13000)
])

# 5️⃣ Insert Mentor Data
cursor.executemany("""
INSERT INTO mentors (mentor_name, track)
VALUES (?, ?)
""", [
    ("Dr. Sharma", "Data Science"),
    ("Mr. Verma", "Web Dev"),
    ("Ms. Iyer", "Cyber Security")
])

conn.commit()

# 6️⃣ JOIN Query
query = """
SELECT interns.name AS Intern_Name,
       interns.track AS Track,
       mentors.mentor_name AS Mentor
FROM interns
JOIN mentors
ON interns.track = mentors.track
"""

df = pd.read_sql_query(query, conn)

print("\nIntern-Mentor Allocation:\n")
print(df)

# 7️⃣ Close Connection
conn.close()