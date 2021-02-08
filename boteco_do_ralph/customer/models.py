from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    doc_num = models.CharField(max_length=50, null=False, blank=False)
    phone = models.CharField(max_length=20, null=True)
