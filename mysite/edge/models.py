# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=20)
    species = models.CharField(max_length=20)
    career = models.CharField(max_length=20)
    specializationTrees= models.CharField(max_length=100)
    soak =models.IntegerField(default=1)
    woundsThreshold= models.IntegerField(default=1)
    woundsCurrent =models.IntegerField(default=1)
    strainThreshold= models.IntegerField(default=1)
    strainCurrent = models.IntegerField(default=1)
    defenseRanged =models.IntegerField(default=1)
    defenseMelee= models.IntegerField(default=1)
    creator =models.CharField(max_length=20)
    brawn =models.IntegerField(default=1)
    agility =models.IntegerField(default=1)
    intellect =models.IntegerField(default=1)
    cunning =models.IntegerField(default=1)
    willpower =models.IntegerField(default=1)
    presence= models.IntegerField(default=1)
    astrogation= models.IntegerField(default=0)
    athletics= models.IntegerField(default=0)
    charm= models.IntegerField(default=0)
    coercion= models.IntegerField(default=0)
    computers= models.IntegerField(default=0)
    cool= models.IntegerField(default=0)
    coordination= models.IntegerField(default=0)
    deception= models.IntegerField(default=0)
    discipline= models.IntegerField(default=0)
    leadership= models.IntegerField(default=0)
    mechanics= models.IntegerField(default=0)
    medicine= models.IntegerField(default=0)
    negotiation= models.IntegerField(default=0)
    perception= models.IntegerField(default=0)
    pilotingPlanetary =models.IntegerField(default=0)
    pilotingSpace= models.IntegerField(default=0)
    resilience =models.IntegerField(default=0)
    skulduggery= models.IntegerField(default=0)
    stealth= models.IntegerField(default=0)
    streetwise =models.IntegerField(default=0)
    survival= models.IntegerField(default=0)
    vigilance =models.IntegerField(default=0)
    brawl =models.IntegerField(default=0)
    gunnery =models.IntegerField(default=0)
    melee= models.IntegerField(default=0)
    rangedLight= models.IntegerField(default=0)
    rangedHeavy =models.IntegerField(default=0)
    coreWorlds= models.IntegerField(default=0)
    education= models.IntegerField(default=0)
    lore= models.IntegerField(default=0)
    outerRim= models.IntegerField(default=0)
    underworld= models.IntegerField(default=0)
    xenology = models.IntegerField(default=0)

    def __str__(self):
        return self.name
        pass

#end BlogPost class
