from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('products/', views.product_list, name='product_list'),
    path('products/new/', views.product_create, name='product_create'),
    path('products/<int:pk>/edit/', views.product_update, name='product_update'),
    path('animals/', views.animal_list, name='animal_list'),
    path('animals/new/', views.animal_create, name='animal_create'),
    path('animals/<int:pk>/edit/', views.animal_update, name='animal_update'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]