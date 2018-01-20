from django.db import models

# Create your models here.
class Candle(models.Model):
    date = models.BigIntegerField()
    ticker = models.CharField(max_length=30)
    high_price = models.IntegerField()
    low_price = models.IntegerField()
    open_price = models.IntegerField()
    close_price = models.IntegerField()
    volume = models.FloatField()
    trade_price = models.IntegerField(blank=True)
    mean_price = models.IntegerField(blank =True)

    def __str__(self):
        return self.ticker

class Price(models.Model):
    date = models.CharField(max_length=30)
    ticker = models.CharField(max_length=20)
    price = models.FloatField()                 #tradePrice
    vol = models.FloatField()                   #volume
    prev_price = models.IntegerField()          #prevClosingPrice
    change = models.CharField(max_length=10)    #FALL or RISE
    ch_price = models.IntegerField()            #Change Price From prev_price
    AB = models.CharField(max_length=10)

    def __str__(self):
        return self.ticker


class MM(models.Model):
    ticker = models.CharField(max_length=20)
    start = models.BigIntegerField()
    end = models.BigIntegerField()
    mm_num = models.IntegerField()

    def __str__(self):
        return self.ticker
