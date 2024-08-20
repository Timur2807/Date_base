"""
В это модуле представлены представления регистрации и авторизации пользователя.
"""

from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.views import LogoutView
# from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import SignUpForm

def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            form.add_error('email', 'Пользователь с таким email уже существует')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            user.email = email
            user.first_name = first_name
            user.last_name = last_name
            user = form.save()
            form.save_m2m()
            messages.success(request, message='Вы успешно зарегистрировались')
            login(request, user)
            return redirect('account:index')
    else:
        form = SignUpForm()
        context = {
            'form': form,
        }
    return render(request, 'registration/req.html', context)


def login_user(request):
    if request.method == 'GET':
        context = {
            'form': AuthenticationForm(),
        }
        return render(request, 'registration/login.html', context)
    else:
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is None:
            context = {
                'form': AuthenticationForm(),
                'error': 'Неверные данные'
            }
            return render(request, 'registration/req.html', context)
        else:
            login(request, user)
            return redirect('account:index')

def welcome(request):
    if request.user.is_authenticated:
        return redirect('account:index')
    else:
        return render(request, 'registration/welcome.html')


def logout_user(request):
    logout(request)
    return redirect('registration:login')
