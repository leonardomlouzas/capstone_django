# Generated by Django 4.0.6 on 2022-07-20 19:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                (
                    'stock_uuid',
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
