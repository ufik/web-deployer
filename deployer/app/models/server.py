from djmoney.models.fields import MoneyField
from django.db import models


class Server(models.Model):
    name = models.CharField(max_length=50)
    ip = models.CharField(max_length=255, null=True)
    path = models.TextField(max_length=255)
    costs = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
