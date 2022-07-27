from core.exceptions import NonNegativeException, StockExceedsException, UniqueException
from django.shortcuts import get_object_or_404
from genres.models import Genre
from genres.serializers import GenreSerializer
from rest_framework.serializers import ModelSerializer
from stocks.serializers import StockSerializer

from movies.models import Cart, Movie


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


class CartMovieSerializer(ModelSerializer):
    stock = StockSerializer()

    class Meta:
        model = Movie
        fields = (
            "movie_uuid",
            "title",
            "price",
            "stock",
        )


class CartSerializer(ModelSerializer):
    movies = CartMovieSerializer(read_only=True)

    class Meta:
        model = Cart
        fields = (
            "cart_uuid",
            "total",
            "paid",
            "quantity",
            "movies",
        )

        read_only_fields = ("total","paid",)

    def validate_quantity(self, quantity: int):
        if quantity < 1:
            raise NonNegativeException(
                {'detail': 'ensure this value is greater than or equal to one'}
            )

        return quantity

    def create(self, validated_data: dict):

        quantity = validated_data.get("quantity")

        movie_uuid = validated_data.get("movies").pk

        account_uuid = validated_data.get('account').pk

        movie = get_object_or_404(Movie, pk=movie_uuid)

        cart_filter = Cart.objects.filter(account_id=account_uuid, movies_id=movie_uuid, paid=False)

        if quantity > movie.stock.quantity:
            raise StockExceedsException

        if cart_filter.exists():

            cart_item = cart_filter.first()
            cart_item.quantity += quantity

            if cart_item.quantity > movie.stock.quantity:
                raise StockExceedsException

            cart_item.total = round(cart_item.quantity * movie.price,2) 
            cart_item.save()

        else:

            total = round(quantity * movie.price,2)

            cart: Cart = Cart.objects.create(**validated_data, total=total)

            return cart

        return cart_item
