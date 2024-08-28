from abc import ABC, abstractmethod
from .students import Student, StudentsContainer
import psycopg2


class DBConnect:

    _instance = None

    @classmethod
    def get_connect(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = psycopg2.connect(*args, **kwargs)
        return cls._instance


class DBManager(ABC):

    @staticmethod
    @abstractmethod
    def create(connect, student: Student):
        ...

    @staticmethod
    @abstractmethod
    def read(connect, student: Student):
        ...

    @staticmethod
    @abstractmethod
    def update(connect, old_student: Student, new_student: Student):
        ...

    @staticmethod
    @abstractmethod
    def delete(connect, student: Student):
        ...


class PGStudentManager(DBManager):

    @staticmethod
    def create(connect, student: Student):
        # Вызвать запрос вставки данных из объекта в таблицу
        ...

    @staticmethod
    def read(connect, student: Student) -> list[Student]:

        try:
            with connect.cursor() as cursor:

                params = (student.surname, student.name, )
                query = """SELECT * 
                           FROM students
                           WHERE surname = %s AND
                                 name = %s"""
                cursor.execute(query, params)
                data = cursor.fetchall()

                if data:
                    container = StudentsContainer()
                    container.create_list_student(data)
                    return container.get_list_students()
                else:
                    raise Exception(f"Не найдена запись с параметрами {params}")
        except (Exception, psycopg2.Error) as e:
            print(e)

    @staticmethod
    def update(connect, index_old_student: int, new_student: Student):
        # Обновить данные о книге в таблице
        ...

    @staticmethod
    def delete(connect, student: Student):
        # Удалить девайс
        ...
