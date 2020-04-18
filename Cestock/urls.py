from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('PaginaPrincipal/', views.PaginaPrincipal, name='PaginaPrincipal'), 
    path('AtencionMedica/', views.AtencionMedica, name='AtencionMedica'), 
]