from rest_framework import serializers
from .models import Event, EventImage

class EventImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventImage
        fields = ('image',)

class EventSerializer(serializers.ModelSerializer):
    images = EventImageSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ('id', 'title', 'description', 'images')
