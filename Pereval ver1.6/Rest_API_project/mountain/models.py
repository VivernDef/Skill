from django.contrib.auth.models import User, AbstractUser
from django.db import models


class Turist(User):
    middle_name = models.CharField(max_length=200)
    phone = models.BigIntegerField(unique=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class MountainCoord(models.Model):
    latitude = models.FloatField(max_length=200)
    longitude = models.FloatField(max_length=200)
    height = models.FloatField(max_length=200)

    def __str__(self):
        return f'{self.latitude} {self.longitude} {self.height}'


class Images(models.Model):
    data = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class PerevalAdded(models.Model):
    NEW = 'new'
    PENDING = 'pending'
    ACCEPTED = 'accepted'
    REJECTED = 'rejected'
    CHOICES = [
        ("new", "новый"),
        ("pending", "модератор взял в работу"),
        ("accepted", "модерация прошла успешно"),
        ("rejected", "модерация прошла, информация не принята"),
    ]

    beauty_title = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255)
    other_titles = models.CharField(max_length=255, blank=True, null=True)
    add_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Turist, on_delete=models.CASCADE, related_name='tourist_mount')
    coords = models.ForeignKey(MountainCoord, related_name='coords', blank=True, null=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=CHOICES, default=NEW)
    connect = models.TextField(null=True)
    winter = models.CharField(max_length=50, verbose_name='Зима', blank=True, null=True)
    summer = models.CharField(max_length=50, verbose_name='Лето', blank=True, null=True)
    autumn = models.CharField(max_length=50, verbose_name='Осень', blank=True, null=True)
    spring = models.CharField(max_length=50, verbose_name='Весна', blank=True, null=True)
    images = models.ForeignKey(Images, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


