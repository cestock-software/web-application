from django import forms
from .models import Usuario,Atencion_Medica,Detalle_Atencion
from django.contrib.auth import get_user_model
from users.models import *

User = get_user_model()

class FormUsuarios(forms.ModelForm):
    class Meta:
        model=UserMedico
        fields=['username','password']

class FormAtencion(forms.ModelForm):
    class Meta:
        model=Atencion_Medica
        fields = (
            'nro_ficha', 'nombre_medico'
        )
        widgets = {
            'nombre_medico': forms.TextInput(attrs={
                'class': 'form-control responsive',
                'placeholder': 'Ingrese Nombre de Medico',
                'required': True,
                
            }), 
            'nro_ficha': forms.TextInput(attrs={
                'class': 'form-control responsive',
                'placeholder': 'Ingrese Numero de Ficha',
                'required': True, 
                
            }),
        }

    # def clean_nro_ficha(self):
    #         nro_ficha = self.cleaned_data['nro_ficha']
    #         fichas = Carnet_Paciente.objects.filter(nro_ficha__iexact=nro_ficha)
    #         if self.instance:
    #             fichas = fichas.exclude(id=self.instance.id)
    #         if fichas.count() is None:
    #             raise ValidationError('Lo sentimos, pero esta ficha no existe')
    #         else:
    #             return nro_ficha
       

class FormPrescripcion(forms.ModelForm):
    class Meta:
        model=Detalle_Atencion
        fields = (
            'sintomas', 'diagnostico','tratamiento','observacion'
        )

        widgets = {
            'sintomas': forms.Textarea(attrs={
                'rows': '3',
                'class': 'textotal form-control',
                'placeholder': 'Ingrese Sintomas del Paciente..',
                'required': True,
            }),
            'diagnostico': forms.Textarea(attrs={
                'rows': '3',
                'class': 'textotal form-control',
                'placeholder': 'Ingrese Diagnostico del Paciente..',
                'required': True,
            }),
            'tratamiento': forms.Textarea(attrs={
                'rows': '3',
                'class': 'textotal form-control',
                'placeholder': 'Ingrese Tratamiento para el Paciente..',
                'required': True,
            }),
            'observacion': forms.Textarea(attrs={
                'rows': '3',
                'class': 'textotal form-control',
                'placeholder': 'Ingrese Observacion..',
            }),
        }