# Generated by Django 2.0.7 on 2018-08-01 03:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DeterminacionForm', '0012_datosformulario_formularios_objetivos_gestion'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Datosformulario',
        ),
        migrations.RemoveField(
            model_name='formularios',
            name='Cargo',
        ),
        migrations.RemoveField(
            model_name='formularios',
            name='ResponsableInformacion',
        ),
        migrations.RemoveField(
            model_name='objetivos_gestion',
            name='Formularios',
        ),
        migrations.DeleteModel(
            name='formularios',
        ),
        migrations.DeleteModel(
            name='objetivos_gestion',
        ),
    ]