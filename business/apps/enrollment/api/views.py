from business.apps.enrollment.serializers.serializers import EnrollmentSerializers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from business.apps.enrollment.models import Enrollment
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ListCreateEnrollmentAPIView(ListCreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializers


class RetrieveUpdateDestroyEnrollmentAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializers
