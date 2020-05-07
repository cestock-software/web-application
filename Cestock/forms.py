from django import forms
from .models import *




class CarnetForm(forms.ModelForm):

    class Meta:
        model = Carnet_Paciente

        fields = [
            'nro_ficha',
            'rut_paciente',
            'sector',
            'prevision',
            'grupo_sanguineo',
            'cesfam',
        ]

        labels = {
            'nro_ficha': 'Nro. Ficha',
            'rut_paciente': 'Rut Paciente',
            'sector': 'Sector',
            'prevision': 'Previsión',
            'grupo_sanguineo': 'Grupo Sanguíneo',
            'cesfam': 'CESFAM',
        }

        widgets = {
            'nro_ficha': forms.TextInput(attrs={'class': 'form-control-sm form-control', 'readonly': ''}),
            'rut_paciente': forms.TextInput(attrs={'class': 'form-control-sm form-control', 'readonly': ''}),
            'sector': forms.TextInput(attrs={'class': 'form-control-sm form-control', 'readonly': '', 'style': 'text-transform: capitalize'}),
            'prevision': forms.TextInput(attrs={'class': 'form-control-sm form-control', 'readonly': ''}),
            'grupo_sanguineo': forms.TextInput(attrs={'class': 'form-control-sm form-control', 'readonly': ''}),
            'cesfam': forms.TextInput(attrs={'class': 'form-control-sm form-control', 'readonly': ''}),
        }


class PacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente

        fields = '__all__'

        exclude = [
            'rut_paciente', 
            'nombre',
            'ap_paterno', 
            'ap_materno', 
            'sexo',
            'fecha_nacimiento',
            'estado'
        ]

        labels = {
            'direccion': 'Dirección',
            'email': 'Correo',
            'nro_celular': 'Nro. Celular',
            'comuna': 'Comuna',
            'nombre_familiar': 'Nombre del Familiar',
            'nro_familiar': 'Nro. del Familiar',
            'email_familiar': 'Correo  del Familiar'
        }

        widgets = {
            'direccion': forms.TextInput(attrs={'class': 'form-control-sm form-control', 'readonly': ''}),
            'email': forms.TextInput(attrs={'class': 'form-control-sm form-control', 'readonly': ''}),
            'nro_celular': forms.TextInput(attrs={'class': 'form-control-sm form-control', 'readonly': ''}),
            'comuna': forms.TextInput(attrs={'class': 'form-control-sm form-control', 'readonly': '', 'style': 'text-transform: capitalize'}),
            'nombre_familiar': forms.TextInput(attrs={'class': 'form-control-sm form-control', 'readonly': ''}),
            'nro_familiar': forms.TextInput(attrs={'class': 'form-control-sm form-control', 'readonly': ''}),
            'email_familiar': forms.TextInput(attrs={'class': 'form-control-sm form-control', 'readonly': ''}),
        }

class MedicamentoRecetadoForm(forms.ModelForm):

    class Meta:
        model = Medicamento_Recetado

        fields = [
            'id_receta_medica',
            'id_medicamento',
            'duracion',
            'frecuencia',
            'cantidad_recetada',
        ]

        labels = {
            'id_receta_medica': 'ID Receta',
            'id_medicamento': 'ID Medicamento',
            'duracion': 'Duración',
            'frecuencia': 'Frecuencia',
            'cantidad_recetada': 'Cant. Recetada',
        }

        widgets = {
            'id_receta_medica': forms.TextInput(attrs={'class': 'form-control-sm form-control', 'readonly': ''}),
            'id_medicamento': forms.TextInput(attrs={'class': 'form-control-sm form-control', 'readonly': ''}),
            'duracion': forms.TextInput(attrs={'class': 'form-control-sm form-control', 'readonly': ''}),
            'frecuencia': forms.TextInput(attrs={'class': 'form-control-sm form-control', 'readonly': ''}),
            'cantidad_recetada': forms.TextInput(attrs={'class': 'form-control-sm form-control', 'readonly': ''}),
        }