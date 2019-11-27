from django.conf import settings
from django.urls import path, re_path, include
from django.http import HttpResponse
from .views import (
    home,
    about,
    book_list,
    member_list,
    addbook,
    AddEditBookView,
    delete_book,
    #author

)
from .views.author import (
    author_list,
    author_delete,
    AuthorAddUpdate,
)
from .views.auths import (
    LoginView,
    SignupView,
    forget_password,
    logout_view
)
login_view = LoginView.as_view()
signup_view = SignupView.as_view()

from .views.book_issue import (
    book_issue_list,
    book_issue_view,
    book_return_view,
)



from .views.member import (
    NewMemberView,
)
new_member = NewMemberView.as_view()

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('book-list', book_list, name='book-list'),
    path('home.aspx', home, name='home'),
    path('member-list',member_list,name='member-list'),
    # new member crate
    path('create-new-member', new_member, name='new-member'),
    # path('addbooks', addbook, name='add-book'),
    re_path('add_edit_book/(?P<book_id>[0-9]+)?', AddEditBookView.as_view(), name='add-edit-book'),
    path('delete-book/<int:id>', delete_book, name='delete-book'),
    # author
    path('author-list', author_list, name= 'author-list'),
    path('author-edit-update', AuthorAddUpdate.as_view(), name='author-add-update' ),
    path('author-delete', author_delete, name='author-delete'),
    #auths
    path('login', login_view, name="login"),
    path('logout', logout_view, name="logout"),
    path('signup', signup_view, name="signup"),
    path('forget-password', forget_password, name="forget-password"),

    # book issue view

    path('book-issue', book_issue_view, name='book-issue'),
    path('book-return', book_return_view, name='book-return'),
    path('book-issue-list', book_issue_list, name='book-issue-list'),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
