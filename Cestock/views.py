from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from .forms import *
from django.utils import timezone
from django.urls import reverse
from django.db.models import Count
from .models import *
from django.contrib import messages
from .filters import *
import datetime
import locale
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
    # Para que te tome el tiempo local
    locale.setlocale(locale.LC_TIME, '')

    atenciones_medicas_data = []
    dia_actual = datetime.datetime.now()
    # 0 es lunes y 6 es domingo
    numero_dia_en_semana = datetime.datetime.weekday(dia_actual)
    # el lunes es el dia actual menos en numero de este en la semana, el domingo es el primero mas 6
    primer_dia_semana = dia_actual - datetime.timedelta(days=numero_dia_en_semana)
    ultimo_dia_semana = primer_dia_semana + datetime.timedelta(days=6)
    d = datetime.timedelta(days=1)

    # Recorres del primer dia a el ultimo contado las atenciones medicas de ese dia
    while primer_dia_semana <= ultimo_dia_semana:
        atenciones_medicas_dia = Atencion_Medica.objects.filter(fecha_atencion_medica__day=primer_dia_semana.day, fecha_atencion_medica__month=primer_dia_semana.month, fecha_atencion_medica__year=primer_dia_semana.year)
        # Cambio el formato de la fecha %d es dia en número , %b es mes de manera corta
        date_text = str(primer_dia_semana.strftime("%d %b. "))

        # total(cantidad) de atenciones en ese dia, fecha seleccionada
        info = {}
        info['fecha'] = date_text
        info['total_cant_atenciones'] = len(atenciones_medicas_dia)

        atenciones_medicas_data.append(info)
        primer_dia_semana += d
    print(atenciones_medicas_data)
    ultimas_atenciones_medicas = Atencion_Medica.objects.order_by('-id')[:4]
    context = {
        'ultimas_atenciones_medicas': ultimas_atenciones_medicas,
        'atenciones_medicas_data': atenciones_medicas_data,
        'year': dia_actual.year

    }

    return render(request, "Cestock/PaginaPrincipal.html", context)

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



def ListaRecetas(request):
    recetas = Receta_Medica.objects.all()

    filtro = RecetaFilter(request.GET, queryset=recetas)
    recetas = filtro.qs

    context = {'recetas': recetas, 'filtro': filtro}

    return render(request, "Cestock/ListaRecetas.html", context)


def InfoMedicamentoRecetado(request, id_med):
    med_recetado = Medicamento_Recetado.objects.get(id_receta_medica=id_med)

    if request.method == 'GET':
        form = MedicamentoRecetadoForm(instance=med_recetado)

    return render(request, 'Cestock/InfoMedicamentoRecetado.html', {'form': form})