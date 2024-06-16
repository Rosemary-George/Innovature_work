
# Create your models here.
from django.db import models

class Operation(models.Model):
    num1 = models.FloatField()
    num2 = models.FloatField()
    operation = models.CharField(max_length=10)
