from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Student(models.Model):
    sage = models.IntegerField()
    sclass = models.IntegerField()
    sname= models.CharField(max_length =20)
    joined_date = models.DateField()
    
