from core.permissions import IsAdminOrReadOnlyBook
from core.exceptions import StockExceedsException
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Request, Response, status
from stocks.models import Stock

from movies.models import Cart, Movie
from movies.serializers import CartSerializer, MovieSerializer


class MovieView(generics.ListCreateAPIView):
    permission_classes = [IsAdminOrReadOnlyBook]
    authentication_classes = [TokenAuthentication]

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def perform_create(self, serializer: MovieSerializer):
        valid_stock = serializer.validated_data.get('stock')
        stock = Stock.objects.create(**valid_stock)

        serializer.save(stock=stock)


# class MovieUuidView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer

class CartAddView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def perform_create(self, serializer: CartSerializer):
        movie_uuid = self.kwargs["movie_uuid"]

        movie: Movie = get_object_or_404(Movie, pk=movie_uuid)

        serializer.save(account=self.request.user, movies=movie)


class CartListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Cart.objects.all()
        else:
            carts: list[Cart] = Cart.objects.filter(account=self.request.user)
            return carts

class CartListPendingView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Cart.objects.filter(paid=False)
        else:
            carts: list[Cart] = Cart.objects.filter(account=self.request.user, paid=False)
            return carts

class CartUuidView(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    lookup_field='cart_uuid'

class PaymentView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def post(self, request: Request):
        queryset = Cart.objects.filter(account_id=request.user.pk, paid=False)

        for item in queryset:
            new_quantity = item.movies.stock.quantity - item.quantity

            if new_quantity < 0:
                raise StockExceedsException

            stock = Stock.objects.filter(pk=item.movies.stock.pk)

            stock.update(quantity=new_quantity)

        if not queryset:
            return Response(
                {"detail": "No pending to be paid"},
                status.HTTP_422_UNPROCESSABLE_ENTITY,
            )

        queryset.update(paid=True)

        return Response({"status": "successful payment"}, status.HTTP_200_OK)
