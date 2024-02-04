from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import EventItems
from .serializers import EventItemsSerializers

@api_view(["GET", "POST"])
def EventItemList(request):
        if request.method=="GET":
                data=EventItems.objects.all()
                serializer=EventItemsSerializers(data, many=True)
                return Response(serializer.data)
        elif request.method=="POST":
                serializer=EventItemsSerializers(data=request.data)
                if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'PUT', 'DELETE'])
def Event_detail(request, pk):
    try:
        data = EventItems.objects.get(pk=pk)
    except EventItems.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EventItemsSerializers(data)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = EventItemsSerializers(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)