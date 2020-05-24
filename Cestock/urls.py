from django.urls import path
from . import views

app_name = 'Cestock'

urlpatterns = [
    path('', views.index, name='login'),
    path('logout/', views.logout, name="logout"),

    path('PaginaPrincipal/', views.PaginaPrincipal, name='PaginaPrincipal'),
    path('atencion-medica/', views.crearAtencionMedica, name='AtencionMedica'),
    path('atencion-medica/detalle/', views.get_atencion_detalle, name='atencion-detalle'),
    # path('prescripcion/<int:pk>/', views.Prescripcion, name='Prescripcion'),
    path('lista-pacientes/', views.ListaPacientes, name='ListaPacientes'),
    path('stock-medicamentos/', views.StockMedicamento, name='StockMedicamento'),
    # path('lista-recetas/', views.ListaRecetas, name='ListaRecetas'),
    path('InfoMedicamentoRecetado/<str:id_med>', views.InfoMedicamentoRecetado, name='InfoMedicamentoRecetado'),
    path('InfoPersonalPaciente/<str:rut>', views.InfoPersonalPaciente, name='InfoPersonalPaciente'),
    path('InfoCarnetPaciente/<str:rut>', views.InfoCarnetPaciente, name='InfoCarnetPaciente'),
    path('lista-recetas/', views.ListaAtenciones, name='ListaAtenciones'),
    path('validar_rut/', views.validar_rut, name='validar_rut'),
]