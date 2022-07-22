from django.shortcuts import render
from rest_framework import generics
from genres.models import Genre
from movies.serializers import MovieSerializer
from genres.serializers import GenreSerializer


class GenreView(generics.ListAPIView):

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreSingleView(generics.ListAPIView):

    queryset = Genre.objects.all()
    serializer_class = MovieSerializer

    def get_queryset(self):
        genre = self.kwargs["genre"]
        movies = self.queryset.filter(name=genre).first()
        return movies.movies.all()
