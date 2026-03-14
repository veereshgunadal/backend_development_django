from django.db import models

# Create your models here.

class Student(models.Model):
    roll = models.IntegerField()
    name = models.CharField()
    branch = models.CharField()
