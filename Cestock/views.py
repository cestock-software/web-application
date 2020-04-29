from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from .forms import FormUsuarios,FormAtencion,FormPrescripcion,CarnetForm, PacienteForm
from django.utils import timezone
from django.urls import reverse
from django.db.models import Count
from .models import *
from django.contrib import messages
from .filters import *
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

# def Prescripcion(request, pk=None):
#     obj = Atencion_Medica.objects.filter(id=pk).first()
#     if request.method == "POST":
#         formP = FormPrescripcion(request.POST)
#         if formP.is_valid():
#             presc=formP.save()
#             presc.id = obj.id
#             presc.save()
#             print(formP)
#             return redirect('Cestock:PaginaPrincipal')
#         else:
#             print('form.errors_preinscripcion')
#             print(formP.errors)
#     else:
#         formP = FormPrescripcion()
#     return render(request,'Cestock/Prescripcion.html',{'formP':formP, 'pk': obj})

def AtencionMedica(request):
    if request.method == "POST":
        form = FormAtencion(request.POST)
        formP = FormPrescripcion(request.POST)
        if form.is_valid() and formP.is_valid():
            atencionmedica = form.save()
            atencionmedica.fecha_atencion_medica= timezone.now()
            atencionmedica.save()
            print(atencionmedica)
            messages.add_message(request, messages.SUCCESS, 'se ha creado con exito', extra_tags='Atencion Medica')
            presc=formP.save()
            # presc.save()
            # print(presc)
            # if atencionmedica:
            presc.atencion_medica_id = atencionmedica.id
            presc.save()
            return redirect(('Cestock:PaginaPrincipal'))
            boton()
        else:
            print(form.errors)
    
    form = FormAtencion()
    formP = FormPrescripcion()

    context = {
        'form': form,
        'formP': formP,
        
    }    
    return render(request,'Cestock/AtencionMedica.html',  context )

#-----------------------views Nico--------------------
def ListaPacientes(request):
    pacientes = Paciente.objects.all()

    filtro = PacienteFilter(request.GET, queryset=pacientes)
    pacientes = filtro.qs

    context = {'pacientes': pacientes, 'filtro': filtro}

    return render(request, "Cestock/ListaPacientes.html", context)


def StockMedicamento(request):
    medicamentos = Medicamento.objects.all()

    filtro = MedicamentoFilter(request.GET, queryset=medicamentos)
    medicamentos = filtro.qs

    context = { 
        'medicamentos': medicamentos,
        'filtro': filtro
    }

    return render(request, "Cestock/StockMedicamento.html", context)

def InfoPersonalPaciente(request, rut):
    paciente = Paciente.objects.get(rut_paciente=rut)

    if request.method == 'GET':
        form = PacienteForm(instance=paciente)
    
    return render(request, 'Cestock/InfoPersonal.html', {'form': form})


def InfoCarnetPaciente(request, rut):
    carnet = Carnet_Paciente.objects.get(rut_paciente=rut)

    if request.method == 'GET':
        form = CarnetForm(instance=carnet)

    return render(request, 'Cestock/InfoCarnet.html', {'form': form})