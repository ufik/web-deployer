from django.db import models
from app.models.address import Address


class Invoice(models.Model):
    date = models.DateField()
    dueDate = models.DateField()
    invoiceNo = models.CharField(max_length=50)
    billTo = models.ForeignKey(Address)
