from rest_framework.serializers import ModelSerializer
from user.models import Stock, MyStock, OrderReceipt


class StockSerializer(ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'

class MyStockSerializer(ModelSerializer):
    stock = StockSerializer(Stock.objects.all(), many=False)

    class Meta:
        model = MyStock
        fields = ['stock', 'quantity', 'purchase_price']


class OrderHistorySerializer(ModelSerializer):
    class Meta:
        model = OrderReceipt
        fields = '__all__'



class StockDataSerializer(ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'