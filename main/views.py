# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from django.shortcuts import render, redirect, get_object_or_404
#from django.urls import reverse
from django.db.models import Q
from django.contrib.auth.decorators import login_required, permission_required
from django.db import transaction
from django.contrib.auth.models import User, Group
from django.views.decorators.csrf import csrf_exempt
from .models import *
import datetime
from django.contrib import messages
from entradas_salidas.utils import *

def redirectLogin(request):
	if request.user.id:
	    return redirect('entradas')
	return redirect('login')

@login_required()
@csrf_exempt
@transaction.atomic
def entradas(request):
    if request.POST:
        with transaction.atomic():
            try:
                today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
                today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
                num = len(Entrada.objects.filter(fecha_creacion__range=(today_min, today_max))) + 1

                ent = Entrada()
                ent.correlativo = '{}-{}'.format(str(datetime.date.today()), num)
                ent.tiempo_estimado = request.POST.get('tiempoEstimado')
                ent.tipo =  request.POST.get('tipo')
                ent.visitado = request.POST.get('nombreVisitado')
                ent.direccion = request.POST.get('direccion')
                ent.num_placa = request.POST.get('placaVehiculo')
                ent.num_personas = request.POST.get('numPersonas')
                ent.creador = request.user
                ent.modificador = request.user
                ent.save() 

                counter = 0
                iden = request.POST.getlist('identificacion[]', [])
                for x in request.POST.getlist('nombreVisitante[]', []):
                    per = Persona.objects.create(
                        nombre = x,
                        identificacion = iden[counter],
                        entrada = ent
                    )
                    counter += counter
                messages.success(
                    request, 'Entrada registrada con éxito.')
                ctx = {
                    'entrada': ent,
                    'status': True
                }
            except Exception as e:
                messages.error(
                    request, 'No se pudo realizar el ingreso, error:{}'.format(e))
                ctx = {'status':False}
            return render(request, 'entradas.html', ctx)
    ctx ={
        'status':False
    }
    return render(request, 'entradas.html', ctx)

@login_required()
@csrf_exempt
@transaction.atomic
def salidas(request):
    if request.POST:
        Entrada.objects.filter(pk = request.POST.get('codigo')).update(
            hora_salida = datetime.datetime.now(),
            estado = 'Finalizada',
            modificador = request.user
        )
    #Persona.objects.all().delete()
    #Entrada.objects.all().delete()
    search = request.GET.get('search', '')
    page = request.GET.get('page', 1 )
    data = Entrada.objects.filter(
        Q(correlativo__icontains=search) | Q(creador__username__icontains=search) | Q(
            hora_ingreso__icontains=search) | Q(visitado__icontains=search) | Q(direccion__icontains=search) | Q(num_placa__icontains=search)
    ).order_by('-hora_ingreso', 'estado')

    pagination = setInfoPagination(data, page, 10)

    ctx = {
        'listado': pagination['data'],
        'page_range': pagination['page_range'],
        'totaldatos': pagination['totaldatos'],
        'search': search,
        'page': page
    }

    return render(request, 'salidas.html', ctx)
