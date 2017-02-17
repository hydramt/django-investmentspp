from __future__ import unicode_literals

from django.db import models

class exchanges(models.Model):
      CREATED = models.DateTimeField('CREATED', auto_now_add=True)
      MODIFIED = models.DateTimeField('MODIFIED', auto_now=True)
      EXCH = models.CharField(max_length=10)
      EXCH_FULL = models.CharField(max_length=100)
      ENABLED = models.BooleanField(default=True)
      class Meta:
            verbose_name = 'provider'
            verbose_name_plural = 'providers'
      def __str__(self):
            return '%s %s' % (self.EXCH, self.EXCH_FULL)
