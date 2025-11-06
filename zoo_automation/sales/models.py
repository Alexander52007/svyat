# sales/models.py
from django.db import models
from products.models import Product, Animal

class Sale(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Продажа #{self.id} от {self.date.strftime('%d.%m.%Y')}"

class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL)
    animal = models.ForeignKey(Animal, null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.PositiveIntegerField(default=1)
    price_at_sale = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        item = self.product or self.animal
        return f"{item} x{self.quantity}"