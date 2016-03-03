from __future__ import unicode_literals

from django.db import models

# Create your models here.
class db(models.Model):
    username = models.CharField(max_length=30, blank=False)
    email = models.EmailField(blank=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return self.username
