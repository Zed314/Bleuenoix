from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from .forms import MemeForm, ConnexionForm, ProfilForm
from .models import Meme, Profil
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def deconnexion(request):
    logout(request)
    return redirect(reverse("accueil"))

def connexion(request):
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
            else: # sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'benointerest/connexion.html', locals())

class CreateMeme(CreateView):
    model = Meme
    template_name = 'benointerest/sendmemes.html'
    form_class = MemeForm
    success_url = reverse_lazy('accueil')

    def form_valid(self, form):
        form.instance.uplauder = self.request.user
        return super().form_valid(form)    

class UpdateProfil(UpdateView):
    model = Profil
    template_name = 'benointerest/profil.html'
    form_class = ProfilForm
    success_url = reverse_lazy('updateprofile')


class UpdateMeme(UpdateView):
    model = Meme
    template_name = 'benointerest/sendmemes.html'
    form_class = MemeForm
    success_url = reverse_lazy('accueil')

    def form_valid(self, form):
        if self.request.user != form.instance.uplauder:
      #      print("nope")
            return super().form_invalid(form)
        return super().form_valid(form)    
     #   success_url = reverse_lazy(seememe)
# Create your views here.

class ListMemes(ListView):
    model=Meme
    context_object_name="memes"
    template_name="benointerest/accueil.html"

class SeeMeme(DetailView):
    model=Meme
    context_object_name="meme"
    template_name="benointerest/explore.html"

def sendmemes(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form = MemeForm(request.POST or None, request.FILES)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données 
    # dans le formulaire ou qu'il contient des erreurs.
    if form.is_valid(): 
        # Ici nous pouvons traiter les données du formulaire
        titre = form.cleaned_data['titre']
        auteur = form.cleaned_data['auteur']
        image = form.cleaned_data["image"]
        Meme(titre=titre, auteur=auteur, image=image).save()
        form.save()
        envoi = True
    
    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'benointerest/sendmemes.html', locals())