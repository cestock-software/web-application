from django import forms
from .models import Carnet_Paciente
from .models import Medicamento_Recetado


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

class MedicamentoRecetadoForm(forms.ModelForm):

    class Meta:
        model = Medicamento_Recetado

        fields = [
            'id_medicamento_recetado',
            'id_medicamento',
            'id_receta_medica',
            'duracion',
            'frecuencia',
            'cantidad_recetada',
        ]

        labels = {
            'id_medicamento_recetado': 'ID Medicamento Recetado',
            'id_medicamento': 'ID Medicamento',
            'id_receta_medica': 'ID Receta Médica',
            'duracion': 'Duración',
            'frecuencia': 'Frecuencia',
            'cantidad_recetada': 'Cant. Recetada',
        }

        widgets = {
            'id_medicamento_recetado': forms.TextInput(attrs={'class': 'form-control-sm form-control', 'readonly': ''}),
            'id_medicamento': forms.TextInput(attrs={'class': 'form-control-sm form-control', 'readonly': ''}),
            'id_receta_medica': forms.TextInput(attrs={'class': 'form-control-sm form-control', 'readonly': ''}),
            'duracion': forms.TextInput(attrs={'class': 'form-control-sm form-control', 'readonly': ''}),
            'frecuencia': forms.TextInput(attrs={'class': 'form-control-sm form-control', 'readonly': ''}),
            'cantidad_recetada': forms.TextInput(attrs={'class': 'form-control-sm form-control', 'readonly': ''}),
        }