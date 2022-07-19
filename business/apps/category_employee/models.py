import uuid

from django.db import models


class CategoryEmployee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name_category_employee = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'category_employee'

    def __str__(self):
        return self.name_category_employee
