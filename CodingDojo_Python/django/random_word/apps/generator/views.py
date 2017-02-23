from django.shortcuts import render, redirect
from random import choice
from string import ascii_uppercase

def index(request):  #listens for requests
    print"*"*10
    if 'counter' not in request.session:
        request.session['counter'] = 1
    print "*"*10
    return render(request, 'generator/index.html')

def generate(request):
    request.session['counter'] += 1
    request.session['ranword'] = ''.join(choice(ascii_uppercase) for i in range(14))
    print(''.join(choice(ascii_uppercase) for i in range(14)))
    return redirect('/')
