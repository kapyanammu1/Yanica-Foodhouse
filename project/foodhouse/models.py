from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)  
    image = models.ImageField(upload_to='item_images', blank=True, null=True)

    def __str__(self):
        return self.name
    