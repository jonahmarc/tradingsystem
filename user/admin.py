from django.contrib import admin

from .models import User, Stock, OrderReceipt, MyStock

admin.site.register(User)
admin.site.register(Stock)
admin.site.register(OrderReceipt)
admin.site.register(MyStock)