from django.db import models


class Vaccine(models.Model):

    short_description = models.CharField(max_length=20)
    long_description = models.CharField(blank=True, max_length=500)
    quantity = models.DecimalField(max_digits=10, decimal_places=0)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
