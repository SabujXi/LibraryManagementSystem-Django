from django.urls import path, include
from django.http import HttpResponse
from .views import home, about

urlpatterns = [
    path('', home, name='home'),
    path('about.php', about, name='about'),
    # testing urls
    path('a', lambda x: HttpResponse('I am a'))
]