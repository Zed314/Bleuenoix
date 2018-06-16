from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    envoyeur = forms.EmailField(label="Votre adresse e-mail")
    renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)
    
    def clean_message(self):
        message = self.cleaned_data['message']
        if "benoit" in message:
            raise forms.ValidationError("On ne veut pas entendre parler de benoit !")
        return message  # Ne pas oublier de renvoyer le contenu du champ traité
