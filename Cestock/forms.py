from django import forms
from .models import Usuario,Atencion_Medica,Detalle_Atencion
from django.contrib.auth import get_user_model


User = get_user_model()

class FormUsuarios(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']

class FormAtencion(forms.ModelForm):
    class Meta:
        model=Atencion_Medica
        fields=['id_atencion_medica','nro_ficha','rut_medico']

class FormPrescripcion(forms.ModelForm):
    class Meta:
        model=Detalle_Atencion
        fields=['id_detalle_atencion','id_atencion_medica','sintomas','diagnostico','tratamiento','observacion'] 




