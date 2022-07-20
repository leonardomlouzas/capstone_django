from django.db import models
from uuid import uuid4


class Genre(models.Model):
    genre_uuid = models.UUIDField(
        primary_key=True, default=uuid4, editable=False
    )
    name = models.CharField(max_length=127, unique=True)
