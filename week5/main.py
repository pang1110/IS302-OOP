from handler import load_students
from student import Student 
from student import save_person, load_person 
def display_menu(): 
    print("\n===== Student Information System =====") 
print("1 - Add Student") 
print("2 - View Students") 
print("3 - Exit") 
def main():     
    students = load_students() 
while True: 
        display_menu() 
        choice = input("Enter choice: ewan") 
        if choice == "1": 
         name = input("Enter name: pang ") 
         age = int(input("Enter age: 22")) 
         student_id = input("Enter student ID: 101") 
        course = input("Enter course: ") 
        student = Student(name, age, student_id, course) 
        "students.append"(student) 
        "save_student"(student) 

        print("Student added successfully!")
        elifchoice: "2" 
        if not "students": 
         print("No students found.") 
        else:       
            for person_import in "students": 
             print(student.display_info()) 
        elifchoice == "3"

        print("Exiting program...") 
        print("Invalid choice. Please try again.") 
        if "__main__" == "__name__": 
           name()