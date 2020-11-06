from datetime import datetime

from django.db import models


class Order(models.Model):
    """Orders table"""
    number = models.IntegerField()
    created_date = models.DateTimeField(default=datetime.now)

    def __repr__(self):
        return f"Order #{self.number}"


class OrderItem(models.Model):
    """Order items table"""
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_item")
    product_name = models.CharField(max_length=256)
    product_price = models.DecimalField(max_digits=7, decimal_places=2)
    amount = models.IntegerField()

    def __repr__(self):
        return f"Product - {self.product_name}, order - #{self.order.number}, id - {self.pk}"
