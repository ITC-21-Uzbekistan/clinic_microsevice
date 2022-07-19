import uuid

from django.db import models

from apps.direction.models import Direction


class Service(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=100, blank=True, null=True)
    service_price = models.FloatField(blank=True, null=True, default=0)

    class Meta:
        db_table = 'service'
        ordering = 'service_name'

    def __str__(self):
        return self.service_name
