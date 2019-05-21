from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.
def record(request):
    if request.method == 'GET':
        return render(request, 'record_line.html')
    if request.method == 'POST':
        firstname = request.POST.get('name')
        lastname = request.POST.get('lastname')
        age = request.POST.get('age')
        comment = request.POST.get('comment')

        print(f'{firstname}|{lastname}|{age}|{comment}\n')

        return render(request, 'record_line.html')
