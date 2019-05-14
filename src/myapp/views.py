from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index1(request):
    if request.method == "POST":
        name = request.POST.get('name')
        return HttpResponse('len is {}'.format(len(name)))
    return HttpResponse('Its GET request')
def index2(request):
    if int(request.POST.get('age')) >= 18:

        return HttpResponse('добро пожаловать')
    else:
        return HttpResponse('в доступе отказано')
