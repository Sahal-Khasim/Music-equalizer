from django.shortcuts import render
from django.core.paginator import Paginator
from . models import Song

# Create your views here.
def home(request):
    paginator= Song.objects.all()

    context={"paginator":paginator}
    return render(request, 'webpages/home.html', context)

def intro(request):
    return render(request, 'webpages/intro.html')

def register(request):
    return render(request, 'webpages/register.html')

def login(request):
    return render(request, 'webpages/login.html')







# def index(request):
    
#     return render(request,"index.html",context)