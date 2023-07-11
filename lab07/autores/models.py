from django.db import models

# Create your models here.

class Autores(models.Model):
    nombre = models.CharField(max_length=30)
    biografia = models.TextField
    