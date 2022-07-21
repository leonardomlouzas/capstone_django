from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import status
from rest_framework.views import APIView

# from core.permissions import IsAdminOrReadOnly
from .models import Account
from .serializers import AccountSerializer
from .serializers import LoginSerializer


class AccountView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminOrReadOnly]

    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountUuidView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    lookup_field = 'user_uuid'


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
