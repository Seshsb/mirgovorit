"""
URL configuration for mirgovorit project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('add_product_to_recipe/', views.add_product_to_recipe, name='add_product_to_recipe'),
    path('cook_recipe/', views.cook_recipe, name='cook_recipe'),
    path('show_recipes_without_product/', views.show_recipes_without_product, name='show_recipes_without_product'),
    path('recipe_details/<int:recipe_id>/', views.recipe_details, name='recipe_detail'),
]