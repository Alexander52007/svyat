from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name


class Animal(models.Model):
    SPECIES_CHOICES = [
        ('cat', 'Кошка'),
        ('dog', 'Собака'),
        ('bird', 'Птица'),
        ('fish', 'Рыбка'),
        ('rodent', 'Грызун'),
    ]
    GENDER_CHOICES = [('M', 'Самец'), ('F', 'Самка')]

    species = models.CharField(max_length=20, choices=SPECIES_CHOICES)
    breed = models.CharField(max_length=100, blank=True)
    age_months = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='animals/', blank=True, null=True)

    def __str__(self):
        return f"{self.get_species_display()} ({self.breed or 'без породы'})"