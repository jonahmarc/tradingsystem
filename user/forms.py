from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User, Stock, MyStock


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class StockForm(ModelForm):
    class Meta:
        model = Stock
        fields = '__all__'
        exclude = ['history']


class MyStockForm(ModelForm):
    class Meta:
        model = MyStock
        fields = '__all__'