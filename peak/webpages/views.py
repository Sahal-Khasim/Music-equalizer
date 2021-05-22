from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'webpages/home.html')

def intro(request):
    return render(request, 'webpages/intro.html')