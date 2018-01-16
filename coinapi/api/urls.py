from django.urls import path,include
from coinapi.api.views import (
    CandleAPIView,
    PriceAPIView,
    PriceDetailAPIView,
    CandleDetailAPIView,
    )
# from coinapi.api.views import Candle, Price
# from coinapi.api.serializers import CandleSerializer, PriceSerializer

app_name = 'coin-api'
urlpatterns = [
    path('upbitchart/', CandleAPIView.as_view(), name = 'upbit-chart'),
    path('upbitprice/', PriceAPIView.as_view(), name='upbit-price'),
    path('upbitchart/<int:pk>/', CandleDetailAPIView.as_view(), name = 'upbit-chart-detail'),
    path('upbitprice/<int:pk>/', PriceDetailAPIView.as_view(), name='upbit-price-detail'),
]
