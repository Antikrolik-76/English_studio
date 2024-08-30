from django.shortcuts import render

menu = [{'title': 'Расписание', 'url_name': 'schedule'},
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
    return render(request, 'week.html', {'menu': menu, 'title': 'На неделю'})


def today(request):
    return render(request, 'today.html', {'menu': menu, 'title': 'На сегодня'})

