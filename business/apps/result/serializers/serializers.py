from business.apps.result.models import Result
from rest_framework import serializers


class ResultSerializers(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'
