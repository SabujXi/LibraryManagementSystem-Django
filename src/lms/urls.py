from django.conf import settings
from django.urls import path, re_path, include
from django.http import HttpResponse
from .views import (
    home,
    about,
    book_list,
    member_list,
    addbook,
    AddEditBookView
)

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('book-list', book_list, name='book-list'),
    path('home.aspx', home, name='home'),
    path('member-list',member_list,name='member-list'),
    # path('addbooks', addbook, name='add-book'),
    re_path('add_edit_book/(?P<book_id>[0-9]+)?', AddEditBookView.as_view(), name='add-edit-book'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
