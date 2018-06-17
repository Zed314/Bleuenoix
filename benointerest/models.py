from django.utils import timezone
from django.db import models

# Create your models here.
class Meme(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=42)
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
