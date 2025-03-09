from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=60)
    price = models.IntegerField()
    image = models.ImageField(upload_to="jerseys/", default="default.jpg")

    def __str__(self):
        return self.name