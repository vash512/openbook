# -*- coding: utf-8 -*-
from django.db import models
from linku.models import Cliente

class Deuda(models.Model):
    cleinte = models.ForeignKey(Cliente)
    montoOriginal = models.DecimalField(max_digits=9, decimal_places=2)
    descripcion = models.TextField()
    deaudaActual = models.DecimalField(blank=True, null=True, max_digits=9, decimal_places=2)
    def __unicode__(self):
        return "%s - $%s"%(self.cliente, self.deaudaActual)

class Desglose(models.Model):
    deuda = models.ForeignKey(Deuda)
    producto = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=9, decimal_places=2)

