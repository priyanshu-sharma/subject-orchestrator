from django.db import models
from extensions.models import AutoTimestampedModel, UserTrackingModel
from slot_domain.enums import SlotType

class Slot(AutoTimestampedModel, UserTrackingModel):
    id = models.BigIntegerField(primary_key=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    type = models.TextField(choices=SlotType.choices(), default=SlotType.FALL)

    class Meta:
        db_table = 'so_slot'
        app_label = 'slot_domain'
        unique_together = [('start_time'), ('end_time'), ('type')]
        indexes = [
            models.Index(fields=['start_time', 'end_time', 'type'])
        ]

    @staticmethod
    def get_or_create(start_time, end_time, type):
        try:
            slot = Slot.objects.get(start_time=start_time, end_time=end_time, type=type)
        except Slot.DoesNotExist:
            slot = Slot.objects.create(start_time=start_time, end_time=end_time, type=type)
        return slot
