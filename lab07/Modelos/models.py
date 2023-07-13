from django.db import models

# Create your models here.

class Simple(models.Model):
    text = models.CharField(max_length=10)
    number = models.IntegerField(null=True)
    url = models.URLField(default='www.example.com')
    def __str__ (self) :
        return self.url
    
class DateExamp1e(models.Model):
    the_date = models.DateTimeField()

class NullExamp1e(models.Model):
    col = models.CharField(max_length=10, blank=True, null=True)

"""relacion de uno a muchos en ete caso el que va ser
relacionado con varios es el modelo lenguaje"""

class Lenguage(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class Framework(models.Model):
    name = models.CharField(max_length=10)
    lenguage = models.ForeignKey(Lenguage, on_delete=models.CASCADE)
    def __str__(self):
        return self.name 


