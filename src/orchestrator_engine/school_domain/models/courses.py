from django.db import models
from extensions.models import AutoTimestampedModel, UserTrackingModel
from school_domain.models import Department

class Courses(AutoTimestampedModel, UserTrackingModel):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    schedule = models.JSONField(default=dict)
    meta = models.JSONField(default=dict)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'so_courses'
        app_label = 'school_domain'
        unique_together = [('name'), ('code'), ('department')]
        indexes = [
            models.Index(fields=['name', 'code', 'department'])
        ]

    @staticmethod
    def get_or_create(name, code, department, schedule, meta, active):
        try:
            courses = Courses.objects.get(name=name, code=code, department=department, schedule=schedule, meta=meta, active=active)
        except Courses.DoesNotExist:
            courses = Courses.objects.create(name=name, code=code, department=department, schedule=schedule, meta=meta, active=active)
            courses.save()
        return courses
