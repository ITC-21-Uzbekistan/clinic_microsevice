from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from business.apps.schedule.serializers.serializers import ScheduleSerializer
from business.apps.schedule.models import Schedule
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ListCreateScheduleAPIView(ListCreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class RetrieveUpdateDestroyScheduleAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )