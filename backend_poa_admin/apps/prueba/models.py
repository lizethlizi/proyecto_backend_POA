from django.db import models
class objetivo(models.Model):

    # Gestion=models.IntegerField()
    # fecha=models.DateField()
    Descripcion = models.CharField(max_length=500)
    Resultados = models.CharField(max_length=200)
    Beneficiarios = models.CharField(max_length=200)
    
    
    def __str__(self):
        return str(self.pk)
    class Meta:
        verbose_name_plural = ("Objetivo Prueba")