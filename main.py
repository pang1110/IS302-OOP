#CalilungRRC
from unicodedata import name

from student import Student
from file_handler import save_student, view_students
import student

def add_student():
    student_id = input("Enter Student ID: ")
    name_rrc = input("Enter Name: ")
    course_rrc = input("Enter Course: ")
    student_rrc = Student(student_id, name_rrc, course_rrc)
    save_student(student_rrc)
    print("Student added successfully")
def search_student():
    search_id = input("Enter Student ID to search: ")
    try:
        with open("students.txt", "r") as file:
            for line in file:
                student_id, name_rrc, course_rrc = line.strip().split(",")
                if student_id == search_id:
                    print(f"Student found - ID: {student_id}, Name: {name_rrc}, Course: {course_rrc}")
                    return
            print("Student not found")
    except FileNotFoundError:
        print("No students found.")
def main():
    while True:
        print("\n1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")




