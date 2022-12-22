from django.urls import path, include
from rest_framework.routers import DefaultRouter

from slot_domain.api.web.viewsets import SlotDetailViewSet, CoursesSlotDetailViewSet

router = DefaultRouter()
router.register(
    r"slot_detail", SlotDetailViewSet, basename="slot_detail",
)
router.register(
    r"courses_slot_detail", CoursesSlotDetailViewSet, basename="courses_slot_detail",
)

urlpatterns = [
    path("", include(router.urls)),
]