from django.db import models

# Create your models here.


class Place(models.Model):
    objects = None
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to="pics")
    desc = models.TextField()

    def __str__(self):
        return self.name


class Basket(models.Model):
    objects = None
    img = models.ImageField(upload_to="pics")
    name = models.CharField(max_length=250)
    desc = models.TextField()
