from datetime import date
from django.test import TestCase

from genres.models import Genre
from movies.models import Movie
from stocks.models import Stock


class MovieModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.stock_data = {'quantity': 9}
        cls.stock_obj: Stock = Stock.objects.create(**cls.stock_data)

        cls.movie_data = {
            'title': 'A Firma',
            'run_time': '154',
            'premiere': date.fromisoformat('1996-06-30'),
            'classification': 14,
            'synopsis': 'Um jovem advogado começa a trabalhar...',
            'price': 29.99,
            'stock': cls.stock_obj,
        }

        cls.genres_data = {'name': 'Thriller'}
        cls.genre_obj: Genre = Genre.objects.create(**cls.genres_data)

        cls.movie_obj: Movie = Movie.objects.create(**cls.movie_data)
        cls.movie_obj.genres.add(cls.genre_obj)
        cls.movie_obj.save()

    def test_movie_fields(self) -> None:
        self.assertIsInstance(self.movie_obj.title, str)
        self.assertEqual(self.movie_obj.title, self.movie_data['title'])

        self.assertIsInstance(self.movie_obj.run_time, str)
        self.assertEqual(self.movie_obj.run_time, self.movie_data['run_time'])

        self.assertIsInstance(self.movie_obj.premiere, date)
        self.assertEqual(self.movie_obj.premiere, self.movie_data['premiere'])

        self.assertIsInstance(self.movie_obj.classification, int)
        self.assertEqual(self.movie_obj.classification, self.movie_data['classification'])

        self.assertIsInstance(self.movie_obj.synopsis, str)
        self.assertEqual(self.movie_obj.synopsis, self.movie_data['synopsis'])

        self.assertIsInstance(self.movie_obj.price, float)
        self.assertEqual(self.movie_obj.price, self.movie_data['price'])

        self.assertIsInstance(self.movie_obj.stock, Stock)
        self.assertEqual(self.movie_obj.stock, self.stock_obj)
