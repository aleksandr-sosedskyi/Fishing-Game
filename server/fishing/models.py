from django.db import models
from accounts.models import Player
from equipment.models import Coil, Line, Rod, Hook, Bait


class Fish(models.Model):
    name = models.CharField(max_length=255)
    min_weight = models.DecimalField()
    max_weight = models.DecimalField()
    price = models.PositiveIntegerField()
    exp = models.PositiveIntegerField()

    thumbnail = models.ImageField(upload_to='fishes/')
    bait = models.ManyToManyField(Bait)
    top_chance = models.DecimalField()
    center_chance = models.DecimalField()
    bottom_chance = models.DecimalField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Fish'
        verbose_name_plural = 'Fishes'
        ordering = ('-created_at')

    def __str__(self):
        return self.name 


class PlayerFishCorral(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    fish = models.ForeignKey(Fish, on_delete=models.CASCADE)
    weight = models.DecimalField()
    price = models.PositiveIntegerField()
    exp = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Player fish corral'
        verbose_name_plural = 'Players fish corrals'
        ordering = ('-created_at',)

