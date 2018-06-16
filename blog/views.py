from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime

# Create your views here.

from .forms import ContactForm

def contact(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form = ContactForm(request.POST or None)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données 
    # dans le formulaire ou qu'il contient des erreurs.
    if form.is_valid(): 
        # Ici nous pouvons traiter les données du formulaire
        sujet = form.cleaned_data['sujet']
        message = form.cleaned_data['message']
        envoyeur = form.cleaned_data['envoyeur']
        renvoi = form.cleaned_data['renvoi']

        # Nous pourrions ici envoyer l'e-mail grâce aux données 
        # que nous venons de récupérer
        envoi = True
    
    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'blog/contact.html', locals())
    
def home(request):
    #return HttpResponse("""<h1>WESH</h1>""")
    return redirect(view_redirection, "Redirigé!")

def number(request,numb,numb2):
    return HttpResponse(numb2)

def view_redirection(request, message="ntm"):
    return HttpResponse(message)

def date(request):
    return render(request,'blog/date.html', {'date':datetime.now(), 'req':request})

def lp(request):
    return HttpResponse("i")

def accueil(request):
    return render(request, 'blog/accueil.html')

    