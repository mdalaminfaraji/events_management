from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Event, EventImage
from .serializers import EventSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save()

        # Save event images
        event = serializer.instance
        for image in self.request.FILES.getlist('images'):
            EventImage.objects.create(event=event, image=image)

