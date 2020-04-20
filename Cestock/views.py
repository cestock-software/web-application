from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def index(request):
    return render(request,"Cestock/index.html")

def PaginaPrincipal(request):
    return render(request,"Cestock/PaginaPrincipal.html")

def AtencionMedica(request):
    return render(request,"Cestock/AtencionMedica.html")

def ListaPacientes(request):
    pacientes = Paciente.objects.all()
    
    context = { 'pacientes': pacientes }

    return render(request,"Cestock/ListaPacientes.html", context)

def StockMedicamento(request):
    stock = Stock.objects.all()
    medicamentos = Medicamento.objects.all()

    context = { 'stock': stock, 'medicamentos': medicamentos }

    return render(request,"Cestock/StockMedicamento.html", context)