from abc import ABC, abstractmethod


class Student:

    def __init__(self):
        self.surname = None
        self.name = None
        self.surname_2 = None
        self.age = None
        self.group = None
        self.avg_ball = None
        self.note = None

    # def __str__(self):
    #     return (f'Фамилия: {self.surname}\n'
    #             f'Имя: {self.name}\n'
    #             f'Отчество: {self.surname_2}\n'
    #             f'Возраст: {self.age}')


class Builder(ABC):

    @abstractmethod
    def create(self):
        ...

    @abstractmethod
    def set_surname(self, surname):
        ...

    @abstractmethod
    def set_name(self, name):
        ...

    @abstractmethod
    def set_surname_2(self, surname_2):
        ...

    @abstractmethod
    def set_age(self, age):
        ...

    @abstractmethod
    def set_group(self, group):
        ...

    @abstractmethod
    def set_avg_ball(self, avg_ball):
        ...

    @abstractmethod
    def set_note(self, note):
        ...

    @abstractmethod
    def get_student(self):
        ...


class StudentBuilder(Builder):

    student: Student

    def create(self):
        self.student = Student()

    def set_surname(self, surname):
        self.student.surname = surname

    def set_name(self, name):
        self.student.name = name

    def set_surname_2(self, surname_2):
        self.student.surname_2 = surname_2

    def set_group(self, group):
        self.student.group = group

    def set_age(self, age):
        self.student.age = age

    def set_avg_ball(self, avg_ball):
        self.student.avg_ball = avg_ball

    def set_note(self, note):
        self.student.note = note

    def get_student(self):
        return self.student


class StudentCreator:

    def __init__(self, builder: Builder) -> None:
        self._builder = builder

    def change_builder(self, builder: Builder):
        self._builder = builder

    def make(self, student: tuple) -> Student:
        self._builder.create()
        self._builder.set_surname(student[1])
        self._builder.set_name(student[2])
        self._builder.set_surname_2(student[3])
        self._builder.set_age(student[4])
        self._builder.set_group(student[5])
        self._builder.set_avg_ball(student[6])
        self._builder.set_note(student[7])
        return self._builder.get_student()


class StudentsContainer:

    def __init__(self):
        self.students: list[Student] = []

    def create_list_student(self, data: list) -> None:
        builder = StudentBuilder()
        creator = StudentCreator(builder)

        for inf in data:
            student = creator.make(inf)
            self.students.append(student)

    def add_student(self, student: Student):
        self.students.append(student)

    def get_list_students(self):
        return self.students
