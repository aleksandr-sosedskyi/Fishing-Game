from django.db import models

from accounts.models import Player

from fishing.models import Fish


class UserFishHistory(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    fish = models.ForeignKey(Fish, on_delete=models.CASCADE)
    weight = models.DecimalField()
    price = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'User fish history'
        verbose_name_plural = 'Users fishes history'
        ordering = ('-created_at',)
    
    def __str__(self):
        return f"{self.player.user.username} - {self.fish.name} - {self.weight}"
    
    