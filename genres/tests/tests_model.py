from django.test import TestCase
from genres.models import Genre

class GenreModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.name = "pop"

        cls.genre = Genre.objects.create(
            name = cls.name
        )

    def test_name_field(self) -> None:
        genre = Genre.objects.get(id=1)
        max_length = genre._meta.get_field('name').max_length
        self.assertEquals(max_length, 127)