#Класи

class Student:
    print("Hi!")
    count = 0
    def __init__(self , height = 150):
        self.height = height
dima = Student() #об'єкт , екземпляр класу
print(dima.height)
masha = Student(height = 200)
print(masha.height)
