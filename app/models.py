from django.db import models


class Cobertura(models.Model):

    color = models.CharField(blank=True, null=True, max_length=100)
    location = models.GeometryField(blank=False, null=False)

    def __str__(self):
        return f"Cobertura {self.pk}"

    class Meta:
        db_table = "address"
        order_with_respect_to = "address"


class Plan(models.Model):

    nombre =  models.TextField()

    def __str__(self):
        return f"Plan {self.nombre}"


