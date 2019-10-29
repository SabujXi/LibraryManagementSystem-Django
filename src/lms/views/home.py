from django.shortcuts import render


def home(req):
    context = {
    }
    return render(req, "lms/home.html", context=context)

