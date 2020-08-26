from django.db import models
from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(
        max_length=50
    )
    price = models.DecimalField(
        max_digits=50, decimal_places=10
    )
    picture = models.ImageField(
        upload_to="pictures/products", blank= True, null= True
    )
    category = models.CharField(
        max_length=50
    )
    description = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.name