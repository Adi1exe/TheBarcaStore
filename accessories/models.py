from django.db import models

class Accessory(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='accessories/')

    def __str__(self):
        return self.name
