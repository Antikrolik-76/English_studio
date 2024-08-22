menu=[{'title': 'Расписание', 'url_name': 'schedule'},
      {'title': 'Ученики', 'url_name': 'students'},
      {'title': 'Группы', 'url_name': 'groups'},
      {'title': 'Темы', 'url_name': 'topic'},
      {'title': 'Оплата', 'url_name': 'payment'},
      {'title': 'Галлерея', 'url_name': 'gallery'},
      {'title': 'О студии', 'url_name': 'about'},
      {'title': 'Отзывы', 'url_name': 'reviews'},
]

# for m in menu:
#     print (f'{m['title']} & {m['url_name']}')

for m in menu:
      print(m.get('title'))
      print(m.get('url_name'))
