from django.db import models

# Create your models here.
class Stocks(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    date = models.DateField(blank=False)
    price = models.DecimalField(default=False, max_digits=20,decimal_places=2)

class cryptoCurrencies(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    date = models.DateField(blank=False)
    price = models.DecimalField(default=False, max_digits=20,decimal_places=2)
    symbol = models.CharField(max_length=5, blank=False, default='')
    marketCap = models.DecimalField(default=False, max_digits=20,decimal_places=2)
    circulatingSuply =  models.DecimalField(default=False, max_digits=20,decimal_places=2)