from __future__ import unicode_literals

from django.db import models

class trades(models.Model):
      CREATED = models.DateTimeField('CREATED', auto_now_add=True)
      MODIFIED = models.DateTimeField('MODIFIED', auto_now=True)
      DATE = models.DateTimeField('DATE')
      TICKER = models.CharField(max_length=6)
      VOLUME = models.IntegerField()
      VALUE = models.FloatField()
      TRADES = models.IntegerField()
      HIGH = models.FloatField()
      LOW = models.FloatField()
      OPEN = models.FloatField()
      CLOSE = models.FloatField()
      CHANGE = models.FloatField()
      class Meta:
            verbose_name = 'trade'
            verbose_name_plural = 'trades'
      def __str__(self):
            return '%s %s' % (self.DATE, self.TICKER)
