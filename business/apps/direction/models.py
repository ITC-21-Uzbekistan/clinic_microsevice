import uuid

from django.db import models


class Direction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    direction_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'direction'
        ordering = 'direction_name'

    def __str__(self):
        return self.direction_name
