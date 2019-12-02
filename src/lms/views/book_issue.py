from django.shortcuts import render, redirect
from django.http import HttpResponse

from lms.models import BookIssue
from lms.models import Book, Member

def book_issue_view(reqeust):
    template = "lms/book_issue_new.html"
    members = Member.objects.all()
    books = Book.objects.all()
    context = {
        'members': members,
        'books': books,
    }
    return render(reqeust, template, context=context)



def book_return_view(request):
    raise NotImplemented



def book_issue_list(request):
    raise NotImplemented
