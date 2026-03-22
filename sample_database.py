import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    marks INTEGER
)
""")

cursor.execute("INSERT INTO students (name, age, marks) VALUES ('Prateek', 21, 85)")
cursor.execute("INSERT INTO students (name, age, marks) VALUES ('Rahul', 22, 90)")

conn.commit()
conn.close()