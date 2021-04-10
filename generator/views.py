from django.shortcuts import render
from django.http import HttpResponse
import random
import string
# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):


    characters=list(string.ascii_lowercase)
    thepassword=''
    length=int(request.GET.get('length', 12))

    if request.GET.get('Uppercase'):
        characters.extend(list(string.ascii_uppercase))

    if request.GET.get('Numbers'):
        characters.extend(list(string.digits))

    if request.GET.get('Specials'):
        characters.extend(list(string.punctuation))

    for i in range(length):
        thepassword+=random.choice(characters)
    return render(request, 'generator/password.html', {'password':thepassword})

def about(request):
    return render(request, 'generator/about.html')