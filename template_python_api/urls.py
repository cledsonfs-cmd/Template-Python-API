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
import dj_rest_auth
from allauth.headless.account.views import VerifyEmailView

from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from rest_framework import routers

from core import views
from core.api.viewsets import DetailUserViewSet
from core.auth.login import auth_login
from core.auth.logout import auth_logout
from core.auth.refresh import auth_refresh
from core.auth.register import auth_register
from core.auth.users import auth_users
from roles.api.viewsets import RoleViewSet
from status.api.viewsets import StatusViewSet

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

]
