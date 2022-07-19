from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.direction.models import Direction
from apps.direction.serializers.business.serializers import DirectionSerializer


class DirectionListCreateAPIView(ListCreateAPIView):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class DirectionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
