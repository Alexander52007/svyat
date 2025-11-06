from django.shortcuts import render, redirect
from django.db import transaction
from .models import Sale, SaleItem
from products.models import Product, Animal
from django.contrib.auth.decorators import login_required

@login_required
def sale_list(request):
    sales = Sale.objects.all().order_by('-date')
    return render(request, 'sales/sale_list.html', {'sales': sales})
@login_required
def sale_create(request):
    if request.method == 'POST':
        with transaction.atomic():
            sale = Sale.objects.create(total_amount=0)
            total = 0

            product_ids = request.POST.getlist('product_id')
            quantities = request.POST.getlist('quantity')
            for pid, qty in zip(product_ids, quantities):
                if not pid or not qty:
                    continue
                qty = int(qty)
                if qty <= 0:
                    continue
                product = Product.objects.get(id=pid)
                item_price = product.price * qty
                SaleItem.objects.create(
                    sale=sale,
                    product=product,
                    quantity=qty,
                    price_at_sale=product.price
                )
                total += item_price

            animal_ids = request.POST.getlist('animal_id')
            for aid in animal_ids:
                if not aid:
                    continue
                animal = Animal.objects.get(id=aid)
                if not animal.is_available:
                    continue
                SaleItem.objects.create(
                    sale=sale,
                    animal=animal,
                    quantity=1,
                    price_at_sale=animal.price
                )
                total += animal.price

            sale.total_amount = total
            sale.save()

        return redirect('sale_list')

    products = Product.objects.filter(stock__gt=0)
    animals = Animal.objects.filter(is_available=True)
    return render(request, 'sales/sale_create.html', {
        'products': products,
        'animals': animals
    })