from django.db import models


class Tourist(models.Model):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)
    phone = models.BigIntegerField(unique=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class MountainCoord(models.Model):
    latitude = models.FloatField(max_length=200)
    longitude = models.FloatField(max_length=200)
    height = models.FloatField(max_length=200)

    def __str__(self):
        return f'{self.latitude} {self.longitude} {self.height}'


class Level(models.Model):
    winter = models.CharField(max_length=10, verbose_name='Зима', blank=True, null=True)
    summer = models.CharField(max_length=10, verbose_name='Лето', blank=True, null=True)
    autumn = models.CharField(max_length=10, verbose_name='Осень', blank=True, null=True)
    spring = models.CharField(max_length=10, verbose_name='Весна', blank=True, null=True)

    def __str__(self):
        return f'{self.winter} {self.summer} {self.autumn} {self.spring}'


class Images(models.Model):
    from_mountain = models.ForeignKey('PerevalAdded', on_delete=models.CASCADE,)
    data = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    title = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)


class SprActivitiesTypes(models.Model):
    title = models.CharField(max_length=50, unique=True)

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
    user = models.ForeignKey(Tourist, on_delete=models.CASCADE, related_name='tourist_mount')
    coords = models.ForeignKey(MountainCoord, on_delete=models.CASCADE)
    level_status = models.ForeignKey(Level, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=CHOICES, default=NEW)
    activities = models.ManyToManyField(SprActivitiesTypes, through='PerevalAddedSprActivitiesTypes')
    connect = models.TextField(null=True)

    def __str__(self):
        return self.title


class PerevalAddedSprActivitiesTypes(models.Model):
    perevalAdded = models.ForeignKey(PerevalAdded, on_delete=models.CASCADE)
    sprActivitiesTypes = models.ForeignKey(SprActivitiesTypes, on_delete=models.CASCADE)

