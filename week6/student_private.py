#pang_RRC
class Student:
    def __init__(self, name, student_id, gpa):
        self.__name_rrc = name
        self.__student_id_rrc = student_id
        self.__gpa = gpa

    def get_student_info(self):
        print("Name:", self.__name_rrc)
        print("Student ID:", self.__student_id_rrc)
        print("GPA:", self.__gpa)

student1_rrc = Student("Juan", "2023-001", 1.75)

student1_rrc.get_student_info()