from rest_framework import serializers

from slot_domain.models import Slot


class SlotDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields = (
            'id',
            'start_time',
            'end_time',
            'type'
        )