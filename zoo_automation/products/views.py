from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Product, Animal, Category
from .forms import ProductForm, AnimalForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from sales.models import Sale
@login_required
def index(request):
    total_products = Product.objects.count()
    available_animals = Animal.objects.filter(is_available=True).count()
    total_sales = Sale.objects.count()
    low_stock_items = Product.objects.filter(stock__lt=5, stock__gt=0)
    low_stock_count = low_stock_items.count()
    recent_sales = Sale.objects.select_related().prefetch_related('items__product', 'items__animal').order_by('-date')[:5]

    context = {
        'total_products': total_products,
        'available_animals': available_animals,
        'total_sales': total_sales,
        'low_stock_count': low_stock_count,
        'low_stock_items': low_stock_items,
        'recent_sales': recent_sales,
    }
    return render(request, 'index.html', context)
@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})
@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Товар успешно добавлен!')
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/product_form.html', {'form': form, 'title': 'Добавить товар'})
@login_required
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Товар обновлён!')
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/product_form.html', {'form': form, 'title': 'Редактировать товар'})
@login_required
def animal_list(request):
    animals = Animal.objects.filter(is_available=True)
    return render(request, 'animals/animal_list.html', {'animals': animals})
@login_required
def animal_create(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Животное добавлено в каталог!')
            return redirect('animal_list')
    else:
        form = AnimalForm()
    return render(request, 'animals/animal_form.html', {'form': form, 'title': 'Добавить животное'})
@login_required
def animal_update(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES, instance=animal)
        if form.is_valid():
            form.save()
            messages.success(request, 'Карточка животного обновлена!')
            return redirect('animal_list')
    else:
        form = AnimalForm(instance=animal)
    return render(request, 'animals/animal_form.html', {'form': form, 'title': 'Редактировать животное'})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 != password2:
            messages.error(request, 'Пароли не совпадают!')
            return render(request, 'register.html')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Пользователь с таким именем уже существует!')
            return render(request, 'register.html')
        user = User.objects.create_user(username=username, password=password1)
        user.save()
        login(request, user)
        messages.success(request, f'Добро пожаловать, {username}!')
        return redirect('index')
    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'С возвращением, {username}!')
                return redirect('index')
            else:
                messages.error(request, 'Неверное имя пользователя или пароль.')
        else:
            messages.error(request, 'Неверное имя пользователя или пароль.')
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.info(request, 'Вы вышли из системы.')
    return redirect('login')