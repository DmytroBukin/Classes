#Класи

class Student:
    print("Hi!")
    count = 0
    def __init__(self , height = 150): #конструктор класу
        self.height = height
        Student.count += 1
dima = Student() #об'єкт , екземпляр класу
print(dima.height)
masha = Student(height = 200)
print(masha.height)
print(Student.count)