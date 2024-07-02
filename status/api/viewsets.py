from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from status.models import Status
from .serializers import StatusSerializer


class StatusViewSet(ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    filter_backends = [SearchFilter]
    search_fields = ['nome']
