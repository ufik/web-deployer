from django.db import models


class Address(models.Model):
    name = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    tax_id = models.CharField(max_length=255)

    def __unicode__(self):
        return '%s' % (self.name)
