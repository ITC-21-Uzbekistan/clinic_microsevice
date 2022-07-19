import uuid

from django.db import models
from business.apps.service.models import Service
from business.auth_user.models import User


class Enrollment(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        null=True,
        blank=True)
    patient_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        null=True,
        blank=True
    )

    enrollment_date = models.DateTimeField()
    employee = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE
    )
    enrollment_number = models.IntegerField()
    finished = models.BooleanField()

    class Meta:
        db_table = 'enrollment'
    class Meta:
        db_table = 'enrollment'
