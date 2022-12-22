from django_filters import rest_framework as filters
from school_domain.models import Courses
from extensions.rest_framework_utilities.filters import NumberInFilter, CharInFilter


class CoursesDetailFilter(filters.FilterSet):

    class Meta:
        model = Courses
        fields = {
            'id': ['exact', 'in', 'gte', 'lte'],
            'name': ['exact', 'in'],
            'code': ['exact', 'in'],
            'department': ['exact', 'in'],
            'active': ['exact', 'in'],
        }