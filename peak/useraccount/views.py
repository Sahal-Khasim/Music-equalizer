from django import conf
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import logout

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Your logged in')
            return redirect('home')
        else:
            messages.warning(request, 'Invalid username or password')
            return redirect('login')


    return render(request, 'useraccount/login.html')



def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        email = request.POST['email']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.warning(request, 'Username Exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.warning(request, 'Email Exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(
                        username=username,
                        password=password,
                        email=email,
                    )
                    user.save()
                    messages.success(request, 'Account Created Successfully')
                    return redirect('login')
        else:
            messages.warning(request, 'Password Do Not Match!')
            return redirect('register')


    return render(request, 'useraccount/register.html')



def logout_user(request):
    logout(request)
    return redirect('home')