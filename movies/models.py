from django.db import models
from uuid import uuid4


class Movie(models.Model):
    movie_uuid = models.UUIDField(
        primary_key=True, default=uuid4, editable=False
    )
    title = models.CharField(max_length=127, unique=True)
    run_time = models.CharField(max_length=10)
    year = models.DateField(null=True)
    classification = models.PositiveIntegerField()
    synopsis = models.TextField()
    price = models.FloatField()

    stock = models.OneToOneField(
        to='stocks.Stock',
        on_delete=models.CASCADE,
        related_name='movie',
    )

    genres = models.ManyToManyField(to='genres.Genre', related_name='movies')

    carts = models.ManyToManyField(
        to='accounts.Account', related_name='movies', through='movies.Cart'
    )


class Cart(models.Model):
    cart_uuid = models.UUIDField(
        primary_key=True, default=uuid4, editable=False
    )

    total = models.FloatField()
    quantity = models.IntegerField()
    paid = models.BooleanField(default=False)

    account = models.ForeignKey(
        to='accounts.Account', on_delete=models.CASCADE, related_name='carts'
    )

    movies = models.ForeignKey(
        to='movies.Movie',
        on_delete=models.CASCADE,
    )
