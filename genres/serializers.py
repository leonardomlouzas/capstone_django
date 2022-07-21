from rest_framework.serializers import ModelSerializer

from .models import Genre


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        exclude = ['genre_uuid']

    def validate_name(self, name: str):
        return name.title()
