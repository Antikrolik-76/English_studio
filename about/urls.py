from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('', about, name='about'),
    re_path(r'^\w', about),
]
