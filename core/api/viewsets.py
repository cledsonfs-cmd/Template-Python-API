from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.models import DetailUser
from .serializers import DetailUserSerializer


class DetailUserViewSet(ModelViewSet):
    queryset = DetailUser.objects.all()
    serializer_class = DetailUserSerializer
    filter_backends = [SearchFilter]
    search_fields = ['observacao']
    # permission_classes = (DjangoModelPermissions,)
    # authentication_classes = (TokenAuthentication,)

