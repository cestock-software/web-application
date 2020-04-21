from django import forms
from .models import Usuario,Atencion_Medica
from django.contrib.auth import get_user_model


User = get_user_model()

class FormUsuarios(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']

class FormAtencion(forms.ModelForm):
    class Meta:
        model=Atencion_Medica
        fields=['id_atencion_medica','nro_ficha','rut_medico','fecha_hora_atencion_medica']
        


