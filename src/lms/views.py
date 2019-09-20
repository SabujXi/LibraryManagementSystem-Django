from django.shortcuts import render

# Create your views here.
def home(req):
    context = {
        'title': 'My Horrible Awesome Homepage'
    }
    return render(req, "lms/base.html", context=context)