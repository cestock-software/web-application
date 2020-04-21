from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from .forms import FormUsuarios,FormAtencion
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

def Prescripcion(request):
    return render(request,"Cestock/Prescripcion.html")

def AtencionMedica(request):
    if request.method == "POST":
        print(request.POST)
        form = FormAtencion(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('Prescripcion')       
    else:
        form=FormAtencion()
    print('error2')
    return render(request,'Cestock/AtencionMedica.html',{'form':form})
