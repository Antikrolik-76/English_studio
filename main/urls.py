from django.urls import path, re_path
from groups.views import groups
from main.views import main, today, week
from schedule.views import schedule
from students.views import students
from topic.views import topic
from payment.views import payment
from gallery.views import gallery
from about.views import about
from reviews.views import reviews


urlpatterns = [
    path('', main, name='main'),
    path('today/', today, name='today'),
    path('week/', week, name='week'),
    # re_path('today/schedule/', main, name='main'),
    path('schedule/', schedule, name='schedule'),
    path('students/', students, name='students'),
    path('groups/', groups, name='groups'),
    path('topic/', topic, name='topic'),
    path('payment/', payment, name='payment'),
    path('gallery/', gallery, name='gallery'),
    path('about/', about, name='about'),
    path('reviews/', reviews, name='reviews'),
    # re_path(r'^\w', main),
]
