from django.shortcuts import render, redirect
from django import forms

from .models import Produit

class ProduitForm(forms.ModelForm):
  class Meta:
    model = Produit
    fields = ['nom', 'prix', 'description']

def liste_produits(request):
  produits = Produit.objects.all()
  return render(request, 'magasin/liste.html', {'produits': produits})


def ajouter_Produit(request):
  if request.method == 'POST':
    form = ProduitForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('liste_produits')
  else:
      form = ProduitForm()
  return render(request, 'magasin/ajouter.html', {'form': form})
    