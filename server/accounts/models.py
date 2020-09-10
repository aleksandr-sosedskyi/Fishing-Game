from django.db import models
from django.contrib.auth import get_user_model

from equipment.models import Coil, Hook, Rod, Line, Bait, FishingNet


class PlayerBait(models.Model):
    player = models.ForeignKey('accounts.Player', on_delete=models.CASCADE)
    bait = models.ForeignKey(Bait, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Player bait'
        verbose_name = 'Player baits'

    def __str__(self):
        return f"{self.player.user.username} - {self.bait.name} - {self.amount}"


class Player(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    money = models.PositiveIntegerField()
    level = models.PositiveIntegerField()
    exp = models.PositiveIntegerField()
    rods = models.ManyToManyField(Rod)
    hooks = models.ManyToManyField(Hook)
    coils = models.ManyToManyField(Coil)
    line = models.ManyToManyField(Line)
    bait = models.ManyToManyField(Bait, through=PlayerBait)
    fishing_net = models.ManyToManyField(FishingNet)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Player'
        verbose_name_plural = 'Players'
        ordering = ('-created_at')
    
    def __str__(self):
        return self.user.username


class PlayerLastEquipment(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE)
    rod = models.ForeignKey(Rod, on_delete=models.SET_NULL, null=True)
    hook = models.ForeignKey(Hook, on_delete=models.SET_NULL, null=True)
    coil = models.ForeignKey(Coil, on_delete=models.SET_NULL, null=True)
    line = models.ForeignKey(Line, on_delete=models.SET_NULL, null=True)
    bait = models.ForeignKey(Bait, on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Last player equipment'
        verbose_name = 'Last players equipment'
        ordering = ('-updated_at',)
    
    def __str__(self):
        return self.player.user.username
