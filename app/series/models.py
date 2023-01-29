from django.db import models
from django.db.models import CASCADE

# Create your models here.
class Serie(models.Model):
    title = models.CharField(max_length=100)
    descripcion = models.TextField()
    
    #Para mostrar el modelo en admin
    def __str__(self):
        return self.title


class Episodie(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=100)
    serie = models.ForeignKey(Serie, on_delete=CASCADE)
    
    #Para mostrar el modelo en admin
    def __str__(self):
        return f'{self.name} - {self.number}'
