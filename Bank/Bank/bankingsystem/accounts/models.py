from django.db import models

# Create your models here.
class accountholder(models.Model):
    Name = models.CharField(max_length=1000)
    Withdraw = models.IntegerField()
    interest = models.IntegerField()
    interestperyear = models.IntegerField()

class banktype(models.Model):
    deposit = models.IntegerField()

class amounttype(models.Model):
    withdraw = models.IntegerField()

