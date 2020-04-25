from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import CarnetForm, PacienteForm
from .filters import *

# Create your views here.


def index(request):
    return render(request, "Cestock/index.html")


def PaginaPrincipal(request):
    return render(request, "Cestock/PaginaPrincipal.html")


def AtencionMedica(request):
    return render(request, "Cestock/AtencionMedica.html")


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
