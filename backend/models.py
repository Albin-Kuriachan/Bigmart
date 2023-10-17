from django.db import models


# Create your models here.
class categorydb(models.Model):
    CategoryName = models.CharField(max_length=50, null=True, blank=True)
    Description = models.CharField(max_length=500, null=True, blank=True)
    Image = models.ImageField(upload_to="category")


class productdb(models.Model):
    Category = models.CharField(max_length=50, null=True, blank=True)
    ProductName = models.CharField(max_length=50, null=True, blank=True)
    Description = models.CharField(max_length=500, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Image = models.ImageField(upload_to="product")
