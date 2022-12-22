from django_filters import rest_framework as filters
from rest_framework import viewsets, mixins
from rest_framework.filters import OrderingFilter
from school_domain.api.web.pagination import StandardPagination
from school_domain.models import Schools
from school_domain.api.web.serializers import SchoolDetailSerializer
from school_domain.api.web.filters import SchoolDetailFilter


class SchoolDetailViewSet(viewsets.ModelViewSet):
    queryset = Schools.objects.filter(active=True)
    serializer_class = SchoolDetailSerializer
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filter_class = SchoolDetailFilter
    ordering_fields = ('id',)
    ordering = ('id',)
    pagination_class = StandardPagination
