from bleuenoix.models import Category
from django.core.exceptions import ObjectDoesNotExist

try:
    Category.objects.get(name="default")
except ObjectDoesNotExist:
    cat = Category()
    cat.name = "default"
    cat.save()
