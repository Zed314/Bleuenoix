from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Profil(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)  # La liaison OneToOne vers le modèle User
    avatar = models.ImageField(null=True, blank=True, upload_to="avatars/")
    #email_confirmed = models.BooleanField(default=False)

   # def __str__(self):
   #     return "Profil de {0}".format(self.user.username)

class Meme(models.Model):
    titre = models.CharField(max_length=100)
    #auteur = models.CharField(max_length=42)
    uplauder = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to="photos/", null=True)
    date = models.DateTimeField(default=timezone.now, 
                                verbose_name="Date de parution")
    categorie = models.ForeignKey('Categorie', on_delete=models.SET_NULL, null=True)
    class Meta:
        verbose_name = "meme"
        ordering = ['date']
    
    def __str__(self):
        return self.titre

# Create your models here.
class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    class Meta:
        verbose_name = "categorie"
        ordering = ['nom']
    
    def __str__(self):
        return self.nom
