from django.db import models
from business.apps.direction.models import Direction

class Room(models.Model):
    room_number = models.PositiveIntegerField(null=True, blank=True)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)