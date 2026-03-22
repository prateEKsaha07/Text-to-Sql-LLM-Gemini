import sqlite3
import random

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

cursor.execute("""
CREATE TABLE IF NOT EXISTS courses (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT,
    student_id INTEGER,
    FOREIGN KEY(student_id) REFERENCES students(id)
)
""")


names = ["Amit", "Sneha", "Rohit", "Anjali", "Karan", "Priya", "Vikas", "Neha"]
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

for i in range(50):
    name = random.choice(names)
    age = random.randint(18, 25)
    marks = random.randint(50, 100)

    cursor.execute(
        "INSERT INTO students (name, age, marks) VALUES (?, ?, ?)",
        (name, age, marks)
    )

courses = ["Math", "Science", "CS", "English"]

for i in range(50):
    cursor.execute(
        "INSERT INTO courses (course_name, student_id) VALUES (?, ?)",
        (random.choice(courses), random.randint(1, 50))
    )

conn.commit()
conn.close()
