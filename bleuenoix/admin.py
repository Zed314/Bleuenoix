from django.contrib import admin

from .models import Meme, Category, Profil

admin.site.register(Category)
admin.site.register(Meme)
admin.site.register(Profil)
