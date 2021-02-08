from django.db import models


class Product(models.Models):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=255, null=True)
    price = models.DecimalField(null=False)
