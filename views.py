from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django import forms

# Create your views here.
def email(request):
    email = 'email'
    context = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            validate_email(email)
        except forms.ValidationError:
            context = {'errors':'Email format is incorrect'}
        else:
            return redirect('login')
    return render(request, 'sysadmin/email.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('email')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
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

def logoutUser(request):
    logout(request)
    return redirect('email')

@login_required(login_url='email')
def home(request):
    context = {}
    return render(request, 'sysadmin/home.html', context)