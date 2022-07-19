from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from business.apps.room.serializers.serializers import RoomSerializer
from business.apps.schedule.models import Room
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ListCreateRoomAPIView(ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class RetrieveUpdateDestroyRoomAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
