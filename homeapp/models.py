from django.db import models


# Create your models here.
class regdb(models.Model):
    Username = models.CharField(max_length=50, null=True, blank=True)
    Email = models.EmailField(max_length=50, null=True, blank=True)
    Password = models.CharField(max_length=50, null=True, blank=True)
    Image = models.ImageField(upload_to="userdt", null=True, blank=True)


class Cartdb(models.Model):
    Username = models.CharField(null=True, blank=True, max_length=400)
    ProductName = models.CharField(null=True, blank=True, max_length=400)
    Quantity = models.IntegerField(null=True, blank=True)
    Total = models.IntegerField(null=True, blank=True)


class Checkout(models.Model):
    C_Name = models.CharField(max_length=50, null=True, blank=True)
    C_Email = models.EmailField(max_length=50, null=True, blank=True)
    C_Address = models.CharField(max_length=50, null=True, blank=True)
    C_Phone = models.IntegerField(null=True, blank=True)
