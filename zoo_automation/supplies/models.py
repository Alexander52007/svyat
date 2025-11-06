# supplies/models.py
from django.db import models
from products.models import Product

class Supply(models.Model):
    date = models.DateField()
    supplier = models.CharField(max_length=200)

    def __str__(self):
        return f"Поставка от {self.supplier} ({self.date})"

class SupplyItem(models.Model):
    supply = models.ForeignKey(Supply, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product} x{self.quantity}"