# Generated by Django 2.0.7 on 2018-08-01 03:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DeterminacionForm', '0013_auto_20180801_0322'),
        ('responsablesInformacion', '0003_auto_20180731_2106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personal',
            name='Cargo',
        ),
        migrations.RemoveField(
            model_name='personal',
            name='Unidad',
        ),
        migrations.DeleteModel(
            name='cargo',
        ),
        migrations.DeleteModel(
            name='personal',
        ),
        migrations.DeleteModel(
            name='unidad',
        ),
    ]