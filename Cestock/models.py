from django.db import models

# Create your models here.
class Atencion_Medica(models.Model):
    id_atencion_medica = models.IntegerField(primary_key=True)
    nro_ficha = models.ForeignKey('Carnet_Paciente', db_column='nro_ficha',on_delete=models.CASCADE, null=False)
    fecha_atencion_medica = models.DateField()
    nombre_medico = models.CharField(max_length=255)
    fecha_prox_atencion = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'atencion_medica'
        verbose_name = 'Atención Medica'
        verbose_name_plural = 'Atenciones Medicas'
    
    def __str__(self):
        return f'{self.id_atencion_medica}'

class Carnet_Paciente(models.Model):
    nro_ficha = models.IntegerField(primary_key=True)
    rut_paciente = models.ForeignKey('Paciente', db_column='rut_paciente', on_delete=models.CASCADE, null=False)
    sector = models.CharField(max_length=255)
    prevision = models.CharField(max_length=255)
    grupo_sanguineo = models.CharField(max_length=255)
    cesfam = models.CharField(max_length=255)

    class Meta:
        db_table = 'carnet_paciente'
        verbose_name = 'Carnet Paciente'
        verbose_name_plural = 'Carnet Pacientes'
    
    def __str__(self):
        return f'{self.nro_ficha}'

class Detalle_Atencion(models.Model):
    id_atencion_medica = models.ForeignKey('Atencion_Medica', db_column='id_atencion_medica', on_delete=models.CASCADE, null=False)
    sintomas = models.CharField(max_length=255)
    diagnostico = models.CharField(max_length=255)
    tratamiento = models.CharField(max_length=255, blank=True, null=True)
    observacion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'detalle_atencion'
        verbose_name = 'Detalle Atención'
        verbose_name_plural = 'Detalle Atenciones'

    def __str__(self):
        return f'{self.id_atencion_medica}'

class Entrega(models.Model):
    id_entrega_medicamento = models.IntegerField(primary_key=True)
    fecha_entrega = models.DateField()
    fecha_proxima_entrega = models.DateField(blank=True, null=True)
    nombre_farmaceutico = models.CharField(max_length=255)

    class Meta:
        db_table = 'entrega'
        verbose_name = 'Entrega'
        verbose_name_plural = 'Entregas'

    def __str__(self):
        return f'{self.id_entrega_medicamento}' 

class Error(models.Model):
    id_error = models.IntegerField(primary_key=True)
    nro_error = models.IntegerField()
    codigo_error = models.CharField(max_length=255)
    fecha_hora_error = models.DateField()
    lugar_error = models.CharField(max_length=255)

    class Meta:
        db_table = 'error'
        verbose_name = 'Error'
        verbose_name_plural = 'Errores'

    def __str__(self):
        return f'{self.id_error}'
    
class Estado_Reserva(models.Model):
    id_estado_reserva = models.CharField(primary_key=True, max_length=255)
    tipo_estado = models.CharField(max_length=255)

    class Meta:
        db_table = 'estado_reserva'
        verbose_name = 'Estado Reserva'
        verbose_name_plural = 'Estado Reservas'

    def __str__(self):
        return f'{self.id_estado_reserva}' 

class Informe_Medicamento(models.Model):
    id_informe = models.IntegerField(primary_key=True)
    id_tipo_informe = models.ForeignKey('Tipo_Informe', db_column='id_tipo_informe', on_delete=models.CASCADE, null=False)
    id_medicamento = models.IntegerField()
    nombre_medicamento = models.CharField(max_length=255)
    cantidad = models.CharField(max_length=255)
    nombre_farmaceutico = models.CharField(max_length=255)
    observacion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'informe_medicamento'
        verbose_name = 'Informe de Medicamento'
        verbose_name_plural = 'Informes de Medicamentos'

    def __str__(self):
        return f'{self.id_informe}'
    

class Medicamento(models.Model):
    id_medicamento = models.IntegerField(primary_key=True)
    nombre_medicamento = models.CharField(max_length=255)
    formato = models.CharField(max_length=255)
    gr_ml = models.CharField(max_length=255)
    laboratorio = models.CharField(max_length=255)
    total_disponible = models.IntegerField()
    total_reservado = models.IntegerField(blank=True, null=True)
    total_retirado = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'medicamento'
        verbose_name = 'Medicamento'
        verbose_name_plural = 'Medicamentos'

    def __str__(self):
        return f'{self.id_medicamento}' 

class Medicamento_Entregado(models.Model):
    id_entrega_medicamento = models.ForeignKey('Entrega', db_column='id_entrega_medicamento', on_delete=models.CASCADE, null=False)
    id_medicamento_recetado = models.ForeignKey('Medicamento_Recetado', db_column='id_medicamento_recetado', on_delete=models.CASCADE, null=False)
    cantidad_entregada = models.IntegerField()

    class Meta:
        db_table = 'medicamento_entregado'
        verbose_name = 'Medicamento Entregado'
        verbose_name_plural = 'Medicmentos Entregados'

    def __str__(self):
        return f'{self.id_entrega_medicamento}'
    
class Medicamento_Recetado(models.Model):
    id_medicamento_recetado = models.IntegerField(primary_key=True)
    id_medicamento = models.ForeignKey('Medicamento', db_column='id_medicamento', on_delete=models.CASCADE, null=False)
    id_receta_medica = models.ForeignKey('Receta_Medica', db_column='id_receta_medica', on_delete=models.CASCADE, null=False)
    duracion = models.CharField(max_length=255)
    frecuencia = models.CharField(max_length=255)
    cantidad_recetada = models.IntegerField()

    class Meta:
        db_table = 'medicamento_recetado'
        verbose_name = 'Medicamento Recetado'
        verbose_name_plural = 'Medicamentos Recetados'

    def __str__(self):
        return f'{self.id_medicamento_recetado}'
    

class Paciente(models.Model):
    rut_paciente = models.CharField(primary_key=True, max_length=255)
    nombre = models.CharField(max_length=255)
    ap_paterno = models.CharField(max_length=255)
    ap_materno = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    nro_celular = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=255)
    comuna = models.CharField(max_length=255)
    nombre_familiar = models.CharField(max_length=255)
    nro_familiar = models.CharField(max_length=255)
    email_familiar = models.CharField(max_length=255)

    class Meta:
        db_table = 'paciente'
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'

    def __str__(self):
        return f'{self.rut_paciente}' 

class Receta_Medica(models.Model):
    id_receta = models.IntegerField(primary_key=True)
    id_atencion_medica = models.ForeignKey('Atencion_Medica', db_column='id_atencion_medica', on_delete=models.CASCADE, null=False)

    class Meta:
        db_table = 'receta_medica'
        verbose_name = 'Receta Médica'
        verbose_name_plural = 'Recetas Médicas'

    def __str__(self):
        return f'{self.id_receta}' 

class Reposicion(models.Model):
    id_reposicion = models.IntegerField(primary_key=True)
    id_medicamento = models.ForeignKey('Medicamento', db_column='id_medicamento',on_delete=models.CASCADE, null=False)
    cantidad_repuesta = models.FloatField()
    fecha_reposicion = models.DateField()
    fecha_vencimiento = models.DateField()
    nombre_farmaceutico = models.CharField(max_length=255)

    class Meta:
        db_table = 'reposicion'
        verbose_name = 'Reposición'
        verbose_name_plural = 'Repocisiones'
    
    def __str__(self):
        return f'{self.id_reposicion}' 

class Reserva(models.Model):
    id_reserva = models.IntegerField(primary_key=True)
    id_medicamento_recetado = models.ForeignKey('Medicamento', db_column='id_medicamento_recetado', on_delete=models.CASCADE, null=False)
    id_estado_reserva = models.ForeignKey('Estado_Reserva', db_column='id_estado_reserva', on_delete=models.CASCADE, null=False)
    cant_reservada = models.IntegerField()
    fecha_reserva = models.DateField()
    fecha_retiro = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'reserva'
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'

    def __str__(self):
        return f'{self.id_reserva}' 

class Tipo_Informe(models.Model):
    id_tipo_informe = models.IntegerField(primary_key=True)
    tipo_informe = models.CharField(max_length=255)

    class Meta:
        db_table = 'tipo_informe'
        verbose_name = 'Tipo Informe'
        verbose_name_plural = 'Tipo Informes'

    def __str__(self):
        return f'{self.id_tipo_informe}'
    

class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    rut_usuario = models.CharField(max_length=255)
    contrasena = models.CharField(max_length=255)
    tipo_usuario = models.CharField(max_length=255)
    nivel_usuario = models.IntegerField()
    nombre_completo = models.CharField(max_length=255)


    class Meta:
        db_table = 'usuario'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f'{self.id_usuario}' 