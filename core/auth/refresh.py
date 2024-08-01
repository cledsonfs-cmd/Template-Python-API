from rest_framework import parsers, renderers
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.compat import coreapi, coreschema
from rest_framework.response import Response
from rest_framework.schemas import ManualSchema
from rest_framework.schemas import coreapi as coreapi_schema
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class RefreshAPI(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

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

    def post(self, request, *args, **kwargs):
        try:
            token = request.headers['Authorization'][7:]
            objetos = Token.objects.filter(key=token)
            if len(objetos) == 0:
                return Response({'Token inválido!'})
        except KeyError:
            return Response({'Token inválido!'})

        user1 = User.objects.filter(id=objetos[0].user_id)[0]
        objetos[0].delete()
        token, created = Token.objects.get_or_create(user=user1)

        return Response({
            'uid': user1.id,
            'email': user1.email,
            'nome': user1.username,
            'token': token.key,
            'provedor': '',
            'imageUrl': '',
            'role': '',
        })


auth_refresh = RefreshAPI.as_view()
