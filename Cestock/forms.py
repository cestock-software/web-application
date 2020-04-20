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
            'nro_ficha': forms.TextInput(attrs={'class': 'form-control', 'id': 'disabledTextInput'}) ,
            'rut_paciente': forms.TextInput(attrs={'class': 'form-control', 'id': 'disabledTextInput'}),
            'sector': forms.TextInput(attrs={'class': 'form-control', 'id': 'disabledTextInput'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'id': 'disabledTextInput'}),
            'nro_celular': forms.TextInput(attrs={'class': 'form-control', 'id': 'disabledTextInput'}),
            'fecha_nacimiento': forms.TextInput(attrs={'class': 'form-control', 'id': 'disabledTextInput'}),
            'sexo': forms.TextInput(attrs={'class': 'form-control', 'id': 'disabledTextInput'}),
            'prevision': forms.TextInput(attrs={'class': 'form-control', 'id': 'disabledTextInput'}),
            'grupo_sanguineo': forms.TextInput(attrs={'class': 'form-control', 'id': 'disabledTextInput'}),
            'comuna': forms.TextInput(attrs={'class': 'form-control', 'id': 'disabledTextInput'}),
            'cesfam': forms.TextInput(attrs={'class': 'form-control', 'id': 'disabledTextInput'}),
            'estado': forms.TextInput(attrs={'class': 'form-control', 'id': 'disabledTextInput'}),
        }
