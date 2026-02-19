from django.db import models

# Create your models here.
class Contactos(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    birthdate = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    fijado = models.BooleanField(default=False)
    fijado_orden = models.PositiveIntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre