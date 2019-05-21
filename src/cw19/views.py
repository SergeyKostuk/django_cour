from django.shortcuts import render
from .forms import PostForms
from django.http import HttpResponse


# Create your views here.
def record(request):
    if request.method == 'GET':
        form = PostForms()
        context = {'form': PostForms()}
        return render(request, 'record_line.html', context)

    if request.method == 'POST':
        form = PostForms(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            firstname = data.get('name')
            lastname = data.get('lastname')
            age = data.get('age')
            comment = data.get('comment')

            print(f'{firstname}|{lastname}|{age}|{comment}\n')
            context = {'form': PostForms()}
            return render(request, 'record_line.html', context)
        else:
            errors = form.errors
            return HttpResponse(f'{errors}')
