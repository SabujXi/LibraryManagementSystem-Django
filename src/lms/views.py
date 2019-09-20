from django.shortcuts import render

# Create your views here.
def home(req):
    context = {

    }
    return render(req, "lms/base.html", context=context)