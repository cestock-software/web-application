from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.

# class Userito(AbstractBaseUser):
#     username = models.CharField(max_length=250, unique=True)
#     rut_medico=models.CharField(default="",max_length=12,blank=True, null=True)
#     email= models.EmailField(default="",max_length=254,blank=True, null=True)

#     USERNAME_FIELD = 'username'

class Atencion_Medica(models.Model):
    nro_ficha = models.ForeignKey('Carnet_Paciente', db_column='nro_ficha',on_delete=models.CASCADE, null=True)
    fecha_atencion_medica = models.DateField(auto_now=True)
    nombre_medico = models.CharField(default="",max_length=255, blank=True, null=True)
    fecha_prox_atencion = models.DateField(auto_now=True,blank=True, null=True)

    class Meta:
        db_table = 'atencion_medica'
        verbose_name = 'Atención Medica'
        verbose_name_plural = 'Atenciones Medicas'
    
    def __str__(self):
        return f'{self.nombre_medico}'

class Carnet_Paciente(models.Model):
    nro_ficha = models.IntegerField(primary_key=True)
    rut_paciente = models.ForeignKey('Paciente', db_column='rut_paciente', on_delete=models.CASCADE, null=True)
    sector = models.CharField(default="",max_length=255, blank=True, null=True)
    prevision = models.CharField(default="",max_length=255, blank=True, null=True)
    grupo_sanguineo = models.CharField(default="",max_length=255, blank=True, null=True)
    cesfam = models.CharField(default="",max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'carnet_paciente'
        verbose_name = 'Carnet Paciente'
        verbose_name_plural = 'Carnet Pacientes'
    
    def __str__(self):
        return f'{self.nro_ficha}'

class Detalle_Atencion(models.Model):
    atencion_medica = models.ForeignKey('Atencion_Medica',on_delete=models.CASCADE,blank=True, null=True)
    sintomas = models.CharField(default="",max_length=255, blank=True, null=True)
    diagnostico = models.CharField(default="",max_length=255, blank=True, null=True)
    tratamiento = models.CharField(default="",max_length=255, blank=True, null=True)
    observacion = models.CharField(default="",max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'detalle_atencion'
        verbose_name = 'Detalle Atención'
        verbose_name_plural = 'Detalle Atenciones'

    def __str__(self):
        return f'{self.sintomas}'

class Entrega(models.Model):
    id_entrega_medicamento = models.IntegerField(primary_key=True)
    fecha_entrega = models.DateField(auto_now=True,blank=True, null=True)
    fecha_proxima_entrega = models.DateField(auto_now=True,blank=True, null=True)
    nombre_farmaceutico = models.CharField(default="",max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'entrega'
        verbose_name = 'Entrega'
        verbose_name_plural = 'Entregas'

    def __str__(self):
        return f'{self.id_entrega_medicamento}' 

class Error(models.Model):
    id_error = models.IntegerField(primary_key=True)
    nro_error = models.IntegerField(default=0,blank=True, null=True)
    codigo_error = models.CharField(default="",max_length=255, blank=True, null=True)
    fecha_hora_error = models.DateField(auto_now=True,blank=True, null=True)
    lugar_error = models.CharField(default="",max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'error'
        verbose_name = 'Error'
        verbose_name_plural = 'Errores'

    def __str__(self):
        return f'{self.id_error}'
    
class Estado_Reserva(models.Model):
    id_estado_reserva = models.CharField(primary_key=True, max_length=255)
    tipo_estado = models.CharField(default="",max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'estado_reserva'
        verbose_name = 'Estado Reserva'
        verbose_name_plural = 'Estado Reservas'

    def __str__(self):
        return f'{self.id_estado_reserva}' 

class Informe_Medicamento(models.Model):
    id_informe = models.IntegerField(primary_key=True)
    id_tipo_informe = models.ForeignKey('Tipo_Informe', db_column='id_tipo_informe', on_delete=models.CASCADE, null=True)
    id_medicamento = models.IntegerField(default=0, blank=True, null=True)
    nombre_medicamento = models.CharField(default="",max_length=255, blank=True, null=True)
    cantidad = models.CharField(default="",max_length=255, blank=True, null=True)
    nombre_farmaceutico = models.CharField(default="",max_length=255, blank=True, null=True)
    observacion = models.CharField(default="",max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'informe_medicamento'
        verbose_name = 'Informe de Medicamento'
        verbose_name_plural = 'Informes de Medicamentos'

    def __str__(self):
        return f'{self.id_informe}'
    

class Medicamento(models.Model):
    id_medicamento = models.IntegerField(primary_key=True)
    nombre_medicamento = models.CharField(default=0,max_length=255, blank=True, null=True)
    formato = models.CharField(default=0,max_length=255, blank=True, null=True)
    gr_ml = models.CharField(default=0,max_length=255, blank=True, null=True)
    laboratorio = models.CharField(default="",max_length=255, blank=True, null=True)
    total_disponible = models.IntegerField(default=0,blank=True, null=True)
    total_reservado = models.IntegerField(default=0,blank=True, null=True)
    total_retirado = models.IntegerField(default=0,blank=True, null=True)

    class Meta:
        db_table = 'medicamento'
        verbose_name = 'Medicamento'
        verbose_name_plural = 'Medicamentos'

    def __str__(self):
        return f'{self.id_medicamento}' 

class Medicamento_Entregado(models.Model):
    id_entrega_medicamento = models.ForeignKey('Entrega', db_column='id_entrega_medicamento', on_delete=models.CASCADE, null=True)
    id_medicamento_recetado = models.ForeignKey('Medicamento_Recetado', db_column='id_medicamento_recetado', on_delete=models.CASCADE, null=True)
    cantidad_entregada = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        db_table = 'medicamento_entregado'
        verbose_name = 'Medicamento Entregado'
        verbose_name_plural = 'Medicmentos Entregados'

    def __str__(self):
        return f'{self.id_entrega_medicamento}'
    
class Medicamento_Recetado(models.Model):
    id_medicamento_recetado = models.IntegerField(primary_key=True,null=True)
    id_medicamento = models.ForeignKey('Medicamento', db_column='id_medicamento', on_delete=models.CASCADE, null=True)
    id_receta_medica = models.ForeignKey('Receta_Medica', db_column='id_receta_medica', on_delete=models.CASCADE, null=True)
    duracion = models.CharField(default="",max_length=255, blank=True, null=True)
    frecuencia = models.CharField(default="",max_length=255, blank=True, null=True)
    cantidad_recetada = models.IntegerField()

    class Meta:
        db_table = 'medicamento_recetado'
        verbose_name = 'Medicamento Recetado'
        verbose_name_plural = 'Medicamentos Recetados'

    def __str__(self):
        return f'{self.id_medicamento_recetado}'
    

class Paciente(models.Model):
    rut_paciente = models.CharField(primary_key=True, max_length=255)
    nombre = models.CharField(default="",max_length=255, blank=True, null=True)
    ap_paterno = models.CharField(default="",max_length=255, blank=True, null=True)
    ap_materno = models.CharField(default="",max_length=255, blank=True, null=True)
    direccion = models.CharField(default="",max_length=255, blank=True, null=True)
    email = models.CharField(default="",max_length=255, blank=True, null=True)
    nro_celular = models.CharField(default="",max_length=255, blank=True, null=True)
    fecha_nacimiento = models.DateField(auto_now=False,null=True)
    sexo = models.CharField(default="",max_length=255, blank=True, null=True)
    comuna = models.CharField(default="",max_length=255, blank=True, null=True)
    nombre_familiar = models.CharField(default="",max_length=255, blank=True, null=True)
    nro_familiar = models.CharField(default="",max_length=255, blank=True, null=True)
    email_familiar = models.CharField(default="",max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'paciente'
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'

    def __str__(self):
        return f'{self.rut_paciente}' 

class Receta_Medica(models.Model):
    id_receta_medica = models.IntegerField(primary_key=True)
    atencion_medica = models.ForeignKey('Atencion_Medica',null=True,on_delete=models.CASCADE)

    class Meta:
        db_table = 'receta_medica'
        verbose_name = 'Receta Médica'
        verbose_name_plural = 'Recetas Médicas'

    def __str__(self):
        return f'{self.id_recid_receta_medicaeta}' 

class Reposicion(models.Model):
    id_reposicion = models.IntegerField(primary_key=True)
    id_medicamento = models.ForeignKey('Medicamento', db_column='id_medicamento',on_delete=models.CASCADE, null=True)
    cantidad_repuesta = models.FloatField( default=0,blank=True, null=True)
    fecha_reposicion = models.DateField(auto_now=True,blank=True, null=True)
    fecha_vencimiento = models.DateField(auto_now=True,blank=True, null=True)
    nombre_farmaceutico = models.CharField(default="",max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'reposicion'
        verbose_name = 'Reposición'
        verbose_name_plural = 'Repocisiones'
    
    def __str__(self):
        return f'{self.id_reposicion}' 

class Reserva(models.Model):
    id_reserva = models.IntegerField(primary_key=True)
    id_medicamento_recetado = models.ForeignKey('Medicamento', db_column='id_medicamento_recetado', on_delete=models.CASCADE, null=True)
    id_estado_reserva = models.ForeignKey('Estado_Reserva', db_column='id_estado_reserva', on_delete=models.CASCADE, null=True)
    cant_reservada = models.IntegerField(default=0,blank=True, null=True)
    fecha_reserva = models.DateField(auto_now=True)
    fecha_retiro = models.DateField(auto_now=True,blank=True, null=True)

    class Meta:
        db_table = 'reserva'
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'

    def __str__(self):
        return f'{self.id_reserva}' 

class Tipo_Informe(models.Model):
    id_tipo_informe = models.IntegerField(primary_key=True)
    tipo_informe = models.CharField(default="",max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'tipo_informe'
        verbose_name = 'Tipo Informe'
        verbose_name_plural = 'Tipo Informes'

    def __str__(self):
        return f'{self.id_tipo_informe}'
    

class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    rut_usuario = models.CharField(default="",max_length=255, blank=True, null=True)
    contrasena = models.CharField(default="",max_length=255, blank=True, null=True)
    tipo_usuario = models.CharField(default="",max_length=255, blank=True, null=True)
    nivel_usuario = models.IntegerField(default=0, blank=True, null=True)
    nombre_completo = models.CharField(default="",max_length=255, blank=True, null=True)


    class Meta:
        db_table = 'usuario'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f'{self.id_usuario}' 


class tipo_retiro(models.Model):
    id_tipo_retiro = models.IntegerField(primary_key=True)
    descripcion_retiro = models.CharField(default="",max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'tipo_retiro'
        verbose_name = 'tipo_retiro'
        verbose_name_plural = 'tipo_retiro'

    def __str__(self):
        return f'{self.id_tipo_retiro}' 

class retiro_medicamento(models.Model):
    id_retiro = models.IntegerField(primary_key=True)
    id_medicamento = models.IntegerField(default=0, blank=True, null=True)
    id_tipo_retiro = models.IntegerField(default=0, blank=True, null=True)
    cantidad_retirada = models.IntegerField(default=0, blank=True, null=True)
    fecha_retiro = models.DateField(auto_now=True,blank=True, null=True)
    class Meta:
        db_table = 'retiro_medicamento'
        verbose_name = 'retiro_medicamento'
        verbose_name_plural = 'retiro_medicamento'

    def __str__(self):
        return f'{self.id_retiro}' 


# CREATE TABLE retiro_medicamento (
#     id_retiro          NUMBER(5) NOT NULL,
#     id_medicamento     NUMBER(5) NOT NULL,
#     id_tipo_retiro     NUMBER(5) NOT NULL,
#     cantidad_retirada  NUMBER(10) NOT NULL,
#     fecha_retiro       DATE NOT NULL
# );

# ALTER TABLE retiro_medicamento ADD CONSTRAINT retiro_medicamento_pk PRIMARY KEY ( id_retiro );