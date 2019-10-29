from django.shortcuts import render


def about(req):
    context = {
    }
    return render(req, "lms/about.html", context=context)