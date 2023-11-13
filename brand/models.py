from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField(default="Description")
    image = models.ImageField(upload_to="products", default="products/product.png")


    def __str__(self):
        return self.name




