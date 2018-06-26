from django.urls import path

from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib.auth import views as auth_views
from . import views
from .views import sendmemes, ListMemes, SeeMeme, likeMeme, dislikeMeme, signup
from .models import Meme

urlpatterns = [
    path("", login_required(ListMemes.as_view()), name="home"),
    path("signup", views.signup, name="signup"),
    path("senddamemes", login_required(views.CreateMeme.as_view()), name="sendmemes"),
    path(
        "updatememe/<int:pk>",
        login_required(views.UpdateMeme.as_view()),
        name="updatememe",
    ),
    path("meme/<int:pk>", login_required(views.SeeMeme.as_view()), name="seememe"),
    path(
        "login",
        auth_views.login,
        {"template_name": "benointerest/login.html"},
        name="login",
    ),
    path("logout", auth_views.logout, {"next_page": "/memes"}, name="logout"),
    path(
        "profil/<int:pk>",
        login_required(views.UpdateProfil.as_view()),
        name="updateprofile",
    ),
    path("likememe", login_required(views.likeMeme), name="likememe"),
    path("dislikememe", login_required(views.dislikeMeme), name="dislikememe"),
]
