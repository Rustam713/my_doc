
from .models import News
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .form import UserRegisterForm
from django.contrib.auth import authenticate, login, logout


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Success')
            return redirect('/')
        else:
            messages.error(request, 'Error')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


def mylogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Пароль логин не совподают либо нету такого пользовтеля')

    return render(request, template_name='login.html')



def mylogout(request):
    logout(request)
    return redirect('/')


def index(request):
    new = News.objects.all()
    return render(request, 'index.html', {'data': new})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def glasses(request):
    return render(request, 'glasses.html')


def shop(request):
    return render(request, 'shop.html')