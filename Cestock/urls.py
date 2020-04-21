from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='login'), 
    path('PaginaPrincipal/', views.PaginaPrincipal, name='PaginaPrincipal'), 
    path('atencion-medica/', views.AtencionMedica, name='AtencionMedica'), 
    path('prescripcion/', views.Prescripcion, name='Prescripcion'), 
]