from django.contrib.auth.models import AbstractUser
from django.db import models
from uuid import uuid4

from .managers import CustomAccountManager


class Account(AbstractUser):
    user_uuid = models.UUIDField(
        primary_key=True, default=uuid4, editable=False
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)

    id = None
    username = None
    date_joined = None

    objects = CustomAccountManager()

    REQUIRED_FIELDS: list[str] = ['first_name', 'last_name']
    USERNAME_FIELD: str = 'email'
