from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your views here.

def casa(request):
    return render(request, 'main.html')

def registro(request):
    if request.method == 'GET':
        print("enviando form")
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user=User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                return HttpResponse("usuario creado satisfactioriamente ")
            except:
                return HttpResponse("no se pudo crear el usuario")
        print(request.POST)
        print("recibiendo datos")    
    return render(request, 'registro.html', {
        'form': UserCreationForm
    })


