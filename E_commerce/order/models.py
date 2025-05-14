from django.db import models
from django.contrib.auth.models import User
from base.models import Product

# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    purchased = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.quantity} X {self.item}"
    
    def get_total(self):
        total = self.item.selling_price * self.quantity
        float_total = format(total, '0.2f')
        return float_total
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    orderitems = models.ManyToManyField(Cart)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    paymentId = models.CharField(max_length=100, blank=True)
    orderId = models.CharField(max_length=100, blank=True)
    orderId = models.CharField(max_length=100, blank=True)

    def get_totals(self):
        total = 0
        for order_item in self.orderitems.all():
            total += float(order_item.get_total())
        return total
