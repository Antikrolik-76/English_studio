from django.shortcuts import render
from django.http import HttpResponse
from main.views import *


def students(request: HttpResponse):
    return render(request, 'students.html')
