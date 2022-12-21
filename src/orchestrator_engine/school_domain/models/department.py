from django.db import models
from extensions.models import AutoTimestampedModel, UserTrackingModel
from school_domain.models import Schools

class Department(AutoTimestampedModel, UserTrackingModel):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    school = models.ForeignKey(Schools, on_delete=models.CASCADE)
    meta = models.JSONField(default=dict)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'so_department'
        app_label = 'school_domain'
        unique_together = [('name'), ('school')]
        indexes = [
            models.Index(fields=['name', 'school'])
        ]

    @staticmethod
    def get_or_create(name, school, meta, active):
        try:
            department = Department.objects.get(name=name, school=school, meta=meta, active=active)
        except Department.DoesNotExist:
            department = Department.objects.create(name=name, school=school, meta=meta, active=active)
            department.save()
        return department
