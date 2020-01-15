from django.db import models
class Cachorro(models.Model):
    nome = models.CharField(max_length=255)
    idade =models.IntegerField() 
    cor_do_pelo = models.CharField(max_length=255)
    porte = models.CharField(max_length=255)
    dono = models.CharField(max_length=255)
    


# Create your models here.
