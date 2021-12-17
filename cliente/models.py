from django.db import models

# Create your models here.


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    dni = models.CharField(max_length=8, unique=True)
    direccion = models.CharField(max_length=50, verbose_name="dirección")
    correo = models.EmailField(null=True, blank=True, verbose_name="email")
    telefono = models.CharField(
        max_length=10,
        null=True, blank=True,
        verbose_name="tel"
    )
    created = models.DateTimeField('create at', auto_now_add=True)
    modified = models.DateTimeField('modified at', auto_now=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['-created', '-modified']

    def __str__(self):
        return '{} {}'.format(self.nombre, self.dni)
