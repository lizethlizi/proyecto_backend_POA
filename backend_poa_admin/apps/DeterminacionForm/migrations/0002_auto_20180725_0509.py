# Generated by Django 2.0.7 on 2018-07-25 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DeterminacionForm', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Datosformulario',
        ),
        migrations.RemoveField(
            model_name='descripcion',
            name='objetivos_gestion',
        ),
        migrations.RemoveField(
            model_name='objetivos_gestion',
            name='responsableInformacion',
        ),
        migrations.DeleteModel(
            name='descripcion',
        ),
        migrations.DeleteModel(
            name='objetivos_gestion',
        ),
    ]
