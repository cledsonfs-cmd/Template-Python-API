from django.contrib.auth.models import User
from rest_framework import parsers, renderers
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework.schemas import ManualSchema
from rest_framework.schemas import coreapi as coreapi_schema
from rest_framework.views import APIView
from rest_framework import status


class RegisterAPI(APIView):
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
        userExist = User.objects.filter(username=request.data["username"])
        if len(userExist) > 0:
            return Response({'usuário já cadastrado'})
        userExist = User.objects.filter(email=request.data["email"])
        if len(userExist) > 0:
            return Response({'email já cadastrado'})

        user = User.objects.create_user(request.data["username"], request.data["email"], request.data["password"])
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'uid': user.id,
            'email': user.email,
            'nome': user.username,
            'token': token.key,
            'provedor': '',
            'imageUrl': '',
            'role': '',
        }, status=status.HTTP_201_CREATED)

auth_register = RegisterAPI.as_view()
