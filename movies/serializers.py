from rest_framework.serializers import ModelSerializer

from core.exceptions import NonNegativeException
from core.exceptions import UniqueException
from genres.models import Genre
from movies.models import Cart
from movies.models import Movie
from genres.serializers import GenreSerializer
from stocks.serializers import StockSerializer


class MovieSerializer(ModelSerializer):
    stock = StockSerializer()
    genres = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = (
            'movie_uuid',
            'title',
            'run_time',
            'premiere',
            'classification',
            'synopsis',
            'price',
            'stock',
            'genres',
        )

    def validate_title(self, title: str):
        movie = Movie.objects.filter(title=title.title()).exists()

        if movie:
            raise UniqueException({'detail': 'title already exists'})

        return title.title()

    def validate_classification(self, classification: int):
        if classification < 1:
            raise NonNegativeException(
                {'detail': 'ensure this value is greater than or equal to one'}
            )

        return classification

    def create(self, validated_data: dict):
        genres_field: list[dict] = validated_data.pop('genres')

        movie: Movie = Movie.objects.create(**validated_data)
        movie.save()

        for gnr in genres_field:
            genre, _ = Genre.objects.get_or_create(**gnr)
            movie.genres.add(genre)

        return movie

    def update(self, instance: Movie, validated_data: dict):
        genres_field: list[dict] = validated_data.pop('genres', [])
        stock_field: any | dict = validated_data.pop('stock', {})

        instance.stock.quantity = stock_field.get(
            'quantity', instance.stock.quantity
        )
        # instance.stock.save()

        for gnr in genres_field:
            genre, _ = Genre.objects.get_or_create(**gnr)
            print(genre)
            instance.genres.add(genre)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance


class CartSerializer(ModelSerializer):
    movies = MovieSerializer(many=True)

    class Meta:
        model = Cart
        fields = (
            'total',
            'quantity',
            'paid',
            'movies',
        )
