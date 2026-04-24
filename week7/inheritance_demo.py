#pang_RRC
class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, "makes a sound")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def bark(self):
        print(self.name, "barks")

dog1 = Dog("Buddy")
dog1.speak()
dog1.bark()
