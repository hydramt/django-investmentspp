from __future__ import unicode_literals

from django.db import models

class trades(models.Model):
      created = models.DateTimeField(auto_now_add=True)
      modified = models.DateTimeField(auto_now=True)
      date = models.DateTimeField()
      ticker = models.CharField(max_length=6)
      volume = models.IntegerField()
      value = models.FloatField()
      trades = models.IntegerField()
      high = models.FloatField()
      low = models.FloatField()
      open = models.FloatField()
      close = models.FloatField()
      change = models.FloatField()
      class Meta:
            verbose_name = 'trade'
            verbose_name_plural = 'trades'
      def __str__(self):
            return '%s %s' % (self.date, self.ticker)
