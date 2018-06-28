from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from .forms import MemeForm, ProfilForm, SignUpForm
from .models import Meme, Profil
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from django.http import HttpResponse
from django.http import JsonResponse


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            profil = Profil()
            profil.avatar = form.cleaned_data.get('avatar')
            profil.user = user
            profil.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'benointerest/signup.html', {'form': form})


def deconnexion(request):
    logout(request)
    return redirect(reverse("home"))


def likeMeme(request):
    if request.method == 'GET':
        post_id = request.GET.get('post_id', False)
        if post_id == False:
            return JsonResponse({'ok': False})
        try:
            likedMeme = Meme.objects.get(id=post_id)  # getting the liked posts
        except Meme.DoesNotExist:
            return JsonResponse({'ok': False})
        likedMeme.upvoters.add(request.user.profil)
        likedMeme.downvoters.remove(request.user.profil)
        likedMeme.save()  # saving it to store in database
        # Sending an success response
        return JsonResponse({'ok': True, 'upvotes': likedMeme.upvoters.count(), 'downvotes': likedMeme.downvoters.count()})

    else:
        return JsonResponse({'ok': False})


def dislikeMeme(request):
    if request.method == 'GET':
        post_id = request.GET.get('post_id', False)
        if post_id == False:
            return JsonResponse({'ok': False})
        try:
            dislikedMeme = Meme.objects.get(
                id=post_id)  # getting the disliked meme
        except Meme.DoesNotExist:
            return JsonResponse({'ok': False})
        dislikedMeme.upvoters.remove(request.user.profil)
        dislikedMeme.downvoters.add(request.user.profil)
        dislikedMeme.save()  # saving it to store in database
        # Sending an success response
        return JsonResponse({'ok': True, 'upvotes': dislikedMeme.upvoters.count(), 'downvotes': dislikedMeme.downvoters.count()})
    else:
        return JsonResponse({'ok': False})


def deleteMeme(request):
    if request.method == 'GET':
        post_id = request.GET.get('post_id', False)
        if not request.user.has_perm("benointerest.delete_meme"):
            return JsonResponse({'ok': False})
        if post_id == False:
            return JsonResponse({'ok': False})
        try:
            memeToDelete = Meme.objects.get(id=post_id)
        except Meme.DoesNotExist:
            return JsonResponse({'ok': False})
        memeToDelete.delete()
        return JsonResponse({'ok': True})  # Sending an success response
    else:
        return JsonResponse({'ok': False})


class CreateMeme(CreateView):
    model = Meme
    template_name = 'benointerest/sendmemes.html'
    form_class = MemeForm
    success_url = reverse_lazy('home')

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
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        if self.request.user != form.instance.uplauder:
          #      print("nope")
            return super().form_invalid(form)
        return super().form_valid(form)
     #   success_url = reverse_lazy(seememe)
# Create your views here.


class ListMemes(ListView):
    model = Meme
    context_object_name = "memes"
    template_name = "benointerest/home.html"


class SeeMeme(DetailView):
    model = Meme
    context_object_name = "meme"
    template_name = "benointerest/explore.html"


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
