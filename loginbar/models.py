from __future__ import unicode_literals

from django.db import models

# Create your models here.

class mapping(models.Model):
      created = models.DateTimeField('created', auto_now_add=True)
      modified = models.DateTimeField('modified', auto_now=True)
      uri = models.CharField(max_length=10)
      text = models.CharField(max_length=50)

      def __str__(self):
         return 'uri: %s text: %s' % (self.uri, self.text)

      
