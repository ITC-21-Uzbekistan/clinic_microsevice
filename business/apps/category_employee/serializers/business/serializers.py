from rest_framework.serializers import ModelSerializer

from apps.category_employee.models import CategoryEmployee


class CategoryEmployeeSerializer(ModelSerializer):
    class Meta:
        model = CategoryEmployee
        fields = (
            'id',
            'name_category_employee',
        )
