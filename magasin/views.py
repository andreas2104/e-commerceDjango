from django.shortcuts import render, redirect, get_object_or_404
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

def supprimer_produit(request, produit_id):
    if request.method == 'POST':
        produit = get_object_or_404(Produit, id=produit_id)
        produit.delete()
        return redirect('liste_produits')  # Redirige vers la liste des produits
    else:
        return redirect('liste_produits')  # Redirige si la méthode n'est pas POST
  
    