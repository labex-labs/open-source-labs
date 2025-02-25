# Créer un tracé et une barre de couleur pour les données négatives

Nous créons un tracé des données négatives et ajoutons une barre de couleur au tracé en utilisant la fonction `colorbar`. Cette fois, nous spécifions l'emplacement de la barre de couleur, ainsi que les paramètres d'ancrage et de réduction.

```python
# repeat everything above for the negative data
# you can specify location, anchor and shrink the colorbar
neg = plt.imshow(Zneg, cmap='Reds_r', interpolation='none')
plt.colorbar(neg, location='right', anchor=(0, 0.3), shrink=0.7)
```
