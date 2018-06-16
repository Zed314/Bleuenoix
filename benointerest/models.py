from django.utils import timezone
from django.db import models

# Create your models here.
class Meme(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=42)
    image = models.ImageField(upload_to="photos/", null=True)
    date = models.DateTimeField(default=timezone.now, 
                                verbose_name="Date de parution")

    class Meta:
        verbose_name = "meme"
        ordering = ['date']
    
    def __str__(self):
        """ 
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que 
        nous traiterons plus tard dans l'administration
        """
        return self.titre