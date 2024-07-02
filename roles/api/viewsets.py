from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from roles.models import Role
from .serializers import RoleSerializer


class RoleViewSet(ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    filter_backends = [SearchFilter]
    search_fields = ['nome']