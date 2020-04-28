import django_filters
from .models import *

class MedicamentoFilter(django_filters.FilterSet):
    class Meta:
        model = Medicamento
        fields = {'nombre_medicamento': ['icontains']}


class PacienteFilter(django_filters.FilterSet):
    class Meta:
        model = Paciente
        fields = {'rut_paciente': ['icontains']}

class RecetaFilter(django_filters.FilterSet):
    class Meta:
        model = Receta_Medica
        fields = {'id_receta_medica' : ['icontains']}