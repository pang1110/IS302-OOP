#from student import student
FILENAME="data.txt" 
def save_student(student): 
    with open(FILENAME, "a") as file: 
        file.write(student.to_file_format()) 
def load_students(): 
    student = [] 
    with open(FILENAME, "r") as file: 
        for line in file: 
            name, age, student_id, course = line.strip().split(",") 
students =("pang, 22, 1001, bsis")
students = (students)
# File does not exist yet 
pass
print(students)
