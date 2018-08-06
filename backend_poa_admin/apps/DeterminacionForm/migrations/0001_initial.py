# Generated by Django 2.0.7 on 2018-07-09 04:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('responsablesInformacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Datosformulario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', models.CharField(max_length=10)),
                ('codigo', models.IntegerField()),
                ('nombre_entidad', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Datosformulario',
            },
        ),
        migrations.CreateModel(
            name='descripcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Descripcion',
            },
        ),
        migrations.CreateModel(
            name='objetivos_gestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gestion', models.IntegerField()),
                ('fecha', models.DateField()),
                ('resultados_esperados', models.CharField(max_length=100)),
                ('beneficiarios', models.CharField(choices=[('EA', 'Estudiantes Afiliados'), ('EG', 'Estudiantes en General')], default='Beneficiarios', max_length=30)),
                ('responsableInformacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='responsablesInformacion.unidad')),
            ],
            options={
                'verbose_name_plural': 'Objetivos de Gestion',
            },
        ),
        migrations.AddField(
            model_name='descripcion',
            name='objetivos_gestion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DeterminacionForm.objetivos_gestion'),
        ),
    ]