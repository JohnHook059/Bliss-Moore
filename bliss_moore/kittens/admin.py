from django.contrib import admin
from .models import Cat, Article, Litter
admin.site.register([Cat, Article, Litter])

