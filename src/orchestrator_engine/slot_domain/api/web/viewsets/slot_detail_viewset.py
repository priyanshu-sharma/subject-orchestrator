from django_filters import rest_framework as filters
from rest_framework import viewsets, mixins
from rest_framework.filters import OrderingFilter
from slot_domain.api.web.pagination import StandardPagination
from slot_domain.models import Slot
from slot_domain.api.web.serializers import SlotDetailSerializer
from slot_domain.api.web.filters import SlotDetailFilter


class SlotDetailViewSet(viewsets.ModelViewSet):
    queryset = Slot.objects.all()
    serializer_class = SlotDetailSerializer
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filter_class = SlotDetailFilter
    ordering_fields = ('id',)
    ordering = ('id',)
    pagination_class = StandardPagination
