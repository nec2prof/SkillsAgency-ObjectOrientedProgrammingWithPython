from django.db import models

class User(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=128)
    email = models.EmailField()
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    class TypeUser(models.TextChoices):
        NO_USER = "NU", "No User"
        USER = "US", "User"
        ADMIN = "AD", "Administrator"
    type = models.CharField(
        max_length=2,
        choices=TypeUser.choices,
        default=TypeUser.NO_USER,
        verbose_name="User type"
    )

class Product(models.Model):
    pid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    image = models.CharField(max_length=255, blank=True)
    stock = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=30)
    weight = models.FloatField()
    measures = models.CharField(max_length=60)
    score = models.IntegerField(default=0)

class Order(models.Model):
    user = models.ForeignKey(
        User,
        on_delete= models.SET_NULL,
        null=True,
        related_name='orders',
        verbose_name='Customer'
    )
    class OrderStatus(models.TextChoices):
        PENDING = 'PE', 'Pending'
        PROCESSING = 'PR', 'Processing'
        SHIPPED = 'SH', 'Shipped'
        DELIVERED = 'DE', 'Delivered'
        CANCELLED = 'CA', 'Cancelled'
    status = models.CharField(
        max_length=2,
        choices=OrderStatus.choices,
        default=OrderStatus.PENDING,
        verbose_name='Order Status'
    )
    order_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    shipping_address = models.CharField(max_length=255)

class OrderDetail(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='details',
        verbose_name='Order Header'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Product'
    )
    quantity = models.IntegerField()
    price_at_purchase = models.DecimalField(max_digits=10, decimal_places=2)
    sub_total = models.DecimalField(max_digits=10, decimal_places=2)
