from django.urls import path, re_path
from .views import *


urlpatterns = [
    # path('', main),
    # path('home/', home, name='home'),
    # path('week/', week, name='week'),
    # path('schedule/', schedule, name='schedule'),
    path('', students, name='students'),
    # path('groups/', groups, name='groups'),
    # path('topic/', topic, name='topic'),
    # path('payment/', payment, name='payment'),
    # path('gallery/', gallery, name='gallery'),
    # path('about/', about, name='about'),
    # path('reviews/', reviews, name='reviews'),
]