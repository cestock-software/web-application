from django.db import models

# Create your models here.
class Atencion_Medica(models.Model):
    id_atencion_medica = models.IntegerField(primary_key=True)
    nro_ficha = models.ForeignKey('Carnet_Paciente', db_column='nro_ficha',on_delete=models.CASCADE, null=False)
    rut_medico = models.ForeignKey('Medico', db_column='rut_medico',on_delete=models.CASCADE, null=False)
    id_receta = models.ForeignKey('Receta_Medica', db_column='id_receta',on_delete=models.CASCADE, null=False)
    fecha_hora_atencion_medica = models.DateField()

    class Meta:
        db_table = 'atencion_medica'
        verbose_name = 'Atención Medica'
        verbose_name_plural = 'Atenciones Medicas'
    
    def __str__(self):
        return f'Atencion Médica: {self.id_atencion_medica}'

class Carnet_Paciente(models.Model):
    nro_ficha = models.IntegerField(primary_key=True)
    rut_paciente = models.ForeignKey('Paciente', db_column='rut_paciente', on_delete=models.CASCADE, null=False)
    sector = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    nro_celular = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=255)
    prevision = models.CharField(max_length=255)
    grupo_sanguineo = models.CharField(max_length=255)
    comuna = models.CharField(max_length=255)
    cesfam = models.CharField(max_length=255)
    estado = models.CharField(max_length=1)

    class Meta:
        db_table = 'carnet_paciente'
        verbose_name = 'Carnet Paciente'
        verbose_name_plural = 'Carnet Pacientes'
    
    def __str__(self):
        return f'Carnet Paciente: {self.nro_ficha}'

class Detalle_Atencion(models.Model):
    id_detalle_atencion = models.IntegerField(primary_key=True)
    id_atencion_medica = models.ForeignKey('Atencion_Medica', db_column='id_atencion_medica',on_delete=models.CASCADE, null=False)
    sintomas = models.CharField(max_length=255)
    diagnostico = models.CharField(max_length=255)
    tratamiento = models.CharField(max_length=255)
    observacion = models.CharField(max_length=255)
    control_medico = models.CharField(max_length=1)

    class Meta:
        db_table = 'detalle_atencion'
        verbose_name = 'Detalle Atención'
        verbose_name_plural = 'Detalle Atenciones'

    def __str__(self):
        return f'Detalle Atención: {self.id_detalle_atencion}'

class Detalle_Receta(models.Model):
    id_receta = models.OneToOneField('Receta_Medica', db_column='id_receta', primary_key=True, on_delete=models.CASCADE, null=False)
    id_medicamento = models.ForeignKey('Medicamento', db_column='id_medicamento',on_delete=models.CASCADE, null=False)
    id_entrega_medicamento = models.ForeignKey('Entrega', db_column='id_entrega_medicamento',on_delete=models.CASCADE, null=False)
    id_reserva = models.ForeignKey('Reserva', db_column='id_reserva',on_delete=models.CASCADE, null=False)
    duracion = models.CharField(max_length=255)
    frecuencia = models.CharField(max_length=255)

    class Meta:
        db_table = 'detalle_receta'
        verbose_name = 'Detalle Receta'
        verbose_name_plural = 'Detalle Recetas'
    
        def __str__(self):
            return f'Detalle Receta: {self.id_receta}'

class Entrega(models.Model):
    id_entrega_medicamento = models.IntegerField(primary_key=True)
    id_farmacia = models.ForeignKey('Farmacia', db_column='id_farmacia',on_delete=models.CASCADE, null=False)
    rut_farmaceutico = models.ForeignKey('Farmaceutico', db_column='rut_farmaceutico',on_delete=models.CASCADE, null=False)
    fecha_hora_entrega = models.DateField()
    fecha_proxima_entrega = models.DateField()

    class Meta:
        db_table = 'entrega'
        verbose_name = 'Entrega'
        verbose_name_plural = 'Entregas'

    def __str__(self):
        return f'Entrega: {self.id_entrega_medicamento}' 

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

class Estado_Reserva(models.Model):
    id_estado_reserva = models.CharField(primary_key=True, max_length=255)
    tipo_estado = models.CharField(max_length=255)

    class Meta:
        db_table = 'estado_reserva'
        verbose_name = 'Estado Reserva'
        verbose_name_plural = 'Estado Reservas'

    def __str__(self):
        return f'Estado Reserva: {self.id_estado_reserva}' 

class Farmaceutico(models.Model):
    rut_farmaceutico = models.CharField(primary_key=True, max_length=255)
    nombre_farmaceutico = models.CharField(max_length=255)
    ap_paterno = models.CharField(max_length=255)
    ap_materno = models.CharField(max_length=255)

    class Meta:
        db_table = 'farmaceutico'
        verbose_name = 'Farmaceutico'
        verbose_name_plural = 'Farmaceuticos'
    
    def __str__(self):
        return f'Farmaceutico: {self.rut_farmaceutico}' 

class Farmacia(models.Model):
    id_farmacia = models.IntegerField(primary_key=True)
    nro_farmacia = models.IntegerField()

    class Meta:
        db_table = 'farmacia'
        verbose_name = 'Farmacia'
        verbose_name_plural = 'Farmacias'
    
    def __str__(self):
        return f'Farmacia: {self.id_farmacia}' 

class Medicamento(models.Model):
    id_medicamento = models.IntegerField(primary_key=True)
    nombre_medicamento = models.CharField(max_length=255)
    formato = models.CharField(max_length=255)
    gr_ml = models.CharField(max_length=255)
    laboratorio = models.CharField(max_length=255)

    class Meta:
        db_table = 'medicamento'
        verbose_name = 'Medicamento'
        verbose_name_plural = 'Medicamentos'

    def __str__(self):
        return f'Medicamento: {self.id_medicamento}' 

class Medico(models.Model):
    rut_medico = models.CharField(primary_key=True, max_length=255)
    nombres = models.CharField(max_length=255)
    ap_paterno = models.CharField(max_length=255)
    ap_materno = models.CharField(max_length=255)
    especialidad = models.CharField(max_length=255)

    class Meta:
        db_table = 'medico'
        verbose_name = 'Medico'
        verbose_name_plural = 'Medicos'

    def __str__(self):
        return f'Medico: {self.rut_medico}' 

class Paciente(models.Model):
    rut_paciente = models.CharField(primary_key=True, max_length=255)
    nombre = models.CharField(max_length=255)
    ap_paterno = models.CharField(max_length=255)
    ap_materno = models.CharField(max_length=255)

    class Meta:
        db_table = 'paciente'
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'

    def __str__(self):
        return f'Rut Paciente: {self.rut_paciente}' 

class Receta_Medica(models.Model):
    id_receta = models.IntegerField(primary_key=True)

    class Meta:
        db_table = 'receta_medica'
        verbose_name = 'Receta Médica'
        verbose_name_plural = 'Recetas Médicas'

    def __str__(self):
        return f'Receta Medica: {self.id_receta}' 

class Reposicion(models.Model):
    id_reposicion = models.IntegerField(primary_key=True)
    id_medicamento = models.ForeignKey('Medicamento', db_column='id_medicamento',on_delete=models.CASCADE, null=False)
    rut_farmaceutico = models.ForeignKey('Farmaceutico', db_column='rut_farmaceutico',on_delete=models.CASCADE, null=False)
    cantidad_unitaria = models.IntegerField()
    fecha_hora_reposicion = models.DateField()
    fecha_vencimiento = models.DateField()

    class Meta:
        db_table = 'reposicion'
        verbose_name = 'Reposición'
        verbose_name_plural = 'Repocisiones'
    
    def __str__(self):
        return f'Reposicion: {self.id_reposicion}' 

class Reserva(models.Model):
    id_reserva = models.IntegerField(primary_key=True)
    id_medicamento = models.ForeignKey('Medicamento', db_column='id_medicamento',on_delete=models.CASCADE, null=False)
    id_estado_reserva = models.ForeignKey('Estado_Reserva', db_column='id_estado_reserva',on_delete=models.CASCADE, null=False)
    cantidad_unitaria = models.IntegerField()
    fecha_reserva = models.DateField()
    fecha_retiro = models.DateField()
    agregado = models.CharField(max_length=1)
    descontado = models.CharField(max_length=1)

    class Meta:
        db_table = 'reserva'
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'

    def __str__(self):
        return f'Reserva: {self.id_reserva}' 

class Retiro_Stock(models.Model):
    id_retiro = models.IntegerField(primary_key=True)
    id_medicamento = models.ForeignKey('Medicamento', db_column='id_medicamento',on_delete=models.CASCADE, null=False)
    id_tipo_retiro = models.ForeignKey('Tipo_Retiro', db_column='id_tipo_retiro',on_delete=models.CASCADE, null=False)
    cantidad = models.IntegerField()
    fecha_retiro = models.DateField()

    class Meta:
        db_table = 'retiro_stock'
        verbose_name = 'Retiro Stock'
        verbose_name_plural = 'Restiros Stock'

    def __str__(self):
        return f'Retiro Stock: {self.id_retiro}' 

class Stock(models.Model):
    id_stock = models.IntegerField(primary_key=True)
    id_medicamento = models.ForeignKey('Medicamento', db_column='id_medicamento',on_delete=models.CASCADE, null=False)
    cant_disponible = models.IntegerField()
    cant_reservada = models.IntegerField()

    class Meta:
        db_table = 'stock'
        verbose_name = 'Stock'
        verbose_name_plural = 'Stock'
        ordering = ['id_stock']

    def __str__(self):
        return f'Stock: {self.id_stock}' 

class Tipo_Retiro(models.Model):
    id_tipo_retiro = models.IntegerField(primary_key=True)
    razon_retiro = models.CharField(max_length=255)

    class Meta:
        db_table = 'tipo_retiro'
        verbose_name = 'Tipo Retiro'
        verbose_name_plural = 'Tipos Retiro'

    def __str__(self):
        return f'Tipo Retiro: {self.id_tipo_retiro}' 

class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    nombre_usuario = models.CharField(max_length=255)
    contrasena = models.CharField(max_length=255)
    estado = models.CharField(max_length=1)
    tipo_usuario = models.CharField(max_length=255)

    class Meta:
        db_table = 'usuario'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f'Usuario: {self.id_usuario}' 