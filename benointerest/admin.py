from django.contrib import admin

from .models import Meme, Categorie

admin.site.register(Categorie)
admin.site.register(Meme)