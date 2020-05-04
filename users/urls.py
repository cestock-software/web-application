from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('crear/', views.UserCreate.as_view(), name='crear_doctor'),
    path('editar/<int:pk>/', views.user_update, name='editar_doctor'),
    path('lista/', views.lista_users, name='lista_users'),
    path('datatable/', views.usuario_lista_database, name='usuario_lista_database'),
    path('eliminar/', views.eliminar_doctor, name='eliminar_doctor'),


]