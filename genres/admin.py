from django.contrib.admin import site

from .models import Genre


site.register(Genre)
