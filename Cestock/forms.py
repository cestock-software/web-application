from django import forms
from .models import Usuario
from django.contrib.auth import get_user_model


User = get_user_model()

class FormUsuarios(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']