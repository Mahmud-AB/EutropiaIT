from django.db import models

# Create your models here.

class Cloth(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.ImageField()
    
    def __str__(self):
        return f"{self.name}"
    
class Device(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.ImageField()
    
    def __str__(self):
        return f"{self.name}"
    
class Jewellery(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.ImageField()
    
    def __str__(self):
        return f"{self.name}"
    
