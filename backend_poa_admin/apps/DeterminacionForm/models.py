from django.db import models
from ..responsablesInformacion.models import personal
from ..responsablesInformacion.models import cargo
# Create your models here.
class Datosformulario(models.Model):
    sigla=models.CharField(max_length=10)
    codigo=models.IntegerField()
    nombre_entidad=models.CharField(max_length=100)
    def __str__(self):
        return str(self.pk)
    class Meta:
        verbose_name_plural = ("Datosformulario")

#formularios
class formularios(models.Model):
    Gestion = models.IntegerField()
    Fecha=models.DateField()
    ResponsableInformacion=models.ForeignKey(personal,on_delete=models.CASCADE)
    Cargo=models.ForeignKey(cargo,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.pk)
    class Meta:
        verbose_name_plural = ("Lista de Formularios")
    
    def examenes_solicitados(self):
        return ", ".join([p.descripcion for p in self.ordenExamen.all()])

    def __unicode__(self):
        return self.fechaEmision

#formulario de objetivos de gestion
class objetivos_gestion(models.Model):
    Descripcion = models.CharField(max_length=500)
    Resultados = models.CharField(max_length=500)
    BENEFICIARIOS_CHOICES= (
    ('Estudiantes Afiliados', 'Estudiantes Afiliados'),
    ('Estudiantes en General', 'Estudiantes en General'),
    )
    Beneficiarios = models.CharField(max_length=30, choices=BENEFICIARIOS_CHOICES, default='Beneficiarios')
    Formularios=models.ForeignKey(formularios,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.pk)
    class Meta:
        verbose_name_plural = ("Objetivos de Gestion")

#descripcion del los objetivos
# class descripcion(models.Model):
#     descripcion = models.CharField(max_length=500)
#     objetivos_gestion=models.ForeignKey(objetivos_gestion,on_delete=models.CASCADE)

#     def __str__(self):
#         return str(self.pk)
#     class Meta:
#         verbose_name_plural = ("Descripcion")

#ElaboradoPorSSU
# class ElaboradoPorSSU(models.Model):
#     descripcion = models.CharField(max_length=500)
#     objetivos_gestion=models.ForeignKey(objetivos_gestion,on_delete=models.CASCADE)

#     def __str__(self):
#         return str(self.pk)
#     class Meta:
#         verbose_name_plural = ("Descripcion")