#CalilungRRC
def save_student(student):
    with open("students.txt", "a") as file_rrc:
        file_rrc.write(student.student_id + "," + student.name + "," + student.course + "\n")

def view_students():
    try:
        with open("students.txt", "r") as file_rrc:
            for line in file_rrc:
                student_id, name, course = line.strip().split(",")
                print(student_id, name, course)
    except FileNotFoundError:
        print("No records found.")