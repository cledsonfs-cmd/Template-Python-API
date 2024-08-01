from rest_framework import parsers, renderers
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.compat import coreapi, coreschema
from rest_framework.response import Response
from rest_framework.schemas import ManualSchema
from rest_framework.schemas import coreapi as coreapi_schema
from rest_framework.utils import json
from rest_framework.views import APIView
from django.contrib.auth.models import User


class UsersAPI(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer
    http_method_names = ['get', 'head', 'post']

    if coreapi_schema.is_enabled():
        schema = ManualSchema(
            fields=[],
            encoding="application/json",
        )

    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def get(self, request):
        try:
            token = request.headers['Authorization'][7:]
            objetos = Token.objects.filter(key=token)
            if len(objetos) == 0:
                return Response({'Token inválido!'})
        except KeyError:
            return Response({'Token inválido!'})
        users = User.objects.all().order_by('username')
        retorno = []
        for u in users:
            userDTO = {
                'uid': u.id,
                'email': u.email,
                'nome': u.username,
                'provedor': '',
                'imageUrl': '',
                'role': '',
            }
            retorno.append(userDTO)

        return Response(retorno)


auth_users = UsersAPI.as_view()
