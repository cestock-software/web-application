from django.urls import path
from . import views

app_name = 'Cestock'

urlpatterns = [
    path('', views.index, name='login'),
    path('logout/', views.logout, name="logout"),

    path('main/', views.PaginaPrincipal, name='PaginaPrincipal'),
    path('atencion-medica/', views.crearAtencionMedica, name='AtencionMedica'),
    path('atencion-medica/detalle/', views.get_atencion_detalle, name='atencion-detalle'),
    # path('prescripcion/<int:pk>/', views.Prescripcion, name='Prescripcion'),
    path('lista-pacientes/', views.ListaPacientes, name='ListaPacientes'),
    path('stock-medicamentos/', views.StockMedicamento, name='StockMedicamento'),
    path('lista-atenciones/', views.ListaAtenciones, name='ListaAtenciones'),
    # path('info-detalle-atencion/<int:id_atencion>', views.InfoDetalleAtencion, name='InfoDetalleAtencion'),
    path('info-receta-medica/<str:id_med>', views.InfoMedicamentoRecetado, name='InfoMedicamentoRecetado'),
    path('info-personal-paciente/<str:rut>', views.InfoPersonalPaciente, name='InfoPersonalPaciente'),
    path('info-carnet-paciente/<str:rut>', views.InfoCarnetPaciente, name='InfoCarnetPaciente'),
]