from rest_framework import generics

from genres.models import Genre
from genres.serializers import GenreSerializer
from movies.serializers import MovieSerializer


class GenreView(generics.ListAPIView):

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreSingleView(generics.ListAPIView):

    queryset = Genre.objects.all()
    serializer_class = MovieSerializer

    def get_queryset(self):
        genre = self.kwargs['genre'].title()
        movies = self.queryset.filter(name=genre).first()
        return movies.movies.all() if movies else []
