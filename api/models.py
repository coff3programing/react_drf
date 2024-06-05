from django.db import models

# Create your models here.
class MarcasModel(models.Model):
    nombre = models.CharField(max_length=255)


    #* Auditorie models
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'marcas'
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"

    def __str__(self):
        return self.nombre

class LaboratoriosModel(models.Model):
    nombre_laboratorio = models.CharField(max_length=255)
    
    
    #* Auditorie models
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'laboratorios'
        verbose_name = "Laboratorio"
        verbose_name_plural = "Laboratorios"

    def __str__(self):
        return self.nombre_laboratorio

class ActivosModel(models.Model):
    ESTADO_CHOICES = [
        ('EN_USO', 'En uso'),
        ('EN_REPARACION', 'En reparacion'),
    ]

    laboratorio = models.ForeignKey(
        LaboratoriosModel,
        related_name='activos',
        on_delete=models.CASCADE
    )

    codigo_activo = models.CharField(max_length=12)
    nombre_activo = models.CharField(max_length=25)
    
    marca = models.ForeignKey(
        MarcasModel,
        related_name='activos',
        on_delete=models.CASCADE
    )

    estado = models.CharField(
        max_length=16,
        choices=ESTADO_CHOICES,
        default='EN_USO'
    )

    descripcion = models.TextField(blank=True)

    class Meta:
        db_table = 'activos'
        verbose_name = "Activo"
        verbose_name_plural = "Activos"

    def __str__(self):
        return f"{self.nombre_activo} ({self.codigo_activo})"
