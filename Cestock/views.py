from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from .forms import FormUsuarios,FormAtencion,FormPrescripcion
from django.utils import timezone
from django.db.models import Count
from .models import Atencion_Medica,Detalle_Atencion
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
    if request.method == "POST":
        formP = FormPrescripcion(request.POST)
        
        if formP.is_valid():
           # post = form.save(commit=False)
            #post.id_detalle_atencion=1
            formP.save()
            print(formP)
            return redirect('PaginaPrincipal')    
    formP=FormPrescripcion()
    print(request.POST)
    return render(request,'Cestock/Prescripcion.html',{'formP':formP})

def AtencionMedica(request):
    if request.method == "POST":
       
        form = FormAtencion(request.POST)
     
        if form.is_valid():
            post = form.save(commit=False)
            post.fecha_hora_atencion_medica= timezone.now()
            form.save()
            #question = Atencion_Medica.objects.get(id_atencion_medica=post.id_atencion_medica)
            #return redirect('Prescripcion',pk=post.id_atencion_medica)  
            return render(request,'Cestock/Prescripcion.html')   
        else: 
            print(form.errors)
    else:
        
        form=FormAtencion()
    return render(request,'Cestock/AtencionMedica.html',{'form':form})
