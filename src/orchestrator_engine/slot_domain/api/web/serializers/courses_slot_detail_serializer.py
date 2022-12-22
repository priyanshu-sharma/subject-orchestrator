from rest_framework import serializers

from slot_domain.models import CoursesSlot


class CoursesSlotDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursesSlot
        fields = (
            'id',
            'courses',
            'slot',
            'planned_capacity',
            'actual_capacity',
            'active'
        )