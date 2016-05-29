from django.db import models
from djmoney.models.fields import MoneyField
from app.models.invoice import Invoice


class InvoiceItem(models.Model):
    title = models.CharField(max_length=255)
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
    vat = models.IntegerField()
    invoice = models.ForeignKey(Invoice)
