""" Views """

from django.shortcuts import render, redirect
from django.db.models import Count
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from .models import Meme, Profil

from .forms import MemeForm, ProfilForm, SignUpForm



def create_profile(sender, **kwargs):
    if kwargs['created']:
        user = kwargs['instance']
        if not hasattr(user, 'profile'):
            p = Profil()
            user.profile = p
            p.save()


post_save.connect(create_profile, sender=User)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            profile = user.profile
            profile.avatar = form.cleaned_data.get('avatar')
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'bleuenoix/signup.html', {'form': form})



def deconnexion(request):
    logout(request)
    return redirect(reverse("home"))

def voteMeme(request, like):
    if request.method == 'GET':
        post_id = request.GET.get('post_id', False)
        if not post_id:
            return JsonResponse({'ok': False})
        try:
            votedMeme = Meme.objects.get(id=post_id)
        except Meme.DoesNotExist:
            return JsonResponse({'ok': False})
        if like:
            votedMeme.downvoters.remove(request.user.profile)
            if request.user.profile in votedMeme.upvoters.all():
                votedMeme.upvoters.remove(request.user.profile)
            else:   
                votedMeme.upvoters.add(request.user.profile)
        else:
            votedMeme.upvoters.remove(request.user.profile)
            if request.user.profile in votedMeme.downvoters.all():
                votedMeme.downvoters.remove(request.user.profile)
            else:   
                votedMeme.downvoters.add(request.user.profile)
        
        votedMeme.save()
        return JsonResponse({'ok': True, 'upvotes': votedMeme.upvoters.count(), 'downvotes': votedMeme.downvoters.count()})
    else:
        return JsonResponse({'ok': False})

def renderMemes(request, memes):
    memeArray = []
    memeDict = {}
    for meme in memes:
        memeId = meme.id
        title = meme.title
        image = meme.image.url
        editable = request.user == meme.uploader or request.user.has_perm('bleuenoix.change_meme')
        deletable  = request.user == meme.uploader or request.user.has_perm('bleuenoix.delete_meme')
        if meme.category:
            category = meme.category.name
        else:
            category = ""
        if meme.uploader:
            uploader = meme.uploader.username
        else:
            uploader = ""
        upvoters = meme.upvoters.count()
        downvoters = meme.downvoters.count()
        record = {"id":memeId, "title":title,"image":image,"editable":editable,"deletable":deletable,"category":category,"uploader":uploader,"upvoters":upvoters,"downvoters":downvoters}
        memeArray.append(record)
    memeDict["memes"]=memeArray
    return JsonResponse(memeDict)

def getAllMemes(request):
    if request.method == 'GET':
        memes = Meme.objects.order_by('-date')#>[:10]
        return renderMemes(request, memes)
    else:
        return JsonResponse({'ok': False})

def getAllMemesOrderedByVote(request):
    if request.method == 'GET':
        memes = Meme.objects.order_by('-date')#>[:10]
        memes = Meme.objects.annotate(upvote_count=Count('upvoters')).order_by('-upvote_count')
        return renderMemes(request, memes)
    else:
        return JsonResponse({'ok': False})

def getAllMemesOrderedByDislikeVote(request):
    if request.method == 'GET':
        memes = Meme.objects.order_by('-date')#>[:10]
        memes = Meme.objects.annotate(downvote_count=Count('downvoters')).order_by('-downvote_count')
        return renderMemes(request, memes)
    else:
        return JsonResponse({'ok': False})


def deleteMeme(request):
    if request.method == 'GET':
        post_id = request.GET.get('post_id', False)
        if post_id == False:
            return JsonResponse({'ok': False})
        try:
            memeToDelete = Meme.objects.get(id=post_id)
        except Meme.DoesNotExist:
            return JsonResponse({'ok': False})
        if not request.user.has_perm("bleuenoix.delete_meme") and not request.user == memeToDelete.uploader:
            return JsonResponse({'ok': False})
        memeToDelete.delete()
        return JsonResponse({'ok': True})  # Sending an success response
    else:
        return JsonResponse({'ok': False})


class CreateMeme(CreateView):
    model = Meme
    template_name = 'bleuenoix/sendmemes.html'
    form_class = MemeForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.uploader = self.request.user
        return super().form_valid(form)


class UpdateProfil(UpdateView):
    model = Profil
    template_name = 'bleuenoix/profil.html'
    form_class = ProfilForm
    success_url = reverse_lazy('home')

class UpdateMeme(UpdateView):
    model = Meme
    template_name = 'bleuenoix/sendmemes.html'
    form_class = MemeForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        if self.request.user != form.instance.uploader and not self.request.user.has_perm('bleuenoix.change_meme'):
            return super().form_invalid(form)
        return super().form_valid(form)


class ListMemes(ListView):
    model = Meme
    context_object_name = "memes"
    template_name = "bleuenoix/home.html"
