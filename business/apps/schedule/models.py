import uuid
from datetime import datetime

from django.db import models

from business.auth_user.models import User

from business.apps.room.models import Room


class Schedule(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.TimeField(blank=True,null=True)
    finish_time = models.TimeField(blank=True,null=True)
    start_lunch = models.TimeField(default=datetime.datetime.strptime('13:00', '%H:%M').time(), blank=True,null=True)
    finish_lunch = models.TimeField(default=datetime.datetime.strptime('14:00', '%H:%M').time(), blank=True,null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)


    class Meta:
        db_table = 'schedule'