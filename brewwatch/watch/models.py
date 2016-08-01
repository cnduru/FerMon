from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Reading(models.Model):
    value = models.IntegerField()
    date = models.DecimalField(decimal_places = 2, max_digits = 15) 