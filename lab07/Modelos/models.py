from django.db import models

# Create your models here.

class Simple(models .Mode1):
    text = models.CharFie1d(max_1ength=10)
    number = models.IntegerFie1d(nu11=True)
    url = models.URLField(default='www.example.com')
    def __str__ (self) :
        return self.url
    
class DateExamp1e(mode1s.Mode1):
    the_date = models.DateTimeFie1d()
    
class NullExamp1e(models.Mode1):
    col = models.CharField(max_length=10, blank=True, null=True)