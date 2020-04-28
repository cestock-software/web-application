from django.contrib import admin
from .models import *

# Register your models here.
class ListaAtencion(admin.ModelAdmin):
    list_display = ['id_atencion_medica', 'nro_ficha', 'fecha_atencion_medica', 'nombre_medico', 'fecha_prox_atencion']

class ListaCarnet(admin.ModelAdmin):
    list_display = ['nro_ficha', 'rut_paciente', 'sector', 'prevision', 'grupo_sanguineo', 'cesfam']

class ListaDetalleAtencion(admin.ModelAdmin):
    list_display = ['id_atencion_medica', 'sintomas', 'diagnostico', 'tratamiento', 'observacion']

class ListaEntrega(admin.ModelAdmin):
    list_display = ['id_entrega_medicamento', 'fecha_entrega', 'fecha_proxima_entrega', 'nombre_farmaceutico']

class ListaError(admin.ModelAdmin):
    list_display = ['id_error', 'nro_error', 'codigo_error', 'fecha_hora_error', 'lugar_error']

class ListaEstadoReserva(admin.ModelAdmin):
    list_display = ['id_estado_reserva', 'tipo_estado']

class ListaInformeMedicamento(admin.ModelAdmin):
    list_display = ['id_informe', 'id_tipo_informe', 'id_medicamento', 'nombre_medicamento', 'cantidad', 'nombre_farmaceutico', 'observacion']

class ListaMedicamento(admin.ModelAdmin):
    list_display = ['id_medicamento', 'nombre_medicamento', 'formato', 'gr_ml', 'laboratorio', 'total_disponible', 'total_reservado', 'total_retirado']

class ListaMedicamentoEntregado(admin.ModelAdmin):
    list_display = ['id_entrega_medicamento', 'id_medicamento_recetado', 'cantidad_entregada']

class ListaMedicamentoRecetado(admin.ModelAdmin):
    list_display = ['id_medicamento_recetado', 'id_medicamento', 'duracion', 'frecuencia', 'cantidad_recetada']

class ListaPaciente(admin.ModelAdmin):
    list_display = ['rut_paciente', 'nombre', 'ap_paterno', 'ap_materno', 'direccion', 'email', 'nro_celular', 'fecha_nacimiento', 'sexo', 'comuna', 'nombre_familiar', 'email_familiar']

class ListaRecetaMedica(admin.ModelAdmin):
    list_display = ['id_receta_medica', 'id_atencion_medica']

class ListaReposicion(admin.ModelAdmin):
    list_display = ['id_reposicion', 'id_medicamento', 'cantidad_repuesta', 'fecha_reposicion', 'fecha_vencimiento', 'nombre_farmaceutico']

class ListaReserva(admin.ModelAdmin):
    list_display = ['id_reserva', 'id_medicamento_recetado', 'id_estado_reserva', 'cant_reservada', 'fecha_reserva', 'fecha_retiro']

class ListaTipoInforme(admin.ModelAdmin):
    list_display = ['id_tipo_informe', 'tipo_informe']

class ListaUsuario(admin.ModelAdmin):
    list_display = ['id_usuario', 'rut_usuario', 'contrasena', 'tipo_usuario', 'nivel_usuario', 'nombre_completo']


admin.site.register(Atencion_Medica, ListaAtencion)
admin.site.register(Carnet_Paciente, ListaCarnet)
admin.site.register(Detalle_Atencion, ListaDetalleAtencion)
admin.site.register(Entrega, ListaEntrega)
admin.site.register(Error, ListaError)
admin.site.register(Estado_Reserva, ListaEstadoReserva)
admin.site.register(Informe_Medicamento, ListaInformeMedicamento)
admin.site.register(Medicamento, ListaMedicamento)
admin.site.register(Medicamento_Entregado, ListaMedicamentoEntregado)
admin.site.register(Medicamento_Recetado, ListaMedicamentoRecetado)
admin.site.register(Paciente, ListaPaciente)
admin.site.register(Receta_Medica, ListaRecetaMedica)
admin.site.register(Reposicion, ListaReposicion)
admin.site.register(Reserva, ListaReserva)
admin.site.register(Tipo_Informe, ListaTipoInforme)
admin.site.register(Usuario, ListaUsuario)
