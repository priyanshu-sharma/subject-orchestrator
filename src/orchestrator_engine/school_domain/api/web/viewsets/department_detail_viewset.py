from django_filters import rest_framework as filters
from rest_framework import viewsets, mixins
from rest_framework.filters import OrderingFilter
from school_domain.api.web.pagination import StandardPagination
from school_domain.models import Department
from school_domain.api.web.serializers import DepartmentDetailSerializer
from school_domain.api.web.filters import DepartmentDetailFilter


class DepartmentDetailViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.filter(active=True)
    serializer_class = DepartmentDetailSerializer
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filterset_class = DepartmentDetailFilter
    ordering_fields = ('id',)
    ordering = ('id',)
    pagination_class = StandardPagination
