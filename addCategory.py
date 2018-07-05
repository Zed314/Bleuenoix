from bleuenoix.models import Category
from django.core.exceptions import ObjectDoesNotExist

try:
    Category.objects.get(nom="default")
except ObjectDoesNotExist:
    cat = Category()
    cat.nom = "default"
    cat.save()
