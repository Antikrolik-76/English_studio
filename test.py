# menu=[{'title': 'Расписание', 'url_name': 'schedule'},
#       {'title': 'Ученики', 'url_name': 'students'},
#       {'title': 'Группы', 'url_name': 'groups'},
#       {'title': 'Темы', 'url_name': 'topic'},
#       {'title': 'Оплата', 'url_name': 'payment'},
#       {'title': 'Галлерея', 'url_name': 'gallery'},
#       {'title': 'О студии', 'url_name': 'about'},
#       {'title': 'Отзывы', 'url_name': 'reviews'},
# ]
#
# # for m in menu:
# #     print (f'{m['title']} & {m['url_name']}')
#
# for m in menu:
#       print(m.get('title'))
#       print(m.get('url_name'))
from main.views import *

import psycopg2
from students.students import Student, StudentBuilder, StudentsContainer
from students.database import DBConnect, PGStudentManager


# connect = psycopg2.connect(dbname='students',
#                                     host='localhost',
#                                     port=5432,
#                                     user='postgres',
#                                     password='admin')
#
# cursor = connect.cursor()
# query = """ SELECT * FROM students """
# cursor.execute(query)
# # cursor.fetchall()
# container = StudentsContainer()
# container.create_list_student(cursor.fetchall())
# data = container.get_list_students()
# # print(data)
# # count = len(data) if data is not None else 0
# cursor.close()
# a = [3, 4, 5, 6]
# for b in a:
# # print(data[1].surname)
#     print(a.index(b))




# num = [1, 2, 3, 4, 5]
# info = zip(num, data)
# for i in info:
# for pupil in data:
#     num.append(data.index(pupil)+1)
    print(i)


# class DBConnect:
#
#     _instance = None
#
#     @classmethod
#     def get_connect(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = psycopg2.connect(*args, **kwargs)
#         return cls._instance


#{% url m.url_name %} {{m.title}} {% for m in menu %}-->