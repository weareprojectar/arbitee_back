from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from coinapi.models import Candle, Price
from coinapi.api.serializers import CandleSerializer, PriceSerializer
from utils.paginations import StandardResultPagination

class PriceAPIView(generics.ListCreateAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
    pagination_class = StandardResultPagination
    filter_backends = [SearchFilter, OrderingFilter]

    def get_queryset(self, *args, **kwargs):
        queryset = Price.objects.all().order_by('id')
        date_by = self.request.GET.get('date')
        ticker_by = self.request.GET.get('ticker')
        if date_by and ticker_by:
            queryset_list = queryset.filter(date=date_by).filter(tikcer=ticker_by)
            return queryset_list
        if date_by and not ticker_by:
            queryset_list = queryset.filter(date=date_by)
            return queryset_list
        if ticker_by and not date_by:
            queryset_list = queryset.filter(ticker=ticker_by)
            return queryset_list
        return queryset

class PriceDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


class CandleAPIView(generics.ListCreateAPIView):
    queryset = Candle.objects.all()
    serializer_class = CandleSerializer
    pagination_class = StandardResultPagination
    filter_backends = [SearchFilter, OrderingFilter]

    def get_queryset(self, *args, **kwargs):
        queryset = Candle.objects.all().order_by('id')
        date_by = self.request.GET.get('date')
        ticker_by = self.request.GET.get('ticker')
        if date_by and ticker_by:
            queryset_list = queryset.filter(date=date_by).filter(ticker=ticker_by)
            return queryset_list
        if date_by and not ticker_by:
            queryset_list = queryset.filter(date=date_by)
            return queryset_list
        if ticker_by and not date_by:
            queryset_list = queryset.filter(ticker=ticker_by)
            return queryset_list
        return queryset


class CandleDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Candle.objects.all()
    serializer_class = CandleSerializer
