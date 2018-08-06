from django.db import models

# Create your models here.
#unidad
class unidad(models.Model):
    nombre_unidad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_unidad
    class Meta:
        verbose_name_plural = ("Unidad")
#cargo
class cargo(models.Model):
    descripcion = models.CharField(max_length=50)
    
    def __str__(self):
        return self.descripcion
    
    class Meta:
        verbose_name_plural = ("Cargo")    
#Personal
class personal(models.Model):
    Nombre = models.CharField(max_length=50)
    Apellidos = models.CharField(max_length=100)
    Ci=models.IntegerField()
    Tipo_personal = models.CharField(max_length=30)
    Nro_item=models.IntegerField()
    Responsable=models.BooleanField(default=False)
    Unidad=models.ForeignKey(unidad,on_delete=models.CASCADE)
    Cargo=models.ForeignKey(cargo,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.Ci)
    class Meta:
        verbose_name_plural = ("Personal")
    
    
    
    
