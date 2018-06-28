from django.contrib import admin

from .models import Meme, Categorie, Profil

admin.site.register(Categorie)
admin.site.register(Meme)
admin.site.register(Profil)
