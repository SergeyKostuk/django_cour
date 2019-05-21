from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def len_of_coment(request):
    comemtt = request.POST.get('coment').lower()

    vowels = "aeiuoy"

    consonants = 'bcdfghjklmnpqrstvwxz'

    a = [letter for letter in comemtt if letter in vowels]
    b = [letter for letter in comemtt if letter in consonants]

    return HttpResponse(f'len of comment is: {len(comemtt)}, number of vowels: {len(a)}, number of consonats: {len(b)}')


def text_area(request):
    comentt = request.POST.get('text')
    name = request.POST.get('name')
    comentt= comentt.split('\n')
    res = []
    for i in comentt:
        res.append(f'{i} с {name}')
    strin = '<br>'.join(res)




    return HttpResponse(f'{strin}')
