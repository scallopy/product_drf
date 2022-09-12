from django.db import models
from enum import Enum


class Months(Enum):
    Jan = 1
    Feb = 2
    Mar = 3
    Apr = 4
    May = 5
    Jun = 6
    Jul = 7
    Aug = 8
    Sep = 9
    Oct = 10
    Nov = 11
    Dec = 12


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title


class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(
        Product, related_name='products', blank=True
    )

    def get_order_month(self):
        pass
