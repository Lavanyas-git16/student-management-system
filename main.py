# Connect to SQLite database
import sqlite3

# Create database connection
connection = sqlite3.connect("students.db")

# Create cursor object
cursor = connection.cursor()

def add_student():

    student_id = input("Enter Student ID: ").strip()

    if student_id == "":
        print("Student ID cannot be empty.")
        return

    name = input("Enter Student Name: ").strip()

    if not name.replace(" ", "").isalpha():
        print("Invalid Name")
        return

    age = input("Enter Age: ")

    if not age.isdigit():
        print("Age must be numeric.")
        return

    department = input("Enter Department: ").strip()

    if department == "":
        print("Department cannot be empty.")
        return

    # Check duplicate ID
    cursor.execute(
        "SELECT * FROM students WHERE id=?",
        (student_id,)
    )

    if cursor.fetchone():
        print("Student ID already exists.")
        return

    # Insert new student
    cursor.execute(
        "INSERT INTO students VALUES (?, ?, ?, ?)",
        (student_id, name, age, department)
    )

    connection.commit()

    print("Student added successfully!")

def view_students():
    print("\n----- Student List -----")

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    if len(students) == 0:
        print("No students found.")
        return

    print("=" * 60)
    print(f"{'ID':<10}{'NAME':<20}{'AGE':<10}{'DEPARTMENT':<20}")
    print("=" * 60)

    for student in students:
        print(f"{student[0]:<10}{student[1]:<20}{student[2]:<10}{student[3]:<20}")

    print("=" * 60)

def search_student():
    print("\n----- Search Student -----")

    student_id = input("Enter Student ID: ")

    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    student = cursor.fetchone()

    if student:
        print("\nStudent Found")
        print("------------------------")
        print("Student ID :", student[0])
        print("Name       :", student[1])
        print("Age        :", student[2])
        print("Department :", student[3])
    else:
        print("Student not found.")

def update_student():
    print("\n----- Update Student -----")

    student_id = input("Enter Student ID to update: ")

    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    student = cursor.fetchone()

    if student:
        name = input("Enter New Name: ")
        age = input("Enter New Age: ")
        department = input("Enter New Department: ")

        cursor.execute(
            "UPDATE students SET name=?, age=?, department=? WHERE id=?",
            (name, age, department, student_id)
        )

        connection.commit()

        print("Student updated successfully!")

    else:
        print("Student not found.")

def delete_student():
    print("\n----- Delete Student -----")

    student_id = input("Enter Student ID to delete: ")

    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    student = cursor.fetchone()

    if student:

        cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
        connection.commit()

        print("Student deleted successfully!")

    else:
        print("Student not found.")

while True:
    print("\n==============================")
    print(" STUDENT MANAGEMENT SYSTEM")
    print("==============================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
       update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice!")
connection.close()