from rest_framework.serializers import ModelSerializer

from apps.service.models import Service


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = (
            'id',
            'direction',
            'service_name',
            'service_price',
        )
