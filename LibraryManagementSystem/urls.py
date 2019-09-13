from django.urls import path
from django.http import HttpResponse

def hello(request):
	var = "<!doctype html>\n" + ""
	return HttpResponse(var)

def hello_file(request):
	...
	return HttpResponse(var)

urlpatterns = [
	path('a', hello),
	#path('b', hello_file)
]
