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
from . import views

urlpatterns = [
    path('maison', views.home),
    path('<int:numb><int:numb2>', views.number),
    path('view_redirection<str:message>', views.view_redirection),
    path('view_redirection', views.view_redirection),
    path('date',views.date),
    path('ac',views.accueil),
    path('l',views.lp, name="nom"),
    path('contact/',views.contact, name="contact"),

]
