from django.shortcuts import render, HttpResponse


def topic(request: HttpResponse):
    return HttpResponse(f'<h2>Темы</h2>'
                        f'<a href=http://127.0.0.1:8000/>На главную </a>')
