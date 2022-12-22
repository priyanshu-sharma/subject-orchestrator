from django_filters import rest_framework as filters
from school_domain.models import Department
from extensions.rest_framework_utilities.filters import NumberInFilter, CharInFilter


class DepartmentDetailFilter(filters.FilterSet):

    class Meta:
        model = Department
        fields = {
            'id': ['exact', 'in', 'gte', 'lte'],
            'name': ['exact', 'in'],
            'school': ['exact', 'in'],
            'active': ['exact', 'in'],
        }