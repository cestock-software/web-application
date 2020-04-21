from django import forms
from .models import Carnet_Paciente


class CarnetForm(forms.ModelForm):

    class Meta:
        model = Carnet_Paciente

        fields = [
            'nro_ficha',
            'rut_paciente',
            'sector',
            'direccion',
            'nro_celular',
            'fecha_nacimiento',
            'sexo',
            'prevision',
            'grupo_sanguineo',
            'comuna',
            'cesfam',
            'estado',
        ]

        labels = {
            'nro_ficha': 'Nro. Ficha',
            'rut_paciente': 'Rut Paciente',
            'sector': 'Sector',
            'direccion': 'Dirección',
            'nro_celular': 'Nro. Celular',
            'fecha_nacimiento': 'Fecha Nacimiento',
            'sexo': 'Sexo',
            'prevision': 'Previsión',
            'grupo_sanguineo': 'Grupo Sanguíneo',
            'comuna': 'Comuna',
            'cesfam': 'CESFAM',
            'estado': 'Estado',
        }
        
        widgets = {
            'nro_ficha': forms.TextInput(attrs={'class': 'form-control-sm form-control', 'readonly': ''}),
            'rut_paciente': forms.TextInput(attrs={'class': 'form-control-sm form-control', 'readonly': ''}),
            'sector': forms.TextInput(attrs={'class': 'form-control-sm form-control', 'readonly': ''}),
            'direccion': forms.TextInput(attrs={'class': 'form-control-sm form-control', 'readonly': ''}),
            'nro_celular': forms.TextInput(attrs={'class': 'form-control-sm form-control', 'readonly': ''}),
            'fecha_nacimiento': forms.TextInput(attrs={'class': 'form-control-sm form-control', 'readonly': ''}),
            'sexo': forms.TextInput(attrs={'class': 'form-control-sm form-control', 'readonly': ''}),
            'prevision': forms.TextInput(attrs={'class': 'form-control-sm form-control', 'readonly': ''}),
            'grupo_sanguineo': forms.TextInput(attrs={'class': 'form-control-sm form-control', 'readonly': ''}),
            'comuna': forms.TextInput(attrs={'class': 'form-control-sm form-control', 'readonly': ''}),
            'cesfam': forms.TextInput(attrs={'class': 'form-control-sm form-control', 'readonly': ''}),
            'estado': forms.TextInput(attrs={'class': 'form-control-sm form-control', 'readonly': ''}),
        }
