from django.contrib import admin
from .models import Brand, Category, Products  # , ProductVariance, ProductVarianceAttribute

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Products)