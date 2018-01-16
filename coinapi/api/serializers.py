from rest_framework import serializers
from coinapi.models import Candle , Price

class CandleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candle
        fields = ('id',
                  'date',
                  'ticker',
                  'hi',
                  'lo',
                  'op',
                  'cl',
                  'vol',
                  'trp',
                  'mp',)

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ('id',
                  'date',
                  'ticker',
                  'price',
                  'vol',
                  'prev_price',
                  'change',
                  'ch_price',
                  'AB',)
