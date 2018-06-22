from django import forms
from .models import Meme, Profil
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):

    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = (  'username','email', 'password1', 'password2')

class ProfilForm(forms.ModelForm):
    class Meta:
        model = Profil
        exclude = ('user',)


class MemeForm(forms.ModelForm):
    class Meta:
        model = Meme
        exclude = ('date','auteur', 'uplauder', 'upvoters', 'downvoters')


class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
