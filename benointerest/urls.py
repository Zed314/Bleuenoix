"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib.auth import views as auth_views
from . import views
from .views import sendmemes, ListMemes, SeeMeme, likeMeme, dislikeMeme, signup
from .models import Meme

urlpatterns = [
    path("", login_required(ListMemes.as_view()), name="accueil"),
    #     path('', ListView.as_view(model=Meme,
    #                   context_object_name="memes",
    #                  template_name="benointerest/accueil.html")),
    # path('senddamemes', views.sendmemes, name  = "sendmemes"),
    path("signup", views.signup, name="signup"),
    path("senddamemes", login_required(views.CreateMeme.as_view()), name="sendmemes"),
    path(
        "updatememe/<int:pk>",
        login_required(views.UpdateMeme.as_view()),
        name="updatememe",
    ),
    #   path(r'^meme/(?P<pk>\d+)$', views.SeeMeme.as_view(), name = "seememe"),
    path("meme/<int:pk>", login_required(views.SeeMeme.as_view()), name="seememe"),
    path(
        "connexion",
        auth_views.login,
        {"template_name": "benointerest/connexion.html"},
        name="connexion",
    ),
    # {'template_name': 'benointerest/connexion.html'},
    path("deconnexion", auth_views.logout, {"next_page": "/memes"}, name="deconnexion"),
    # path('account_activation_sent', views.account_activation_sent, name='account_activation_sent'),
    # path('activate/<str:uidb64>/<str:token>', views.activate, name='activate'),
    path(
        "profil/<int:pk>",
        login_required(views.UpdateProfil.as_view()),
        name="updateprofile",
    ),
    path("likememe", login_required(views.likeMeme), name="likememe"),
    path("dislikememe", login_required(views.dislikeMeme), name="dislikememe"),
]
