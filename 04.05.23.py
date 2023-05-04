
#1

class Student():
    def __init__(self, name ,age):
        self.name = name
        self.age = age
    def info(self):
        print(f"Ім'я: {self.name}, Вік: {self.age}")
student = Student("Dima" , 16)
student.info()

#2

class Circle:
    def __init__(self , radius):
        self.radius = radius
    def area(self):
        print(3.14 * self.radius**2)
areaa = Circle(3)
areaa.area()

#3









