from django.shortcuts import render
from django.core.paginator import Paginator
from . models import Song

# Create your views here.
def home(request):
    paginator= Paginator(Song.objects.all(),1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={"page_obj":page_obj}
    return render(request, 'webpages/home.html', context)

def intro(request):
    return render(request, 'webpages/intro.html')

def register(request):
    return render(request, 'webpages/register.html')

def login(request):
    return render(request, 'webpages/login.html')





# def index(request):
    
#     return render(request,"index.html",context)