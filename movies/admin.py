from django.contrib.admin import site

from .models import Cart
from .models import Movie


site.register(Cart)
site.register(Movie)
