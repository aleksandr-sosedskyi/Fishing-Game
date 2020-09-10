from django.db import models

from equipment.models import FishingNet

from accounts.models import Player


class Level(models.Model):
    value = models.PositiveIntegerField()
    exp = models.PositiveIntegerField()
    award = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Level'
        verbose_name_plural = 'Levels'
        ordering = ('value',)

    def __str__(self):
        return self.value 


class SetFishingNet(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    fishing_net = models.ForeignKey(FishingNet, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Set fishing net'
        verbose_name_plural = 'Set fishing nets'
        ordering = ('-created_at',)
    
    def __str__(self):
        return f"{self.player.user.username} - {self.fishing_net.name}"
