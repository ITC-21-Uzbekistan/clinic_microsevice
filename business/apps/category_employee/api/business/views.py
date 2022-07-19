from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.category_employee.models import CategoryEmployee
from apps.category_employee.serializers.business.serializers import CategoryEmployeeSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class CategoryEmployeeListCreateAPIView(ListCreateAPIView):
    queryset = CategoryEmployee.objects.all()
    serializer_class = CategoryEmployeeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CategoryEmployeeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = CategoryEmployee.objects.all()
    serializer_class = CategoryEmployeeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
