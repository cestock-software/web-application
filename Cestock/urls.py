from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('main/', views.PaginaPrincipal, name='PaginaPrincipal'), 
    path('atencion-medica/', views.AtencionMedica, name='AtencionMedica'),
    path('lista-pacientes/', views.ListaPacientes, name='ListaPacientes'),
    path('info-carnet/<str:rut>', views.InfoCarnetPaciente, name='InfoCarnetPaciente'),
    path('info-personal-paciente/<str:rut>', views.InfoPersonalPaciente, name='InfoPersonalPaciente'),
    path('stock-medicamentos/', views.StockMedicamento, name='StockMedicamento'),
    path('lista-recetas/', views.ListaAtenciones, name='ListaAtenciones'),
    path('info-receta/<str:id_med>', views.InfoMedicamentoRecetado, name='InfoMedicamentoRecetado'),
]