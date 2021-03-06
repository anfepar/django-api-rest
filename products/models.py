from django.db import models

# Create your models here.
class Size(models.Model):
    name= models.CharField(
        max_length=20
    )

    def __str__(self):
        return self.name

class Color(models.Model):
    name= models.CharField(
        max_length=20
    )
    ref = models.CharField(
        max_length = 7
    )

    def __str__(self):
        return self.name

class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(
        max_length=20
    )

    icon = models.CharField(
        max_length=20
    )

    def __str__(self):
        return self.name

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
    category = models.ForeignKey( Category, on_delete=models.CASCADE)

    sizes = models.ManyToManyField(Size, blank =True)
    colors = models.ManyToManyField(Color, blank =True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.name


