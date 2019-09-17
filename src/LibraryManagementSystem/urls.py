from django.urls import path, include
from django.http import HttpResponse

urlpatterns = [
    path('', include('lms.urls'))
]
