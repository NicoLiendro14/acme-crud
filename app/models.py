from django.db import models as models_django
from django.contrib.gis.db import models as models_gis
from django.contrib.auth.models import User


class Direccion(models_django.Model):
    direccion = models_django.CharField(max_length=100)
    ciudad = models_django.CharField(max_length=50)

    def __str__(self):
        return self.direccion


class Cobertura(models_django.Model):
    color = models_django.CharField(blank=True, null=True, max_length=100)
    location = models_gis.GeometryField(blank=False, null=False)

    def __str__(self):
        return f"Cobertura {self.pk}"

    class Meta:
        db_table = "cobertura"  # Corrige el nombre de la tabla


class Plan(models_django.Model):
    nombre = models_django.TextField()
    coberturas = models_django.ManyToManyField(Cobertura)
    direcciones = models_django.ManyToManyField(Direccion)

    def __str__(self):
        return f"Plan {self.nombre}"
