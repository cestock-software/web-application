from django.contrib import admin
from .models import *

# Register your models here.
class ListaAtencion(admin.ModelAdmin):
    list_display = ['id_atencion_medica', 'nro_ficha', 'rut_medico', 'id_receta', 'fecha_hora_atencion_medica']

class ListaCarnet(admin.ModelAdmin):
    list_display = ['nro_ficha', 'rut_paciente', 'sector', 'direccion', 'nro_celular', 'fecha_nacimiento', 'sexo', 'prevision', 'grupo_sanguineo', 'comuna', 'cesfam', 'estado']

class ListaDetalleAtencion(admin.ModelAdmin):
    list_display = ['id_detalle_atencion', 'id_atencion_medica', 'sintomas', 'diagnostico', 'tratamiento', 'observacion', 'control_medico']

class ListaDetalleReceta(admin.ModelAdmin):
    list_display = ['id_receta', 'id_medicamento', 'id_entrega_medicamento', 'id_reserva', 'duracion', 'frecuencia']

class ListaDetalleAtencion(admin.ModelAdmin):
    list_display = ['id_detalle_atencion', 'id_atencion_medica', 'sintomas', 'diagnostico', 'tratamiento', 'observacion', 'control_medico']

class ListaEntrega(admin.ModelAdmin):
    list_display = ['id_entrega_medicamento', 'id_farmacia', 'rut_farmaceutico', 'fecha_hora_entrega', 'fecha_proxima_entrega']

class ListaError(admin.ModelAdmin):
    list_display = ['id_error', 'nro_error', 'codigo_error', 'fecha_hora_error', 'lugar_error']

class ListaError(admin.ModelAdmin):
    list_display = ['id_error', 'nro_error', 'codigo_error', 'fecha_hora_error', 'lugar_error']

class ListaEstadoReserva(admin.ModelAdmin):
    list_display = ['id_estado_reserva', 'tipo_estado']

class ListaFarmaceutico(admin.ModelAdmin):
    list_display = ['rut_farmaceutico', 'nombre_farmaceutico', 'ap_paterno', 'ap_materno']

class ListaFarmacia(admin.ModelAdmin):
    list_display = ['id_farmacia', 'nro_farmacia']

class ListaMedicamento(admin.ModelAdmin):
    list_display = ['id_medicamento', 'nombre_medicamento', 'formato', 'gr_ml', 'laboratorio']

class ListaMedico(admin.ModelAdmin):
    list_display = ['rut_medico', 'nombres', 'ap_paterno', 'ap_materno', 'especialidad']

class ListaPaciente(admin.ModelAdmin):
    list_display = ['rut_paciente', 'nombre', 'ap_paterno', 'ap_materno']

class ListaRecetaMedica(admin.ModelAdmin):
    list_display = ['id_receta']

class ListaReposicion(admin.ModelAdmin):
    list_display = ['id_reposicion', 'id_medicamento', 'rut_farmaceutico', 'cantidad_unitaria', 'fecha_vencimiento']

class ListaReserva(admin.ModelAdmin):
    list_display = ['id_reserva', 'id_medicamento', 'id_estado_reserva', 'cantidad_unitaria', 'fecha_reserva', 'fecha_retiro', 'agregado', 'descontado']

class ListaRetiroStock(admin.ModelAdmin):
    list_display = ['id_retiro', 'id_medicamento', 'id_tipo_retiro', 'cantidad', 'fecha_retiro']

class ListaStock(admin.ModelAdmin):
    list_display = ['id_stock', 'id_medicamento', 'cant_disponible', 'cant_reservada']

class ListaTipoRetiro(admin.ModelAdmin):
    list_display = ['id_tipo_retiro', 'razon_retiro']

class ListaUsuario(admin.ModelAdmin):
    list_display = ['id_usuario', 'nombre_usuario', 'contrasena', 'estado', 'tipo_usuario']


admin.site.register(Atencion_Medica, ListaAtencion)
admin.site.register(Carnet_Paciente, ListaCarnet)
admin.site.register(Detalle_Atencion, ListaDetalleAtencion)
admin.site.register(Detalle_Receta, ListaDetalleReceta)
admin.site.register(Entrega, ListaEntrega)
admin.site.register(Error, ListaError)
admin.site.register(Estado_Reserva, ListaEstadoReserva)
admin.site.register(Farmaceutico, ListaFarmaceutico)
admin.site.register(Farmacia, ListaFarmacia)
admin.site.register(Medicamento, ListaMedicamento)
admin.site.register(Medico, ListaMedico)
admin.site.register(Paciente, ListaPaciente)
admin.site.register(Receta_Medica, ListaRecetaMedica)
admin.site.register(Reposicion, ListaReposicion)
admin.site.register(Reserva, ListaReserva)
admin.site.register(Retiro_Stock, ListaRetiroStock)
admin.site.register(Stock, ListaStock)
admin.site.register(Tipo_Retiro, ListaTipoRetiro)
admin.site.register(Usuario, ListaUsuario)
