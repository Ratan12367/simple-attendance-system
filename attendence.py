# Simple Attendance System
# College Level Project

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")

    with open("students.txt", "a") as file:
        file.write(roll + "," + name + "\n")

    print("Student added successfully!")

def mark_attendance():
    roll = input("Enter Roll Number: ")
    status = input("Enter P for Present or A for Absent: ")

    with open("attendance.txt", "a") as file:
        file.write(roll + "," + status + "\n")

    print("Attendance marked successfully!")

def view_students():
    print("\n--- Student List ---")
    try:
        with open("students.txt", "r") as file:
            print(file.read())
    except:
        print("No students found.")

def view_attendance():
    print("\n--- Attendance Records ---")
    try:
        with open("attendance.txt", "r") as file:
            print(file.read())
    except:
        print("No attendance records found.")

while True:
    print("\n===== STUDENT ATTENDANCE SYSTEM =====")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. View Students")
    print("4. View Attendance")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        mark_attendance()
    elif choice == "3":
        view_students()
    elif choice == "4":
        view_attendance()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.")
