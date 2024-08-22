"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from main.views import week


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls'), name='main'),
    # path('today/', include('main.urls'), name='main'),
    # path('week/', include('main.urls'), name='main'),
    path('groups/', include('groups.urls'), name='groups'),
    path('students/', include('students.urls'), name='students'),
    # path('schedule/', include('schedule.urls'), name='schedule'),
    # path('topic/', include('topic.urls'), name='topic'),
    # path('payment/', include('payment.urls'), name='payment'),
    # path('gallery/', include('gallery.urls'), name='gallery'),
    # path('about/', include('about.urls'), name='about'),
    # path('reviews/', include('reviews.urls'), name='reviews'),

]
