from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from .forms import FormUsuarios,FormAtencion,FormPrescripcion
from django.utils import timezone
from django.urls import reverse
from django.db.models import Count
from .models import Atencion_Medica,Detalle_Atencion
from django.contrib import messages
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
    obj = Atencion_Medica.objects.filter(id=pk).first()
    if request.method == "POST":
        formP = FormPrescripcion(request.POST)
        if formP.is_valid():
            presc=formP.save()
            presc.id = obj.id
            presc.save()
            print(formP)
            return redirect('Cestock:PaginaPrincipal')
        else:
            print('form.errors_preinscripcion')
            print(formP.errors)
    else:
        formP = FormPrescripcion()
    return render(request,'Cestock/Prescripcion.html',{'formP':formP, 'pk': obj})

def AtencionMedica(request):
    if request.method == "POST":
        form = FormAtencion(request.POST)
        formP = FormPrescripcion(request.POST)
        if form.is_valid() and formP.is_valid():
            atencionmedica = form.save()
            atencionmedica.fecha_atencion_medica= timezone.now()
            atencionmedica.save()
            print(atencionmedica)
            messages.add_message(request, messages.SUCCESS, 'se ha creado con exito', extra_tags='Evento')
            presc=formP.save()
            presc.save()
            print(presc)
            if atencionmedica:
                presc.id = atencionmedica.id
            presc.save()
            return redirect(reverse('Cestock:PaginaPrincipal'))
        else:
            print(form.errors)
    else:
        form = FormAtencion()
        formP = FormPrescripcion()

    context = {
        'form': form,
        'formP': formP,
        'id': None
    }    
    return render(request,'Cestock/AtencionMedica.html',  context )