class Student:
    class_year = 2027  # class variable
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1


student1 = Student("IndieDev", 19)
print(student1.name, student1.age)
print(Student.class_year)

student2 = Student("DuoDevs", 25)
print(student2.name, student2.age)
print(Student.class_year)


student2 = Student("TriDevs", 27)
print(student2.name, student2.age)
print(Student.class_year)

student4 = Student("FourDevs", 22)
print(student2.name, student2.age)
print(Student.class_year)

student5 = Student("FiveDevs", 25)
print(student2.name, student2.age)
print(Student.class_year)

print(Student.num_students)
