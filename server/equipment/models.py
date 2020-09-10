from django.db import models


class Rod(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='equipment/rods/images/')
    thumbnail = models.ImageField(upload_to='equipment/rods/thumbnails/')
    price = models.PositiveIntegerField()
    max_weight = models.DecimalField()
    strong = models.DecimalField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Rod'
        verbose_name_plural = 'Rods'
        ordering = ('price',)

    def __str__(self):
        return self.name

    
class Hook(models.Model):
    name = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='equipment/hooks/thumbnails/')
    weigth_from = models.DecimalField()
    weight_to = models.DecimalField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Hook'
        verbose_name_plural = 'Hooks'
        ordering = ('weight_from',)

    def __str__(self):
        return self.name


class Coil(models.Model):
    name = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='equipment/coils/thumbnails/')
    strong = models.DecimalField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Coil'
        verbose_name_plural = 'Coils'
        ordering = ('strong',)
    
    def __str__(self):
        return self.name

    
class Line(models.Model):
    name = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='equipment/lines/thumbmails/')
    max_weight = models.DecimalField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Line'
        verbose_name_plural = 'Lines'
        ordering = ('max_weight',)

    def __str__(self):
        return self.name


class Bait(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    thumbnail = models.ImageField(upload_to='baits/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Bait'
        verbose_name_plural = 'Baits'
        ordering = ('price',)
    
    def __str__(self):
        return self.name


class FishingNet(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    time = models.PositiveIntegerField()
    avarange_weight = models.PositiveIntegerField()
    
    class Meta:
        verbose_name = 'Fishing net'
        verbose_name_plural = 'Fishing nets'
        ordering = ('price',)
    
    def __str__(self):
        return self.name
    