# Generated by Django 4.0.6 on 2022-07-21 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='year',
            new_name='premiere',
        ),
    ]
