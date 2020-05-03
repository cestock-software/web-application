from django.db import models
from django.contrib.auth.models import AbstractUser
#Create your models here.
class UserMedico(AbstractUser):
    username = models.CharField(max_length=250, unique=True)
    rut_medico=models.CharField(default="",max_length=12,blank=True, null=True, unique=True)
    email= models.EmailField(default="",max_length=254,blank=True, null=True)

    USERNAME_FIELD = 'username'