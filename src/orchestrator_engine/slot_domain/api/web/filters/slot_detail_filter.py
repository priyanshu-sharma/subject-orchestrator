from django_filters import rest_framework as filters
from slot_domain.models import Slot
from extensions.rest_framework_utilities.filters import NumberInFilter, CharInFilter


class SlotDetailFilter(filters.FilterSet):

    class Meta:
        model = Slot
        fields = {
            'id': ['exact', 'in', 'gte', 'lte'],
            'start_time': ['exact', 'in', 'gte', 'lte'],
            'end_time': ['exact', 'in', 'gte', 'lte'],
            'type': ['exact', 'in']
        }