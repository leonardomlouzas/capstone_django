from django.db import models
from uuid import uuid4


class Stock(models.Model):
    stock_uuid = models.UUIDField(
        primary_key=True, default=uuid4, editable=False
    )
    quantity = models.IntegerField()
