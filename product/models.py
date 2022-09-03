from django.db import models


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
        Product,
        related_name='products',
        blank=True
    )
