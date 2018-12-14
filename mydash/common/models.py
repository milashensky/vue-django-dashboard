from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    name = models.CharField(max_length=128)
    item_name = models.CharField(max_length=128)
    price = models.FloatField()
    owner = models.ForeignKey(User, on_delete=models.deletion.CASCADE)

    def __str__(self):
        return '{s.name} - {s.price}'.format(s=self)
