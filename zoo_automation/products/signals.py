from django.db.models.signals import post_save
from django.dispatch import receiver
from sales.models import SaleItem
from supplies.models import SupplyItem

@receiver(post_save, sender=SupplyItem)
def update_product_stock_on_supply(sender, instance, **kwargs):
    product = instance.product
    product.stock += instance.quantity
    product.save()

@receiver(post_save, sender=SaleItem)
def update_stock_on_sale(sender, instance, **kwargs):
    if instance.product:
        instance.product.stock -= instance.quantity
        instance.product.save()
    elif instance.animal:
        instance.animal.is_available = False
        instance.animal.save()