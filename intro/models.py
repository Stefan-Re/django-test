from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.TextField(max_length=3000)
    price = models.CharField(max_length=120)

    def __str__(self):
        return self.name