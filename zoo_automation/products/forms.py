from django import forms
from .models import Product, Animal, Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock', 'category', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Выберите категорию...'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['species', 'breed', 'age_months', 'gender', 'price', 'image']
        widgets = {
            'species': forms.Select(attrs={'class': 'form-control'}),
            'breed': forms.TextInput(attrs={'class': 'form-control'}),
            'age_months': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': 0.01}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }