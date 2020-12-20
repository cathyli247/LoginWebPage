from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password =request.POST.get('password')

            email = authenticate(request, email=email, password=password)

            if email is not None:
                login(request, email)
                return redirect('home')
            else:
                messages.info(request, 'Email OR password is incorrect')

        context = {}
        return render(request, 'sysadmin/login.html', context)

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'The account was created successfully!')
                return redirect('login')
        
        context = {'form' : form}
        return render(request, 'sysadmin/register.html', context)

@login_required(login_url='login')
def home(request):
    context = {}
    return render(request, 'sysadmin/home.html', context)