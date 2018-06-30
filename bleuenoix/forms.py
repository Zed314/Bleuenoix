from django import forms
from .models import Meme, Profil
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):

    avatar = forms.ImageField(required=True)

    class Meta:
        model = User
        fields = (  'username' , 'avatar' ,'email', 'password1', 'password2')

class ProfilForm(forms.ModelForm):
    class Meta:
        model = Profil
        exclude = ('user',)


class MemeForm(forms.ModelForm):
    class Meta:
        model = Meme
        exclude = ('date','auteur', 'uploader', 'upvoters', 'downvoters')

