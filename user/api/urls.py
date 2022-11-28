from django.urls import path
from . import apis

urlpatterns = [
    path('stocks/',  apis.getStocks),
    path('mystocks/',  apis.getMyStock),
    path('stocks/purchase/history/', apis.getPurchaseStockHistory),
    path('stock/data/<str:stock_name>/', apis.getStockData)
]