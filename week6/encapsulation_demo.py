#pang_RRC
class Person:
    def __init__(self, name, age):
        self.__name_rrc = name
        self.__age = age

    def get_name(self):
        return self.__name_rrc

    def get_age(self):
        return self.__age

        return self.__name
    def get_age(self):
        return self.__age

p1_rrc = Person("Maria", 20)
print("Name:", p1_rrc.get_name())
print("Age:", p1_rrc.get_age())