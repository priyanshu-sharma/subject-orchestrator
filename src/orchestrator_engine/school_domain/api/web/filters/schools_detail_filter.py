from django_filters import rest_framework as filters
from school_domain.models import Schools
from extensions.rest_framework_utilities.filters import NumberInFilter, CharInFilter


class SchoolDetailFilter(filters.FilterSet):

    class Meta:
        model = Schools
        fields = {
            'id': ['exact', 'in', 'gte', 'lte'],
            'name': ['exact', 'in'],
            'state': ['exact', 'in'],
            'country': ['exact', 'in'],
            'college_name': ['exact', 'in'],
            'type': ['exact', 'in'],
            'active': ['exact', 'in'],
        }