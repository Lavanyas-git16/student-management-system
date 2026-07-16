import sqlite3

connection = sqlite3.connect("students.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id TEXT PRIMARY KEY,
    name TEXT,
    age INTEGER,
    department TEXT
)
""")

connection.commit()

print("Database created successfully!")

connection.close()