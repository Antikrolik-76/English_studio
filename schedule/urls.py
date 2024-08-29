from django.urls import path, re_path
from .views import *
from main.views import main

urlpatterns = [
    path('', schedule, name='schedule'),
    # re_path(r'^\w', main),
]