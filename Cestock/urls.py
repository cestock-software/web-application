from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('main/', views.PaginaPrincipal, name='PaginaPrincipal'), 
    path('atencion-medica/', views.AtencionMedica, name='AtencionMedica'),
    path('lista-pacientes/', views.ListaPacientes, name='ListaPacientes'),
    path('stock-medicamentos/', views.StockMedicamento, name='StockMedicamento')
]