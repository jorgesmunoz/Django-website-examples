from django.shortcuts import render
from django.http import HttpResponse

import random


# Create your views here.
def home(request):
    return render(request, 'generator/home.html', {'password': 'random'})


def about(request):
    return render(request, 'generator/about.html')


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    # Checks if the user want uppercase
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    # Checks if the user want special characters
    if request.GET.get('special'):
        characters.extend(list('!"#$%&/()=?_'))

    # Checks if the user want numbers
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length'))
    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})
