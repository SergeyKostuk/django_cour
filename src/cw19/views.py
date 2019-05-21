from django.shortcuts import render
from .forms import PostForms
from django.http import HttpResponse


# Create your views here.
def record(request):
    if request.method == 'GET':
        return render(request, 'record_line.html')
    if request.method == 'POST':
        form = PostForms(request.POST)
        if form.is_valid():
            data = form.clean_data
            firstname = data.POST.get('name')
            lastname = data.POST.get('lastname')
            age = data.POST.get('age')
            comment = data.POST.get('comment')

            print(f'{firstname}|{lastname}|{age}|{comment}\n')

            return render(request, 'record_line.html')
        else:
            errors = form.errors
            return HttpResponse(f'{errors}')
