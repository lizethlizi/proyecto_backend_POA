# Generated by Django 2.0.7 on 2018-07-31 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DeterminacionForm', '0009_datosformulario_formularios_objetivos_gestion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formularios',
            name='Cargo',
        ),
        migrations.RemoveField(
            model_name='formularios',
            name='ResponsableInformacion',
        ),
    ]