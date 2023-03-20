from django.shortcuts import render
import random


def about(requests):
    return render(requests, 'generator/about.html') 


def home(request):
    return render(request, 'generator/home.html')

def password(request):
    characters = list('abcdefghijklmnopgrstuvwxyz')
    if request.GET.get('lowercase'):
        characters.extend(list('abcdefghijklmnopqrstuvwxys'))
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    
    length = int(request.GET.get('length', 12))
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})











