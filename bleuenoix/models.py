from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Profil(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name='profile')
    avatar = models.ImageField(null=False, blank=False, upload_to="avatars/", default='bleuenoix/profile_default.png') 
 
    def __str__(self):
        return "Profile of {0}".format(self.user.username)

class Meme(models.Model):
    title = models.CharField(max_length=100)
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to="photos/", null=False)
    date = models.DateTimeField(default=timezone.now, verbose_name="Date of upload")
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    upvoters = models.ManyToManyField(Profil, related_name="upvoters")
    downvoters = models.ManyToManyField(Profil, related_name="downvoters")
    class Meta:
        verbose_name = "meme"
        ordering = ['date']
    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name = "category"
        ordering = ['name']
    def __str__(self):
        return self.name
        
