from django.shortcuts import render, HttpResponse
from main.views import menu


def groups(request: HttpResponse):
    return render(request, 'groups.html', {'menu': menu, 'title': 'Группы'})
