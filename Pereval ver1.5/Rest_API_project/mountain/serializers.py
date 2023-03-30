from rest_framework import serializers
from rest_framework.fields import ImageField

from .models import PerevalAdded, MountainCoord, Tourist, Images


class MountainCoordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MountainCoord
        fields = '__all__'

    def create(self, validated_data):
        return MountainCoord.objects.create(**validated_data)


class TouristSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tourist
        fields = '__all__'

    def create(self, validated_data):
        return Tourist.objects.create(**validated_data)


class ImagesSerializer(serializers.ModelSerializer):
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
        user = Tourist.objects.create(**user_data)
        images = Images.objects.create(**images_data)

        pereval = PerevalAdded.objects.create(images=images, coords=coords, user=user, **validated_data)
        return pereval

    #
    # def create(self, validated_data):
    #     a_data = validated_data.pop("a")
    #     n = N.objects.create(**validated_data)
    #     for one in a.data:
    #         A.objects.create(n=n, **one)
    #
    #         A.objects.create(n=n, **a_data)





