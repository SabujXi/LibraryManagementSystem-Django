from django.shortcuts import render
from .models import (
    Book,
    Member,
)

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
    members = Member.objects.all()

    context = {

            'members': members
    }
    return render (req,"lms/member_list.html",context=context)

def addbook(request):
    context = {

    }
    return render(request, "lms/add_book.html", context=context)