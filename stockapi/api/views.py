from rest_framework import generics
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from stockapi.models import Ticker, OHLCV
from stockapi.api.serializers import (
    TickerSerializer,
    OHLCVSerializer,
    )
from utils.paginations import StandardResultPagination


class TickerAPIView(generics.ListCreateAPIView):
    queryset = Ticker.objects.all()
    serializer_class = TickerSerializer
    pagination_class = StandardResultPagination
    filter_backends = [SearchFilter, OrderingFilter]

    def get_queryset(self, *args, **kwargs):
        queryset = Ticker.objects.all().order_by('id')
        date_by = self.request.GET.get('date')
        code_by = self.request.GET.get('code')
        if date_by and code_by:
            queryset_list = queryset.filter(date=date_by).filter(code=code_by)
            return queryset_list
        if date_by and not code_by:
            queryset_list = queryset.filter(date=date_by)
            return queryset_list
        if code_by and not date_by:
            queryset_list = queryset.filter(code=code_by)
            return queryset_list
        return queryset


class TickerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticker.objects.all()
    serializer_class = TickerSerializer


class OHLCVAPIView(generics.ListCreateAPIView):
    queryset = OHLCV.objects.all()
    serializer_class = OHLCVSerializer
    pagination_class = StandardResultPagination
    filter_backends = [SearchFilter, OrderingFilter]

    def get_queryset(self, *args, **kwargs):
        queryset = OHLCV.objects.all().order_by('id')
        date_by = self.request.GET.get('date')
        code_by = self.request.GET.get('code')
        name_by = self.request.GET.get('name')
        if date_by and code_by and name_by:
            queryset_list = queryset.filter(date=date_by).filter(code=code_by).filter(name=name_by)
            return queryset_list
        if date_by and code_by and not name_by:
            queryset_list = queryset.filter(date=date_by).filter(code=code_by)
            return queryset_list
        if date_by and not code_by and name_by:
            queryset_list = queryset.filter(date=date_by).filter(name=name_by)
            return queryset_list
        if date_by and not date_by and not name_by:
            queryset_list = queryset.filter(date=date_by)
            return queryset_list
        if code_by and not date_by and name_by:
            queryset_list = queryset.filter(code=code_by).filter(name=name_by)
            return queryset_list
        if code_by and not date_by and not name_by:
            queryset_list = queryset.filter(code=code_by)
            return queryset_list
        if name_by and not date_by and not code_by :
            queryset_list = queryset.filter(name=name_by)
            return queryset_list
        return queryset


class OHLCVDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OHLCV.objects.all()
    serializer_class = OHLCVSerializer
