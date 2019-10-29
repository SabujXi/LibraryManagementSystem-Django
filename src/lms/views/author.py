from django.shortcuts import render
from django.views import View



def author_list(request):
    template = "lms/author_add_edit.html"
    context = {

    }
    return render(request, template, context)


class AuthorAddUpdate(View):
    def get(self, request):
        raise NotImplemented


    def post(self, requst):
        raise NotImplemented



def author_delete(request):
    raise NotImplemented