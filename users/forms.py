from django import forms
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.admin.forms import AdminPasswordChangeForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserChangeForm(forms.ModelForm):
    '''
    Formulario para editar a un usuario
    '''
    password = ReadOnlyPasswordHashField(
        label=("password"),
        help_text= ("Raw passwords are not stored, so there is no way to see "
               "this user's password, but you can change the password "
               "using <a href=\"../password/\">this form</a>."))

    class Meta:
        model = UserMedico
        fields = (
            'username', 'email', 'rut_medico', 'password'
        )
        labels = {
            'username': 'Nombre completo',
            'rut_medico': 'Rut',
            'email': 'Correo electrónico',
        }

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre completo del usuario',
                'required': True,
                'aria-describedby': 'ID',
            }),
            'rut_medico': forms.TextInput(attrs={
                'class': 'form-control valida-rut',
                'placeholder': 'Rut del usuario',
                'required': True,
                'aria-describedby': 'ID',
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese un correo',
                'type': 'email',
                # 'required': True,
                'aria-describedby': 'emailHelp',
            }),
        }