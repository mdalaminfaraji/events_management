from rest_framework import serializers
from .models import EventItems

class EventItemsSerializers(serializers.ModelSerializer):
        class Meta:
                model=EventItems
                fields=('id', 'title', 'image')