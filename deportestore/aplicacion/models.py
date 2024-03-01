from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Productos(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return f"{self.nombre}"
    

class Medios_pago(models.Model):
    nombre = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = "Medio_pago"
        verbose_name_plural = "Medios_pagos"
    
    def __str__(self):
        return f"{self.nombre}"
     

class Sucursales(models.Model):
    ciudad = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Sucursal"
        verbose_name_plural = "Sucursales"
        ordering = ['ciudad']
    def __str__(self):
        return f"{self.ciudad}"
    
class Preguntas_frecuentes(models.Model):
    consulta = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = "Consulta"
        verbose_name_plural = "Consultas"
    
    def __str__(self):
        return f"{self.consulta}"

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"        