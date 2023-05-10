from django.db import models
from datetime import date


class Arts_test(models.Model):
    Id_art = models.AutoField(primary_key=True)
    Referencia = models.CharField(max_length=150)
    Nombre = models.CharField(max_length=150)
    Descripcion = models.CharField(max_length=150)
    Precio = models.IntegerField(default=0)
    tax = models.IntegerField(default=7)
    date = models.DateField(default=date.today)

class Orders(models.Model):
    Id_art = models.AutoField(primary_key=True)
    Referencia = models.CharField(max_length=150)
    Cantidad = models.IntegerField(default=0)
    Precio_T= models.IntegerField(default=0)
    Precio_I= models.IntegerField(default=0)
    date = models.DateField(default=date.today)