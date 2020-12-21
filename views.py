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
from django.contrib.auth.models import User

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
            try:
                match = User.objects.get(username=email)
            except User.DoesNotExist:
                return redirect('register', email=email)
            else:
                return redirect('login', email=email)
            
    return render(request, 'sysadmin/email.html', context)


def login(request, email=None):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = email
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Password is incorrect')

        context = {'email': email}
        return render(request, 'sysadmin/login.html', context)

def register(request, email=None):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()     
        if request.method == "POST":

            form = CreateUserForm(request.POST)
            if form.is_valid():
                try:
                    form.save()
                except forms.ValidationError:
                    messages.warning(request, 'The email is already in use.')
                else:
                    messages.success(request, 'The account was created successfully!')
                    return redirect('email')
        
        context = {'form' : form, 'email':email}
        return render(request, 'sysadmin/register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('email')

@login_required(login_url='email')
def home(request):
    context = {}
    return render(request, 'sysadmin/home.html', context)