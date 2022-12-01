from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):
    characters = list('abcdefghijklmnoprstuvxyz')

    lenght = int(request.GET.get('lenght',14))
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHTIJKLMNOPRSTTUWXYZ'))
    if request.GET.get('numbers'):
        characters.extend('1234567890')
    if request.GET.get('special'):
        characters.extend('!@#$%^&*()')
    thepassword = ''
    for x in range(lenght):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html',{'password': thepassword})

def about(requerst):
    return render(requerst, 'generator/about.html')