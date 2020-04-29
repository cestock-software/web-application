from django.urls import path
from . import views

app_name = 'Cestock'

urlpatterns = [
    path('', views.index, name='login'),
    path('PaginaPrincipal/', views.PaginaPrincipal, name='PaginaPrincipal'),
    path('atencion-medica/', views.AtencionMedica, name='AtencionMedica'),
    # path('prescripcion/<int:pk>/', views.Prescripcion, name='Prescripcion'),
    path('lista-pacientes/', views.ListaPacientes, name='ListaPacientes'),
    path('info-carnet/<str:rut>', views.InfoCarnetPaciente, name='InfoCarnetPaciente'),
    path('info-personal-paciente/<str:rut>', views.InfoPersonalPaciente, name='InfoPersonalPaciente'),
    path('stock-medicamentos/', views.StockMedicamento, name='StockMedicamento')
]