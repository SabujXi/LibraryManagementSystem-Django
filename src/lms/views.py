from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib import messages

from .models import (
    Book,
    Member,
)
from .utils import validate_book_data, del_values_by_key

# Create your views here.
def home(req):
    context = {
    }
    return render(req, "lms/home.html", context=context)


def about(req):
    context = {
    }
    return render(req, "lms/about.html", context=context)

def book_list(req):
    books = Book.objects.all()

    context = {
        'books': books
    }
    return render(req, "lms/book_list.html", context=context)

def member_list(req):
    members = [
        {
            "id": 1,
            "name": "Shisihr",
            "e_mail": "shishir@example.com",
            "bio": "I Am The Boss"
        },
        {
            "id":2,
            "name":"Taukir",
            "e_mail": "taukir@example.com",
            "bio":"I Am Donkey"
        }
    ]


    context = {

            'members': members
    }
    return render (req,"lms/member_list.html",context=context)

def addbook(request):
    if request.method == 'GET':
        context = {
        }
        return render(request, "lms/add_edit_book.html", context=context)
    else:
        assert request.method == 'POST'
        # TODO: process the form, validate it, save into db and report to the user - on failure report error.
        title = request.POST.get('title')
        author = request.POST.get('author')
        description = request.POST.get('description')
        return HttpResponse(f"""
Title: {title}
Author: {author}
Description: {description}
""")

class AddEditBookView(View):
    template = "lms/add_edit_book.html"

    def get(self, request, book_id=None):
        errors = request.session.get('errors', {})
        # build book_data dict
        if book_id is None:  # non existing book
            book_data = {
                'title': request.session.get('title', ''),
                'author': request.session.get('author', ''),
                'description': request.session.get('description', '')
            }
            # remove data from session
            del_values_by_key(request.session, 'title', 'author', 'description', 'errors')

        else: # existing book
            _book = Book.objects.get(id=book_id)
            book_data = {
                'id': _book.id,
                'title': _book.title,
                'author': _book.author,
                'description': _book.description
            }

        context = {
            'book_data': book_data,
            'errors': errors
        }
        return render(request, self.template, context=context)

    def post(self, request, book_id=None):
        # determine if the request is for new book or editing existing book.
        book_id = request.POST.get('book_id', None)
        if not book_id:  # empty string, None
            book_id = None
        if book_id is not None:  # conversion
            book_id = int(book_id)

        # validate submitted data.
        # TODO: process the form, validate it, save into db and report to the user - on failure report error.
        title = request.POST.get('title')
        author = request.POST.get('author')
        description = request.POST.get('description')
        # TODO: validate - pure python validator
        errors = validate_book_data(request.POST)

        if errors:
            request.session['title'] = title
            request.session['author'] = author
            request.session['description'] = description
            request.session['errors'] = errors
        else:
            if book_id is None:
                book = Book()
            else:
                book = Book.objects.get(id=book_id)

            book.title = title
            book.author = author
            book.description = description
            book.save()
            messages.add_message(request, messages.INFO, f"{ 'Created' if book_id is None else 'Updated'} successfully with id {book.id}, title {book.title}")
        return redirect('add-edit-book', book_id=book_id)
