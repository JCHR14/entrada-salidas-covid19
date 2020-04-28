from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Entrada(models.Model):
    id = models.AutoField(primary_key=True)
    correlativo = models.CharField(max_length=50)
    hora_ingreso = models.DateTimeField(auto_now_add=True)
    tiempo_estimado = models.SmallIntegerField()
    hora_salida = models.DateTimeField(blank=True, null=True)
    borrado = models.NullBooleanField(default = False)
    estado = models.CharField(max_length=50, default='Abierta')  # Abierto o cerrado
    tipo = models.CharField(max_length=50) #Visita o repartidor
    visitado = models.CharField(max_length=100)
    direccion = models.TextField(max_length=200)
    num_placa = models.CharField(max_length=50)
    num_personas = models.SmallIntegerField()
    repartidor = models.ForeignKey(
        'Repartidor', models.DO_NOTHING, blank=True, null=True)
    creador = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    modificador = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='modifica_entrada')
    fecha_creacion = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True, auto_now=True)

    @property
    def personas(self):
        listado = list(Persona.objects.filter(
            entrada=self.pk).values('nombre', 'identificacion'))
        data = ''
        for x in listado:
            data += '{} ({}) |  '.format(x['nombre'], x['identificacion'])
        return data

    def __str__(self):
        return '{}'.format(self.correlativo)
    class Meta:
        db_table = 'entrada'
        managed = True
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'

class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    nombre  = models.CharField(max_length=100)
    identificacion = models.CharField(max_length=50)
    entrada = models.ForeignKey(
        Entrada, models.DO_NOTHING, blank=True, null=True)
    def __str__(self):
        return '{}'.format(self.nombre)
    class Meta:
        db_table = 'persona'
        managed = True
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

class Repartidor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre  = models.CharField(max_length=100)
    def __str__(self):
        return '{}'.format(self.nombre)
    class Meta:
        db_table = 'repartidor'
        managed = True
        verbose_name = 'Repartidor'
        verbose_name_plural = 'Repartidores'
