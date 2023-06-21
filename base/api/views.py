from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serializers import RoomSerializer

@api_view(['GET'])
def getRoutes(request): #Remember that this is REST Framework - allows users to get our data if they want to
    routes =[
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id'
    ]
    return Response(routes) #safe=False means that we can use more than Python dictionaries in the resonse (routes); makes the list into a Json list/data 

@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True) #many=True asks if are there many objects that will be serialized; we answered true so yes
    return Response(serializer.data)

@api_view(['GET'])
def getRoom(request, pk):
    room = Room.objects.get(id=pk)
    serializer = RoomSerializer(room, many=False) #many=True asks if are there many objects that will be serialized; we answered true so yes
    return Response(serializer.data)