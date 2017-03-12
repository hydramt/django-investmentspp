from __future__ import unicode_literals

from django.db import models

class exchanges(models.Model):
      created = models.DateTimeField(auto_now_add=True)
      modified = models.DateTimeField(auto_now=True)
      exch = models.CharField(max_length=10)
      exch_full = models.CharField(max_length=100)
      enabled = models.BooleanField(default=True)
      class Meta:
            verbose_name = 'provider'
            verbose_name_plural = 'providers'
      def __str__(self):
            return '%s %s' % (self.exch, self.exch_full)
