# Compte du nombre d'enregistrements par catégorie

Enfin, nous allons compter le nombre d'enregistrements par catégorie.

```python
# Compte du nombre de passagers dans chaque classe de cabine
passengers_per_class = titanic["Pclass"].value_counts()
# Affichage du résultat
print(f"Le nombre de passagers dans chaque classe de cabine est {passengers_per_class}")
```
