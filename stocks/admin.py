from django.contrib.admin import site

from .models import Stock


site.register(Stock)
