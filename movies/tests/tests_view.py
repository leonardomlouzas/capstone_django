from datetime import date
from faker import Faker
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from uuid import uuid4

from accounts.models import Account
from genres.models import Genre
from movies.models import Movie
from stocks.models import Stock


class MovieViewTest(APITestCase):
    def setUp(self) -> None:
        fake = Faker()
        user_data = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'email': fake.email(),
            'password': fake.password(),
        }
        user: Account = Account.objects.create_superuser(**user_data)

        token = Token.objects.create(user=user)

        # self.client.credentials(HTTP_AUTHORIZATION='Token' + token.key)
        # self.client.force_login(user=user)
        self.client.force_authenticate(user=user)

        # @classmethod
        # def setUpTestData(cls) -> None:
        self.url = '/api/movies/'
        self.stock_data = {'quantity': 9}
        self.stock_obj: Stock = Stock.objects.create(**self.stock_data)
        # print(self.stock_obj)

        self.movie_data = {
            'title': 'A Firma',
            'run_time': '154',
            'premiere': date.fromisoformat('1996-06-30'),
            'classification': 14,
            'synopsis': 'Um jovem advogado começa a trabalhar...',
            'price': 29.99,
            'stock': self.stock_obj
        }

        self.genres_data = {'name': 'Thriller'}
        self.genre_obj: Genre = Genre.objects.create(**self.genres_data)

        self.movie_obj: Movie = Movie.objects.create(**self.movie_data)
        self.movie_obj.genres.add(self.genre_obj)
        self.movie_obj.save()

        self.movie_data_response = {
            'movie_uuid': uuid4(),
            'title': 'A Firma',
            'run_time': '154',
            'premiere': date.fromisoformat('1996-06-30'),
            'classification': 14,
            'synopsis': 'Um jovem advogado começa a trabalhar...',
            'price': 29.99,
            'stock': self.stock_obj,
            'genres': self.genre_obj,
        }

    def test_create_movie_without_authentication_fails(self) -> None:
        response = self.client.post(self.url, self.movie_data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            {
                'title': ['movie with this title already exists.'],
                'stock': ['This field is required.'],
                'genres': ['This field is required.'],
            },
            response.json(),
        )

    def test_create_movie_missing_fields_fail(self) -> None:
        response = self.client.post(self.url, {})

        self.assertEqual(response.status_code, 400)
        self.assertDictEqual(
            response.json(),
            {
                'classification': ['This field is required.'],
                'genres': ['This field is required.'],
                'price': ['This field is required.'],
                'run_time': ['This field is required.'],
                'stock': ['This field is required.'],
                'synopsis': ['This field is required.'],
                'title': ['This field is required.'],
            },
        )

    # def test_create_movie_invalid_format_premiere(self) -> None:
    #     response = self.client.post(self.url, self.movie_data)
    #     self.assertEqual(response.status_code, 400)
