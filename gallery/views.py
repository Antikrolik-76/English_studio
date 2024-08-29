from django.shortcuts import render, HttpResponse


def gallery(request: HttpResponse):
    return HttpResponse(f'<h2>Галлерея</h2>'
                        f'<a href=http://127.0.0.1:8000/>На главную </a>')

