from django import forms
from .models import Carnet_Paciente


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
            'sector': forms.TextInput(attrs={'class': 'form-control-sm form-control', 'readonly': ''}),
            'prevision': forms.TextInput(attrs={'class': 'form-control-sm form-control', 'readonly': ''}),
            'grupo_sanguineo': forms.TextInput(attrs={'class': 'form-control-sm form-control', 'readonly': ''}),
            'cesfam': forms.TextInput(attrs={'class': 'form-control-sm form-control', 'readonly': ''}),
        }
