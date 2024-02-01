from rest_framework import serializers
from .models import EventItems, EventItemImages

class EventItemImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventItemImages
        fields = ('image',)

class EventItemsSerializer(serializers.ModelSerializer):
    image = EventItemImagesSerializer()

    class Meta:
        model = EventItems
        fields = ('id', 'title', 'image')


    def create(self, validated_data):
        image_data = validated_data.pop('image')
        image_instance = EventItemImages.objects.create(image=image_data['image'])
        event = EventItems.objects.create(image=image_instance, **validated_data)
        return event

    def update(self, instance, validated_data):
        image_data = validated_data.pop('image')
        instance.title = validated_data.get('title', instance.title)
        instance.image.image = image_data.get('image', instance.image.image)
        instance.image.save()
        instance.save()
        return instance

class EventItemsInputSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    image = serializers.ImageField()
