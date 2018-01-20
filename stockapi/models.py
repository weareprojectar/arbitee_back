from django.db import models

# Create your models here.
class Ticker(models.Model):
    date = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=6)
    sector = models.CharField(max_length=15)
    market_type = models.CharField(max_length=10)

    def __str__(self):
        return '{} {}'.format(self.code, self.name)

class OHLCV(models.Model):
    code = models.CharField(max_length=6)
    name = models.CharField(max_length=50)
    date = models.CharField(max_length=16)
    open_price = models.FloatField()
    high_price = models.FloatField()
    low_price = models.FloatField()
    close_price = models.FloatField()
    volume = models.IntegerField()

    def __str__(self):
        return '{} {}'.format(self.code, self.name)
