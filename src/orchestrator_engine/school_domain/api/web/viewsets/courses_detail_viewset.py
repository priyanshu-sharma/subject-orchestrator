from django_filters import rest_framework as filters
from rest_framework import viewsets, mixins
from rest_framework.filters import OrderingFilter
from school_domain.api.web.pagination import StandardPagination
from school_domain.models import Courses
from school_domain.api.web.serializers import CoursesDetailSerializer
from school_domain.api.web.filters import CoursesDetailFilter


class CoursesDetailViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.filter(active=True)
    serializer_class = CoursesDetailSerializer
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filterset_class = CoursesDetailFilter
    ordering_fields = ('id',)
    ordering = ('id',)
    pagination_class = StandardPagination
