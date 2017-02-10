from __future__ import unicode_literals

from django.db import models

class exchanges(models.Model):
      DATE = models.DateTimeField('DATE')
      EXCH = models.CharField(max_length=10)
      EXCH_FULL = models.CharField(max_length=100)
      class Meta:
            verbose_name = 'provider'
            verbose_name_plural = 'providers'
      def __str__(self):
            return '%s %s' % (self.EXCH, self.EXCH_FULL)
