from django.urls import path

from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from . import views
from .views import ListMemes


urlpatterns = [
    path("", login_required(ListMemes.as_view()), name="home"),
    path("signup", views.signup, name="signup"),
    path("senddamemes", login_required(views.CreateMeme.as_view()), name="sendmemes"),
    path(
        "updatememe/<int:pk>",
        login_required(views.UpdateMeme.as_view()),
        name="updatememe",
    ),
    path(
        "login",
        auth_views.login,
        {"template_name": "bleuenoix/login.html"},
        name="login",
    ),
    path("logout", auth_views.logout, {"next_page": "/memes"}, name="logout"),
    path(
        "profil/<int:pk>",
        login_required(views.UpdateProfil.as_view()),
        name="updateprofile"
    ),
    path("getAllMemes", login_required(views.getAllMemes), name="getAllMemes"),
    path("getPreferredMemes", login_required(views.getAllMemesOrderedByVote), name="getPreferredMemes"),
    path("getHatedMemes", login_required(views.getAllMemesOrderedByDislikeVote), name="getHatedMemes"),
    path("getMyMemes", login_required(views.getMyMemes), name="getMyMemes"),
    path("likememe", login_required(views.voteMeme), {'like':True}, name="likememe"),
    path("dislikememe", login_required(views.voteMeme), {'like':False}, name="dislikememe"),
    path("deletememe", login_required(views.deleteMeme), name="deletememe"),
]
