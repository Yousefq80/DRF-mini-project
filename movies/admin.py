from django.contrib import admin
from .models import Movies, Watchlist

admin.site.register([Movies, Watchlist])