from django.urls import path, include
from django.http import HttpResponse

urlpatterns = [
    path('a', lambda x: HttpResponse('I am a'))
]