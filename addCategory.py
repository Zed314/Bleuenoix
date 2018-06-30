from bleuenoix.models import Categorie
from django.core.exceptions import ObjectDoesNotExist

try:
    Categorie.objects.get(nom="default")
except ObjectDoesNotExist:
    cat = Categorie()
    cat.nom = "default"
    cat.save()
