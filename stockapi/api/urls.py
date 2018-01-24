from django.urls import path,include
from stockapi.api.views import (
    TickerAPIView,
    OHLCVAPIView,
    STOCKINFOVAPIView
    )

app_name = 'stock-api'
urlpatterns = [
    path('ticker/', TickerAPIView.as_view(), name='ticker'),
    path('stockinfo/', STOCKINFOVAPIView.as_view(), name='info'),
    path('ohlcv/', OHLCVAPIView.as_view(), name='ohlcv'),
]
