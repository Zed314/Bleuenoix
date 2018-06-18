from django import forms
from .models import Meme

class MemeForm(forms.ModelForm):
    class Meta:
        model = Meme
        exclude = ('date',)
        
class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
