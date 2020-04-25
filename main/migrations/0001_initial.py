# Generated by Django 2.1.15 on 2020-04-25 02:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('correlativo', models.CharField(max_length=50)),
                ('hora_ingreso', models.DateTimeField(auto_now_add=True)),
                ('tiempo_estimado', models.SmallIntegerField()),
                ('hora_salida', models.DateTimeField()),
                ('borrado', models.NullBooleanField(default=False)),
                ('estado', models.CharField(default='Abierto', max_length=50)),
                ('tipo', models.CharField(max_length=50)),
                ('visitado', models.CharField(max_length=100)),
                ('direccion', models.TextField(max_length=200)),
                ('num_placa', models.CharField(max_length=50)),
                ('num_personas', models.SmallIntegerField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, null=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, null=True)),
                ('creador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('modificador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='modifica_entrada', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Entrada',
                'verbose_name_plural': 'Entradas',
                'db_table': 'entrada',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('identificacion', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
                'db_table': '',
                'managed': True,
            },
        ),
    ]