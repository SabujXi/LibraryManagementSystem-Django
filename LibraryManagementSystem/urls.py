from django.urls import path, include
from django.http import HttpResponse

urlpatterns = [
    path('lms/', include('lms.urls'))
]
