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
from django.urls import path, include
from rest_framework import routers
from core.api.viewsets import DetailUserViewSet
from rest_framework.authtoken.views import obtain_auth_token

from roles.api.viewsets import RoleViewSet
from status.api.viewsets import StatusViewSet

router = routers.DefaultRouter()
router.register(r'template', DetailUserViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'status', StatusViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
    path("api-token-auth/", obtain_auth_token, name='api_token_auth'),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('accounts/', include('allauth.urls')),
]
