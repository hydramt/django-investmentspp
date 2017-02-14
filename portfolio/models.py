from __future__ import unicode_literals

from django.db import models

class portfolio(models.Model):
      user_id = models.IntegerField(blank=False)
      security_id = models.CharField(max_length=100)
      date = models.DateTimeField(blank=False)
      quantity = models.FloatField()
      purchase_price = models.FloatField()
      expenses = models.FloatField()
