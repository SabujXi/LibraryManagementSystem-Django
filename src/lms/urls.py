from django.urls import path, include
from django.http import HttpResponse
from .views import (
    home,
    about,
    book_list
)

urlpatterns = [
    path('', home, name='home'),
    path('about.php', about, name='about'),
    path('book-list.aspx', book_list, name='book-list'),
    # testing urls
    path('a', lambda x: HttpResponse('I am a'))
]