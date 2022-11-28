from rest_framework.decorators import api_view
from rest_framework.response import Response
from user.models import Stock, OrderReceipt, MyStock, User
from .serializers import StockSerializer, MyStockSerializer, OrderHistorySerializer, StockDataSerializer
from user.api import serializers
from django.db.models import F

@api_view(['GET'])
def getStocks(request):
    stocks = Stock.objects.all()
    data = StockSerializer(stocks, many=True)
    return Response(data.data)


@api_view(['GET'])
def getMyStock(request):
    stocks = MyStock.objects.filter(user__username=request.user)
    data = MyStockSerializer(stocks, many=True)
    return Response(data.data)


@api_view(['GET'])
def getPurchaseStockHistory(request):
    purchases = OrderReceipt.objects.filter(user__username=request.user, order_type='BUY')
    data = OrderHistorySerializer(purchases, many=True)
    return Response(data.data)


@api_view(['GET'])
def getStockData(request, stock_name):
    stock_data = Stock.objects.get(name=stock_name)
    history = stock_data.history.all().values()
    data = StockDataSerializer(history, many=True)
    return Response(data.data)