from django.db import models
from django.utils.functional import empty

# Create your models here.

class Donate(models.Model):
    name = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    payment_id = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.name