#pang_RRC
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def display_student(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)

student1 = Student("Pang", 22, "BSIS")
student1.display_student()