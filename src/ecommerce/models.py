from django.db import models

# Create your models here.
class ProductModel(models.Model):
    title = models.TextField()
    price = models.FloatField()
    description = models.TextField()
    seller = models.TextField()
    color  = models.TextField()
    Product_dimensions = models.TextField() 