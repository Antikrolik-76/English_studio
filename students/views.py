from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
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
    cursor.close()
    context = {
        "data": data,
    }

    return render(request, template_name='students_1.html', context=context) # context=context

# def students(request: HttpResponse):
#     return render(request, 'students.html')
