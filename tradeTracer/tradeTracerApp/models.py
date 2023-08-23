from django.db import models

# Create your models here.
class Stocks(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    date = models.DateField(blank=False)
    price = models.DecimalField(default=False, max_digits=20,decimal_places=2)

class Crypto_Currencies(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    date = models.DateField(blank=False)
    price = models.DecimalField(default=False, max_digits=20,decimal_places=2)