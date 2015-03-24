# -*- coding: utf-8 -*-
from django.db import models
from linku.models import Cliente

from datetime import date

class Deuda(models.Model):
    cliente = models.ForeignKey(Cliente)
    montoOriginal = models.DecimalField(max_digits=9, decimal_places=2)
    descripcion = models.TextField()
    deaudaActual = models.DecimalField(blank=True, null=True, max_digits=9, decimal_places=2)
    individual = models.BooleanField(help_text='los individuales tendran historales de pagos propios mientras que los no individuales tendran un historial de pagos conjunto', default=True)
    fecha = models.DateField(default=date.today)
    def __unicode__(self):
        return "%s - $%s"%(self.cliente, self.deaudaActual)

class Desglose(models.Model):
    deuda = models.ForeignKey(Deuda)
    producto = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=9, decimal_places=2)

class HistorialPago(models.Model):
    deuda = models.ForeignKey(Deuda)
    pago = models.DecimalField(max_digits=9, decimal_places=2)
    fecha = models.DateField(default=date.today)
    notas = models.CharField(blank=True, null=True, max_length=50)
    def __unicode__(self):
        return "%s / %s $%s"%(self.deuda, self.fecha, self.pago)
    