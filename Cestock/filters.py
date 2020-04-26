import django_filters
from .models import *

class MedicamentoFilter(django_filters.FilterSet):
    class Meta:
        model = Medicamento
        fields = {'nombre_medicamento': ['icontains']}


class PacienteFilter(django_filters.FilterSet):
    class Meta:
        model = Paciente
        fields = ['nombre', 'ap_paterno', 'ap_materno']

