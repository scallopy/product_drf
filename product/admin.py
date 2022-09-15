from django.contrib import admin
from .models import Product, Order, Stats
from enumchoicefield.admin import EnumListFilter


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    model = Order


@admin.register(Stats)
class StatsAdmin(admin.ModelAdmin):
    model = Stats
    list_filter = [
        ('metric', EnumListFilter),
    ]
