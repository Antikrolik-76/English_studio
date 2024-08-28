from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from main.views import *
from students.students import Student, StudentBuilder, StudentsContainer
from students.database import DBConnect, PGStudentManager

# from catalog.books import Book, BookBuilder, BooksContainer
# from catalog.database import DBConnect, PGBooksManager


def students(request: HttpRequest):
    connect = DBConnect.get_connect(dbname='studio',
                                    host='localhost',
                                    port=5432,
                                    user='postgres',
                                    password='admin')

    cursor = connect.cursor()
    query = """ SELECT * FROM pupils """
    cursor.execute(query)
    container = StudentsContainer()
    container.create_list_student(cursor.fetchall())
    data = container.get_list_students()
    # print(data)
    # count = len(data) if data is not None else 0
    cursor.close()

    # cursor = connect.cursor()
    # query = """ SELECT name_genre, translation FROM genres """
    # cursor.execute(query)
    # genres = {item[0]: "http://127.0.0.1:8000/catalog/genre/" + item[1] + '/' for item in cursor.fetchall()}
    # cursor.close()

    context = {
        "data": data,
        # "name": data[1],
        # "surname_2": data[2],
        # "age": data[3],
        # "group": data[4],
        # "avg_ball": data[5],
        # "note": data[6],
        # "count": count,
        # "genres": genres,
    }

    return render(request, template_name='students_1.html', context=context)

# def students(request: HttpResponse):
#     return render(request, 'students.html')
