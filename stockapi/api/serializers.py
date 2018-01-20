from rest_framework import serializers
from stockapi.models import Ticker, OHLCV

class TickerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticker
        fields = ('id',
                'name',
                'code',
                'sector',
                'market_type',)

class OHLCVSerializer(serializers.ModelSerializer):
    class Meta:
        model = OHLCV
        fields = ('id',
                'name',
                'code',
                'open_price',
                'close_price',
                'high_price',
                'low_price',
                'volume',
                )
