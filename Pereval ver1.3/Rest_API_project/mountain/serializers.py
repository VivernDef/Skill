from rest_framework import serializers

from .models import PerevalAdded


class PerevalSerializer(serializers.ModelSerializer):
#    add_time = serializers.DateTimeField(read_only=True)
#    user_id = serializers.IntegerField()
#   coords_id = serializers.IntegerField()
#    level_status_id = serializers.IntegerField()
#    status = serializers.CharField(default='NEW')
#    activities_id = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = PerevalAdded
        fields = [
            'beauty_title',
            'title',
            'other_titles',
            'add_time',
            'status',
            'connect',
            'activities',
            'level_status',
            'coords',
            'user',
        ]


#class TouristSerializer(serializers.ModelSerializer):
