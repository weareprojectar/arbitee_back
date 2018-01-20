from django.urls import path,include
from stockapi.api.views import (
    TickerAPIView,
    TickerDetailAPIView,
    OHLCVAPIView,
    OHLCVDetailAPIView,
    )

app_name = 'stock-api'
urlpatterns = [
    path('ticker/', TickerAPIView.as_view(), name='ticker'),
    path('ticker/<int:pk>', TickerDetailAPIView.as_view(), name='ticker-detail'),
    path('ohlcv/', OHLCVAPIView.as_view(), name='ohlcv'),
    path('ohlcv/<int:pk>', OHLCVDetailAPIView.as_view(), name = 'ohlcv-detail')
]
