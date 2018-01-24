from django.db import models

# Create your models here.

# stock Ticker
class Ticker(models.Model):
    date = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=6)
    sector = models.CharField(max_length=15)
    market_type = models.CharField(max_length=10)

    def __str__(self):
        return '{} {}'.format(self.code, self.name)


# on time stock price data(9-16)
class STOCKINFO(models.Model):
    date=models.CharField(max_length=15)
    name=models.CharField(max_length=50)
    code=models.CharField(max_length=6)
    market_type=models.CharField(max_length=10)
    price = models.FloatField()
    volume = models.IntegerField()

    def __str__(self):
        return '{} {}'.format(self.date, self.name)

# daily market OHLCV data(at 16 O`Clock)
class OHLCV(models.Model):
    code = models.CharField(max_length=6)
    name = models.CharField(max_length=50)
    date = models.CharField(max_length=16)
    market_type=models.CharField(max_length=10)
    open_price = models.FloatField()
    high_price = models.FloatField()
    low_price = models.FloatField()
    close_price = models.FloatField()
    volume = models.IntegerField()

    def __str__(self):
        return '{} {}'.format(self.code, self.name)
