from core.permissions import IsAdminOrReadOnlyBook
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication

from movies.models import Movie
from movies.serializers import MovieSerializer
from stocks.models import Stock


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
