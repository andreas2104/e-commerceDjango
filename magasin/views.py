from django.shortcuts import render

# Create your views here.
from .models import Produit

def liste_produits(request):
  produits = Produit.objects.all()
  return render(request, 'magasin/liste.html', {'produits': produits})