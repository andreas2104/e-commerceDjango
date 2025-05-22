from django.contrib import admin

# Register your models here.
from .models import Produit
from .models import Categorie

admin.site.register(Categorie)
admin.site.register(Produit)