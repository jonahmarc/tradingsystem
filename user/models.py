from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from simple_history.models import HistoricalRecords


class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50, blank=True)

    USERNAME_FIELD = 'username'

class Stock(models.Model):
    name = models.CharField(unique=True, max_length=50)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.PositiveIntegerField()
    history = HistoricalRecords()

    REQUIRED_FIELDS = [name, price]


class OrderReceipt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.PositiveIntegerField()
    total = models.DecimalField(max_digits=9, decimal_places=2)
    order_type = models.CharField(max_length=5)
    date_ordered = models.DateTimeField(auto_now_add=True)
    
    REQUIRED_FIELDS = [stock_name, price, quantity, total, order_type]


class MyStock(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, null=True, on_delete=models.SET_NULL)
    purchase_price = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.PositiveIntegerField()