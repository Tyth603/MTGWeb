from django.db import models

# Create your models here.
class Card(models.Model):

    rarityTypes = (
        ('M', 'Mythic Rare'),
        ('R','Rare'),
        ('U','Uncommon'),
        ('C','Common'),
        ('L','Land'),
        ('S','Special'),
        ('P','Promo'))
    cardTypes = (
        ('S','Sorcery'),
        ('I','Instant'),
        ('A','Artifact'),
        ('E','Enchantment'),
        ('L','Land'),
        ('C','Creature'),
        ('B','Basic'),
        ('G','Legendary'),
        ('O','Ongoing'),
        ('PH','Phenomenon'),
        ('PL','Plane'),
        ('PW','Planeswalker'),
        ('SC','Scheme'),
        ('S','Snow'),
        ('T','Tribal'),
        ('V','Vanguard'),
        ('W','World'))

    cardName = models.CharField(max_length=30)
    cardCost = models.CharField(max_length=30)
    convertedManaCost = models.SmallIntegerField(null=True)
    cardType = models.CharField(max_length=30, choices=cardTypes)
    cardSubType = models.CharField(max_length=30)
    rulesText = models.TextField()
    power = models.SmallIntegerField(null=True)
    toughness = models.SmallIntegerField(null=True)
    artwork = models.CharField(max_length=30)
    setId = models.SmallIntegerField(null=True)
    rarity = models.CharField(max_length=30, choices=rarityTypes)

class Set(models.Model):
    setName = models.CharField(max_length=30)

class User(models.Model):
    userName = models.CharField(max_length=30)


