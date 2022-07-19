from django.db import models
from business.apps.enrollment.models import Enrollment


class Result_Files(models.Model):
    result_file = models.FileField()


class Result(models.Model):
    enrollment = models.ForeignKey(
        Enrollment,
        on_delete=models.CASCADE
    )
    description = models.TextField(
        max_length=200
    )
    files = models.ForeignKey(Result_Files,
                              on_delete=models.CASCADE
                              )

    class Meta:
        db_table = 'result'


    class Meta:
        db_table = 'result'

