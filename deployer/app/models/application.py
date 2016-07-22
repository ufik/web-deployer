from djmoney.models.fields import MoneyField
from django.db import models
from app.models.address import Address


class Application(models.Model):
    name = models.CharField(max_length=50)
    path = models.TextField(max_length=255)
    database = models.CharField(max_length=255)
    apache_config = models.TextField()
    servers = models.ManyToManyField('Server')
    billTo = models.ForeignKey(Address)
    billDate = models.DateField()
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
