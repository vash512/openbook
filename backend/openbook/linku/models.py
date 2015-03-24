# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    usuario = models.ForeignKey(User, verbose_name = "Propiedad")
    nombre = models.CharField( max_length=255)
    correo = models.EmailField()
    direccion = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    def __unicode__(self):
        return "%s - %s"%(self.usuario.username, self.nombre)
    class Meta:
       unique_together = (("usuario", "nombre"), ("correo", "usuario"))

class Telefono(models.Model):
    cliente = models.ForeignKey(Cliente)
    telefono = models.CharField(max_length=20)
    descripcion = models.CharField(blank=True, null=True, max_length=100)
    def __unicode__(self):
        return "%s - %s"%(self.cliente, self.telefono)
    class Meta:
       unique_together = ("cliente", "telefono")
    
class GrupoCliente(models.Model):
    usuario = models.ForeignKey(User)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    cliente = models.ManyToManyField(Cliente)
    class Meta:
        verbose_name = "Grupo de Cliente"
        verbose_name_plural = "Grupos de Clientes"
    def __unicode__(self):
        return self.nombre
    