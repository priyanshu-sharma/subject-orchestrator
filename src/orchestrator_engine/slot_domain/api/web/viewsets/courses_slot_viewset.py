from django_filters import rest_framework as filters
from rest_framework import viewsets, mixins
from rest_framework.filters import OrderingFilter
from slot_domain.api.web.pagination import StandardPagination
from slot_domain.models import CoursesSlot
from slot_domain.api.web.serializers import CoursesSlotDetailSerializer
from slot_domain.api.web.filters import CoursesSlotDetailFilter


class CoursesSlotDetailViewSet(viewsets.ModelViewSet):
    queryset = CoursesSlot.objects.filter(active=True)
    serializer_class = CoursesSlotDetailSerializer
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filter_class = CoursesSlotDetailFilter
    ordering_fields = ('id',)
    ordering = ('id',)
    pagination_class = StandardPagination
