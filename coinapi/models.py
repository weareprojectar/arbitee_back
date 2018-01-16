from django.db import models

# Create your models here.
class Candle(models.Model):
    date = models.CharField(max_length=30)
    ticker = models.CharField(max_length=30)
    hi = models.IntegerField()
    lo = models.IntegerField()
    op = models.IntegerField()
    cl = models.IntegerField()
    vol = models.IntegerField()
    trp = models.IntegerField(blank=True)
    mp = models.IntegerField(blank =True)

    def __str__(self):
        return self.ticker + self.date

class Price(models.Model):
    date = models.CharField(max_length=30)
    ticker = models.CharField(max_length=20)
    price = models.IntegerField()               #tradePrice
    vol = models.FloatField()                   #volume
    prev_price = models.IntegerField()          #prevClosingPrice
    change = models.CharField(max_length=10)    #FALL or RISE
    ch_price = models.IntegerField()            #Change Price From prev_price
    AB = models.CharField(max_length=10)

    def __str__(self):
        return self.ticker
