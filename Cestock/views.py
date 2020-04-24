from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from .forms import FormUsuarios,FormAtencion,FormPrescripcion
from django.utils import timezone
from django.urls import reverse
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
            return redirect('Cestock:PaginaPrincipal')     
        else:
            return render(request,"Cestock/login.html") 
    else:
        return render(request,"Cestock/login.html")

def PaginaPrincipal(request):
    return render(request,"Cestock/PaginaPrincipal.html")

def Prescripcion(request, pk=None):
    obj = Atencion_Medica.objects.filter(id_atencion_medica=pk).first()
    print('--------------------------')
    print(obj.id_atencion_medica)
    if request.method == "POST":
        print('--------------------------------preinscripcion')
        formP = FormPrescripcion(request.POST)

        if formP.is_valid():
           # post = form.save(commit=False)
            presc=formP.save()
            presc.id_atencion_medica = obj
            presc.save()
            print(formP)
            return redirect('Cestock:PaginaPrincipal')
        else:
            print('form.errors_preinscripcion')
            print(formP.errors)
    formP = FormPrescripcion()
    print(request.POST)
    return render(request,'Cestock/Prescripcion.html',{'formP':formP, 'pk': obj})

def AtencionMedica(request):
    if request.method == "POST":
        print('-------------------------------atencion medica')


        form = FormAtencion(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.fecha_hora_atencion_medica= timezone.now()
            atencion = form.save()
            #question = Atencion_Medica.objects.get(id_atencion_medica=post.id_atencion_medica)
            #return redirect('Prescripcion',pk=post.id_atencion_medica)
            print('es valido')
            return redirect(reverse('Cestock:Prescripcion', kwargs={'pk': atencion.id_atencion_medica}))
        else:
            print('form.errors_atencion medica')
            print(form.errors)
    else:

        form=FormAtencion()
    return render(request,'Cestock/AtencionMedica.html', {'form':form, 'id_atencion_medica': None})