from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,"Cestock/index.html")

def PaginaPrincipal(request):
    return render(request,"Cestock/PaginaPrincipal.html")

def AtencionMedica(request):
    return render(request,"Cestock/AtencionMedica.html")
