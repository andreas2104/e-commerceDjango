from django.urls import path
from .import views

urlpatterns = [
  path('', views.liste_produits, name='liste_produits'),
  path('ajouter/', views.ajouter_Produit, name='ajouter_produit'),
  path('produit/supprimer/<int:produit_id>/', views.supprimer_produit, name='supprimer_produit'),
]