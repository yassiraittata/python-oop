class Person:
    _student_list = []

    def __init__(self, name):
        self.name = name

    def add_student(self):
        self._student_list.append(self.name)


class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        pass

    def show_students_list(self):
        return self._student_list


std = Student('yassir', 44444)
std2 = Student('amine', 44444)
std.add_student()
std2.add_student()
print(std2.show_students_list())
