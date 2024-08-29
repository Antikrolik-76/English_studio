from django.shortcuts import render, HttpResponse
from main.views import menu


def schedule(request: HttpResponse):
    return HttpResponse(f'<h2>Расписание</h2>'
                        f'<a href=http://127.0.0.1:8000/>На главную </a>')
