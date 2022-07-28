from rest_framework.test import APITestCase
from genres.models import Genre
from genres.serializers import GenreSerializer


class GenreViewsTest(APITestCase):
    @classmethod
    
    def setUpTestData(cls):
        cls.genres = [Genre.objects.create(name=f'genre {genre_id}') for genre_id in range(1,6)]


    def test_can_list_all_genres(self):
        response = self.client.get('/api/genres/')
        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(self.genres), len(response.data))

        for genre in self.genres:
            self.assertIn(
                GenreSerializer(instance=genre).data,
                response.data
            )

    def test_can_retrieve_a_specific_genre(self):
        genre = self.genres[0]
        response = self.client.get(f'api/genres/{genre.name}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['id'], genre.id)

        self.assertEqual(
            GenreSerializer(instance=genre).data, response.data
        )