from django.contrib import admin
from .models import User, Product, Order, OrderDetail

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = ('uid', 'name', 'username', 'email', 'type')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ('pid', 'name', 'category', 'price', 'stock')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'status', 'order_date', 'total_amount')

@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
	list_display = ('id', 'order', 'product', 'quantity', 'price_at_purchase')
