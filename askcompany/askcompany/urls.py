from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

def mysum(request, x, y):
    result=x+y
    return HttpResponse('result={}'.format(result))

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mysum/<int:x>/<int:y>', mysum),
]