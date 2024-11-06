from django.db import models
from category.models import Category  # Import the Category model

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, default=1) 
    image = models.ImageField(upload_to='products/media/product_images/', null=True, blank=True)

    def __str__(self):
        return self.name
