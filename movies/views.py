from core.permissions import IsAdminOrReadOnly
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication

from movies.models import Movie
from movies.serializers import MovieSerializer
from stocks.models import Stock


class MovieView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    permission_classes = [IsAdminOrReadOnly]
    authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer: MovieSerializer):
        valid_stock = serializer.validated_data.get('stock')
        stock = Stock.objects.create(**valid_stock)
        
        serializer.save(stock=stock)


# class MovieUuidView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
