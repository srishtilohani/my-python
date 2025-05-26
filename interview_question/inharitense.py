class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def print_student_details(self=None):
        print(self.name, end= "")
        print(self.age)

    @staticmethod
    def isTeen(age):
        return age > 16

#Driver's code
a = Student.isTeen(18)
print(a)

d = {i: i*i for i in range(10)}
print(d)

