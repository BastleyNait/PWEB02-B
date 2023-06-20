from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
# Create your views here.


def casa(request):
    return render(request, 'main.html')


def registro(request):

    if request.method == 'GET':
        print("enviando form")
        return render(request, 'registro.html', {
            'form': UserCreationForm
        })

    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tareas')
            except IntegrityError:
                return render(request, 'registro.html', {
                    'form': UserCreationForm,
                    'error': 'el usuario ya existe elija otro nombre'
                })
        return render(request, 'registro.html', {
            'form': UserCreationForm,
            'error': 'las contraseñas no coiciden'
        })


def tareas(request):
    return render(request, 'tareas.html')


def salir(request):
    logout(request)
    return redirect('main')


def iniciaSesion(request):
    if request.method == 'GET':
        print("enviando form")
        return render(request, 'login.html', {
            'form': AuthenticationForm
        })

    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {
                'form': AuthenticationForm,
                'error':"el usuario o la contraseña no existen"
            })
        else:
            login(request, user)
            return redirect('tareas')
    
