from rest_framework.serializers import ModelSerializer

from core.exceptions import UniqueException
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
            'year',
            'classification',
            'synopsis',
            'price',
            'stock',
            'genres'
        )
    
    def validate_title(self, title: str):
        movie = Movie.objects.filter(title=title.title()).exists()

        if movie:
            raise UniqueException({'detail': 'movie already exists'})
    
    def validate_classification(self, classification: int):
        if classification < 0:
            raise ValueError(
                {'detail': 'ensure this value is greater than or equal to zero'}
            )
        
        return classification


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
