from django.urls import path, include
from django.http import HttpResponse
from .views import home, about

urlpatterns = [
    path('', home),
    path('about.php', about),
    path('a', lambda x: HttpResponse('I am a'))
]