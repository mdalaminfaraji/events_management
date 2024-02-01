from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import EventItems
from .serializers import EventItemsSerializer, EventItemsInputSerializer

class EventItemViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = EventItems.objects.all()
        serializer = EventItemsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        event = EventItems.objects.get(pk=pk)
        serializer = EventItemsSerializer(event)
        return Response(serializer.data)

    def create(self, request):
        serializer = EventItemsInputSerializer(data=request.data)
        if serializer.is_valid():
            event = EventItems.objects.create(
                title=serializer.validated_data['title'],
                image=serializer.validated_data['image']
            )
            response_serializer = EventItemsSerializer(event)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        event = EventItems.objects.get(pk=pk)
        serializer = EventItemsInputSerializer(data=request.data)
        if serializer.is_valid():
            event.title = serializer.validated_data.get('title', event.title)
            event.image = serializer.validated_data.get('image', event.image)
            event.save()
            response_serializer = EventItemsSerializer(event)
            return Response(response_serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        event = EventItems.objects.get(pk=pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
