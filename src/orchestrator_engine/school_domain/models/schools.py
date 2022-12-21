from django.db import models
from extensions.models import AutoTimestampedModel, UserTrackingModel
from school_domain.enums import SchoolType

class Schools(AutoTimestampedModel, UserTrackingModel):
    """
    Responsible for managing all the school related information
    """
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    college_name = models.TextField(null=False)
    type = models.TextField(choices=SchoolType.choices(), default=SchoolType.PUBLIC)
    meta = models.JSONField(default=dict)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'so_schools'
        app_label = 'school_domain'
        unique_together = [('name'), ('college_name')]
        indexes = [
            models.Index(fields=['name', 'college_name'])
        ]

    @staticmethod
    def get_or_create(name, state, country, college_name, meta, type):
        try:
            schools = Schools.objects.get(name=name, college_name=college_name, type=type)
        except Schools.DoesNotExist:
            schools = Schools.objects.create(name=name, state=state, country=country, college_name=college_name, meta=meta, type=type, active=True)
            schools.save()
        return schools