"""
URL configuration for template_python_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers

from core.api.viewsets import DetailUserViewSet
from core.auth.login import auth_login
from core.auth.logout import auth_logout
from core.auth.refresh import auth_refresh
from core.auth.register import auth_register
from core.auth.users import auth_users
from roles.api.viewsets import RoleViewSet
from status.api.viewsets import StatusViewSet

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
       title="Api Python - Template Base",
       default_version='v1.0',
       description="Templete basico para desenvolvimento de APIs em Python",
       contact=openapi.Contact(email="cledsonfs@gmail.com"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'template', DetailUserViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'status', StatusViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),

    path("api/login", auth_login),
    path("api/logout", auth_logout),
    path("api/refresh", auth_refresh),
    path("api/users", auth_users),
    path("api/register", auth_register),

    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),


]
