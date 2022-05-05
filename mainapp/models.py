from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f'{self.id}: {self.name}'


class Product(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to="products_imgs")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=1)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    quantity = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f'{self.id}: {self.name}'