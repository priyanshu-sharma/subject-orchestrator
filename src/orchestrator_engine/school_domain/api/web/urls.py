from django.urls import path, include
from rest_framework.routers import DefaultRouter

from school_domain.api.web.viewsets import SchoolDetailViewSet, DepartmentDetailViewSet, CoursesDetailViewSet

router = DefaultRouter()
router.register(
    r"school_detail", SchoolDetailViewSet, basename="school_detail",
)
router.register(
    r"department_detail", DepartmentDetailViewSet, basename="department_detail",
)
router.register(
    r"courses_detail", CoursesDetailViewSet, basename="courses_detail",
)

urlpatterns = [
    path("", include(router.urls)),
]