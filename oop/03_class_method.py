# class method


class Student:
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1

    @classmethod
    def get_count(cls):
        return f"Total students: {cls.count}"


print(Student.get_count())

s1 = Student("Alice")
print(Student.get_count())
