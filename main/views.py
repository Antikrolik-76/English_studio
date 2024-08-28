
from django.shortcuts import render
from django.http import HttpResponse


menu=[{'title': 'Расписание', 'url_name': 'schedule'},
      {'title': 'Ученики', 'url_name': 'students'},
      {'title': 'Группы', 'url_name': 'groups'},
      {'title': 'Темы', 'url_name': 'topic'},
      {'title': 'Оплата', 'url_name': 'payment'},
      {'title': 'Галлерея', 'url_name': 'gallery'},
      {'title': 'О студии', 'url_name': 'about'},
      {'title': 'Отзывы', 'url_name': 'reviews'},
]


def main(request):
    return render(request, 'today.html', {'menu': menu, 'title': 'Главная'})


def week(request):
    return render(request, 'week.html', {'menu': menu, 'title': 'На нbделю'})


def today(request):
    return render(request, 'today.html', {'menu': menu, 'title': 'На сегодня'})


def schedule(request: HttpResponse):
    return HttpResponse(f'<h2>Расписание</h2>'
                        f'<a href=http://127.0.0.1:8000/>На главную </a>')


def students(request: HttpResponse):
    return render(request, 'students_1.html', {'menu': menu, 'title': 'Ученики'})


def groups(request: HttpResponse):
    return render(request, 'groups.html', {'menu': menu, 'title': 'Группы'})


def topic(request: HttpResponse):
    return HttpResponse(f'<h2>Темы</h2>'
                        f'<a href=http://127.0.0.1:8000/>На главную </a>')


def payment(request: HttpResponse):
    return HttpResponse(f'<h2>Оплата</h2>'
                        f'<a href=http://127.0.0.1:8000/>На главную </a>')


def gallery(request: HttpResponse):
    return HttpResponse(f'<h2>Галлерея</h2>'
                        f'<a href=http://127.0.0.1:8000/>На главную </a>')


def about(request: HttpResponse):
    return HttpResponse(f'<h2>О студии</h2>'
                        f'<a href=http://127.0.0.1:8000/>На главную </a>')


def reviews(request: HttpResponse):
    return HttpResponse(f'<h2>Отзывы</h2>'
                        f'<a href=http://127.0.0.1:8000/>На главную </a>')