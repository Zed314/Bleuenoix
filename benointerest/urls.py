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
from django.views.generic import ListView

from . import views
from .views import sendmemes, ListMemes, SeeMeme
from .models import Meme

urlpatterns = [
     path('', ListMemes.as_view(), name="accueil"),
#     path('', ListView.as_view(model=Meme,
 #                   context_object_name="memes",
  #                  template_name="benointerest/accueil.html")),
    # path('senddamemes', views.sendmemes, name  = "sendmemes"),
     path('senddamemes', views.CreateMeme.as_view(), name  = "sendmemes"),
     path('updatememe/<int:pk>', views.UpdateMeme.as_view(), name  = "updatememe"),
  #   path(r'^meme/(?P<pk>\d+)$', views.SeeMeme.as_view(), name = "seememe"),
     path("meme/<int:pk>", views.SeeMeme.as_view(), name = "seememe"),
     path("connexion",views.connexion,name='connexion')


]
