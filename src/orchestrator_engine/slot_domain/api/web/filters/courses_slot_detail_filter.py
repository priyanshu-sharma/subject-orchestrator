from django_filters import rest_framework as filters
from slot_domain.models import CoursesSlot
from extensions.rest_framework_utilities.filters import NumberInFilter, CharInFilter


class CoursesSlotDetailFilter(filters.FilterSet):

    class Meta:
        model = CoursesSlot
        fields = {
            'id': ['exact', 'in', 'gte', 'lte'],
            'courses': ['exact', 'in'],
            'slot': ['exact', 'in'],
            'planned_capacity': ['exact', 'in'],
            'actual_capacity': ['exact', 'in'],
            'active': ['exact', 'in']
        }