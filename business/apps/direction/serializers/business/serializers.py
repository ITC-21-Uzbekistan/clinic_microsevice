from rest_framework.serializers import ModelSerializer

from apps.direction.models import Direction


class DirectionSerializer(ModelSerializer):
    class Meta:
        model = Direction
        fields = (
            'id',
            'direction_name',
        )
