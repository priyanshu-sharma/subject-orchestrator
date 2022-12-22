"""orchestrator_engine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from rest_framework_swagger.views import get_swagger_view
from server_config import health_check_view
from school_domain.api.web import urls as school_domain_urls
from slot_domain.api.web import urls as slot_domain_urls
from django.conf.urls import include

schema_view = get_swagger_view(title='Orchestrator Engine API')

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^docs$', schema_view),
    re_path('^health_check$', health_check_view),
    re_path("^api/school_domain/v1/", include((school_domain_urls, 'school_domain'), namespace='v1_school_domain')),
    re_path("^api/slot_domain/v1/", include((slot_domain_urls, 'slot_domain'), namespace='v1_slot_domain')),
]
