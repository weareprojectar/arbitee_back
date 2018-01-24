from rest_framework import serializers
from stockapi.models import (
                Ticker,
                STOCKINFO,
                OHLCV,
                )

class TickerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticker
        fields = ('id',
                'name',
                'code',
                'sector',
                'market_type',)


class STOCKINFOSerializer(serializers.ModelSerializer):
    class Meta:
        model = STOCKINFO
        fields = ('id',
                'name',
                'code',
                'date',
                'market_type',
                'price',
                'volume',
                )


class OHLCVSerializer(serializers.ModelSerializer):
    class Meta:
        model = OHLCV
        fields = ('id',
                'date',
                'name',
                'code',
                'market_type',
                'open_price',
                'close_price',
                'high_price',
                'low_price',
                'volume',
                )
