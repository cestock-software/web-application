from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from .forms import FormUsuarios
# Create your views here.


def index(request):
    if request.method =="POST":
        username=request.POST['username']   
        password=request.POST['password']     
        user=authenticate(username=username,password=password) 
        if user is not None:
            login(request,user)
            return redirect('PaginaPrincipal')     
        else:
            return redirect('login')  
    else:
        return render(request,"Cestock/login.html")

def PaginaPrincipal(request):
    return render(request,"Cestock/PaginaPrincipal.html")

def AtencionMedica(request):
    return render(request,"Cestock/AtencionMedica.html")
