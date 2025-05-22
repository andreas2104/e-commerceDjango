from django.db import models

# Create your models here.
class Categorie(models.Model):
  nom = models.CharField(max_length=100)

  def __str__(self):
    return self.nom

class Produit(models.Model):
  nom = models.CharField(max_length=100)
  prix = models.DecimalField(max_digits=10, decimal_places=2)
  description =  models.CharField(max_length=200)
  categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)

  def __str__(self):
    return self.nom