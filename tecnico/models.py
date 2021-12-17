from django.db import models
from cliente.models import Cliente

# Create your models here.


class Tecnico(models.Model):
    fecha = models.DateField()
    cliente = models.ForeignKey(
        Cliente, null=False, blank=False, on_delete=models.CASCADE)
    producto = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    color = models.CharField(max_length=30)
    serie = models.CharField(max_length=50, verbose_name="número de serie")
    extra = models.CharField(
        max_length=80,
        null=True,
        blank=True,
        verbose_name="accesorios incluidos"
    )
    usuario = models.CharField(max_length=50, null=True, blank=True)
    contrasena = models.CharField(max_length=50, null=True, blank=True)
    estado = models.TextField()

    fechaen = models.DateField(
        null=True, blank=True,
        verbose_name="fecha de entrega"
    )
    diagnostico = models.TextField(null=True, blank=True)
    realizar = models.TextField(
        null=True,
        blank=True,
        verbose_name="proceso realizado"
    )
    observacion = models.TextField(null=True, blank=True)
    precio = models.FloatField(null=True, blank=True)
    entrega = models.NullBooleanField()

    created = models.DateTimeField('create at', auto_now_add=True)
    modified = models.DateTimeField('modified at', auto_now=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['-created', '-modified']
