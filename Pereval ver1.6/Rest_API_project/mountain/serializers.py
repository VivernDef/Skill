from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.fields import ImageField

from .models import PerevalAdded, MountainCoord, Images, Turist


class MountainCoordSerializer(serializers.ModelSerializer):
    """Сериализатор для полей координат"""
    class Meta:
        model = MountainCoord
        fields = '__all__'

    def create(self, validated_data):
        return MountainCoord.objects.create(**validated_data)


class TouristSerializer(serializers.ModelSerializer):
    """Сериализатор полей данных о пользователе"""
    class Meta:
        model = Turist
        exclude = [
            'is_staff',
            'date_joined',
            'user_permissions',
            'groups',
            'is_superuser',
            'is_active',
            'password',
            'last_login',
        ]

    def save(self, **kwargs):
        user_is = Turist.objects.filter(email=self.validated_data.get('email'))
        if user_is.exists():
            return user_is.first()
        else:
            return Turist.objects.create(
                email=self.validated_data.get('email'),
                firstname=self.validated_data.get('firstname'),
                lastname=self.validated_data.get('lastname'),
                surname=self.validated_data.get('surname'),
                phone=self.validated_data.get('phone'),
            )


class ImagesSerializer(serializers.ModelSerializer):
    """Сериализатор работы с фото"""
    class Meta:
        model = Images
        fields = [
            'data',
            'title',
        ]

    def create(self, validated_data):
        data = validated_data.pop('data')
        title = validated_data.pop('title')
        return Images.objects.create(data=data, title=title)


class PerevalSerializer(serializers.ModelSerializer):
    """Главный сериализатор для всей информации"""
    coords = MountainCoordSerializer()
    user = TouristSerializer()
    images = ImagesSerializer()

    class Meta:
        model = PerevalAdded
        fields = [
            'id',
            'beauty_title',
            'title',
            'other_titles',
            'add_time',
            'status',
            'connect',
            'winter',
            'summer',
            'autumn',
            'spring',
            'coords',
            'user',
            'images',
        ]

    def create(self, validated_data):
        coords_data = validated_data.pop('coords')
        user_data = validated_data.pop('user')
        images_data = validated_data.pop('images')

        coords = MountainCoord.objects.create(**coords_data)
        user_is = Turist.objects.filter(email=user_data['email'])
        if user_is.exists():
            user_serializer = TouristSerializer(data=user_data)
            user_serializer.is_valid()
            user = user_serializer.save()
        else:
            user = Turist.objects.create(**user_data)

        # user = Turist.objects.create(**user_data)
        images = Images.objects.create(**images_data)

        pereval = PerevalAdded.objects.create(images=images, coords=coords, user=user, **validated_data)
        return pereval


class PerevalSerializerUPdate(serializers.ModelSerializer):
    """Вспомогатльный сериализатор для органиченных полей"""
    coords = MountainCoordSerializer()
    images = ImagesSerializer()

    class Meta:
        model = PerevalAdded
        fields = [
            'id',
            'beauty_title',
            'title',
            'other_titles',
            'add_time',
            'status',
            'connect',
            'winter',
            'summer',
            'autumn',
            'spring',
            'coords',
            'images',
        ]

    def create(self, validated_data):
        coords_data = validated_data.pop('coords')
        images_data = validated_data.pop('images')

        coords = MountainCoord.objects.create(**coords_data)
        images = Images.objects.create(**images_data)

        pereval = PerevalAdded.objects.create(images=images, coords=coords, **validated_data)
        return pereval



