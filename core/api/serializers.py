from rest_framework import serializers
from core.models import DetailUser


class DetailUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailUser
        fields = ['id', 'user', 'role', 'status', 'observacao', 'ativo']
