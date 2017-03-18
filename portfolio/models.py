from __future__ import unicode_literals

from django.db import models


class portfolio(models.Model):
      created = models.DateTimeField(auto_now_add=True)
      modified = models.DateTimeField(auto_now=True)
      user_id = models.IntegerField(blank=False)
      portfolio_id = models.AutoField(primary_key=True)
      portfolio_name = models.CharField(max_length=100)

      def __str__(self):
        return '%s (pid: %s, user_id: %s)' % (self.portfolio_name, self.portfolio_id, self.user_id)

class portfolio_data(models.Model):
      created = models.DateTimeField(auto_now_add=True)
      modified = models.DateTimeField(auto_now=True)
      user_id = models.IntegerField(blank=False)
      portfolio_id = models.IntegerField(blank=False)
      security_id = models.CharField(max_length=100)
      date = models.DateTimeField(blank=False)
      quantity = models.FloatField()
      purchase_price = models.FloatField()
      expenses = models.FloatField(blank=True, null=True)

      class Meta:
         verbose_name = 'Portfolio Data'
         verbose_name_plural = 'Portfolio Data'

      def __str__(self):
        return '%s %s %s' % (self.portfolio_id, self.user_id, self.security_id)
