from django import forms
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, ReadOnlyPasswordHashField
from django.contrib.admin.forms import AdminPasswordChangeForm
from django.forms import TextInput, Select, CharField, PasswordInput, ModelMultipleChoiceField, ModelChoiceField, ImageField, EmailInput


class UserChangeForm(forms.ModelForm):
    
    #Formulario para editar a un usuario
    
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
    def save(self, commit=True):
        id_user = self.instance.id
        if id_user:
            print("id_user", id_user)
            user_old = UserMedico.objects.get(id=id_user)

        user = super(UserChangeForm, self).save(commit=False)
        try:
            if 'password' in self.data:
                password = self.data['password']
                print("password", commit, password)
                if password and password != "":
                    user.set_password(password)
                    print("no elseee")
                    # user.password = password
            elif user_old:
                user.password = user_old.password
                print("elseee")
            if commit:
                user.save()
        except Exception as e:
            print("ERROR SAVE USER: ", e)
            if commit:
                user.save()

        return user

class UserMedicoForm(UserCreationForm):
 
    #Formulario para crear un usuario
  
    password1 = CharField(
        label='Contraseña',
        required=True,
        widget=PasswordInput(attrs={
            'placeholder': 'Ingrese su contraseña',
            'class': 'form-control form-control-user',
            'type': 'password',
        })
    )
    password2 = CharField(
        label='Repita su contraseña',
        required=True,
        widget=PasswordInput(attrs={
            'placeholder': 'Repita su contraseña',
            'class': 'form-control form-control-user',
            'type': 'password',
        })
    )
    rut_medico = forms.CharField(
        label=("Rut"), widget=forms.TextInput(
            attrs={
                'class': 'form-control valida-rut',
                'placeholder': 'Rut...',
                'required': False,
                
            })
    )

    class Meta:
        model = UserMedico
        fields = ('username', 'email', 'rut_medico')
        labels = {
            'username': ('Nombre'),
            'email': ('Correo'),
            'rut_medico': ('Rut')
        }

        widgets = {
            'username': TextInput(attrs={'placeholder': 'Ingrese nombre', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Ingrese correo', 'class': 'form-control'}),
            # 'rut_medico': TextInput(attrs={'placeholder': 'Ingrese rut', 'class': 'form-control valida-rut'}),
        }

class UserMedicoEditForm(forms.ModelForm):
    
    #Formulario para editar a un usuario
    
    rut_medico = forms.CharField(
        label=("Rut"), widget=forms.TextInput(
            attrs={
                'class': 'form-control valida-rut',
                'placeholder': 'Rut...',
                'required': False,
            })
    )
    class Meta:
        model = UserMedico
        fields = ('username', 'email', 'rut_medico')
        labels = {
            'username': ('Nombre'),
            'email': ('Correo'),
            'rut_medico': ('Rut')
        }

        widgets = {
            'username': TextInput(attrs={'placeholder': 'Ingrese nombre', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Ingrese correo', 'class': 'form-control'}),
            'rut_medico': TextInput(attrs={'placeholder': 'Ingrese rut', 'class': 'form-control valida-rut'}),
        }


# class UserDeleteForm(forms.ModelForm):
#     class Meta:
#         model = UserMedico
#         fields=['is_active']