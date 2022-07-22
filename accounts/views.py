from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.views import status

from accounts.models import Account
from accounts.permissions import IsAdmin
from accounts.serializers import AccountSerializer
from accounts.serializers import AccountUpdateSerializer
from accounts.serializers import LoginSerializer
from core.mixins import SerializerByMethodMixin
from core.permissions import IsAdminOrReadOnlyAccount


class AccountView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrReadOnlyAccount]

    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountUuidView(
    SerializerByMethodMixin, generics.RetrieveUpdateDestroyAPIView
):
    queryset = Account.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdmin]

    lookup_field = 'user_uuid'

    serializer_map = {
        'GET': AccountSerializer,
        'PATCH': AccountUpdateSerializer,
        'PUT': AccountUpdateSerializer,
        'DELETE': AccountSerializer,
    }


class LoginView(APIView):
    def post(self, request: Request):
        serialized = LoginSerializer(data=request.data)
        serialized.is_valid(raise_exception=True)

        user: Account = authenticate(**serialized.validated_data)

        if user:
            token, _ = Token.objects.get_or_create(user=user)

            return Response({'token': token.key}, status.HTTP_200_OK)

        return Response(
            {'detail': 'invalid email or password'},
            status.HTTP_401_UNAUTHORIZED,
        )
