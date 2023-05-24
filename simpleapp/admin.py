from django.contrib import admin
from .models import Category, Product, NewsCategory, NewsPortal

admin.site.register(Category)
admin.site.register(Product)

# Register your models here.
# Приложение с новостями
admin.site.register(NewsCategory)
admin.site.register(NewsPortal)
