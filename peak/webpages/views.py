from os import name
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'webpages/home.html')

def intro(request):
    return render(request, 'webpages/intro.html')

def register(request):
    return render(request, 'webpages/register.html')

def login(request):
    return render(request, 'webpages/login.html')



from django.core.paginator import Paginator
from . models import DefaultSongs

def index(request):
    songs = DefaultSongs.objects.all()
    context={"songs":songs}
    return render(request,"home.html",context)