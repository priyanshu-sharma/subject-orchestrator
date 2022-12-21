import uuid
from django.db import models
from extensions.models import AutoTimestampedModel, UserTrackingModel
from school_domain.models import Courses
from slot_domain.models import Slot

class CoursesSlot(AutoTimestampedModel, UserTrackingModel):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE)
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)
    planned_capacity = models.BigIntegerField()
    actual_capacity = models.BigIntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'so_courses_slot'
        app_label = 'slot_domain'
        unique_together = [('courses'), ('slot')]
        indexes = [
            models.Index(fields=['courses', 'slot'])
        ]

    @staticmethod
    def get_or_create(courses, slot, planned_capacity, actual_capacity, active):
        try:
            courses_slot = CoursesSlot.objects.get(courses=courses, slot=slot)
        except CoursesSlot.DoesNotExist:
            courses_slot = CoursesSlot.objects.create(courses=courses, slot=slot, planned_capacity=planned_capacity, actual_capacity=actual_capacity, active=active)
            courses_slot.save()
        return courses_slot
