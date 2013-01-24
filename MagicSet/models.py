from django.db import models

# Create your models here.
class Card(models.Model):
    cardName = models.CharField(max_length=30)
    cardCost = models.CharField(max_length=30)
    cardType = models.CharField(max_length=30)

class Set(models.Model):
    setName = models.CharField(max_length=30)

class User(models.Model):
    userName = models.CharField(max_length=30)


