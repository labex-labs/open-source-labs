# Ajuster la position de la barre de couleur

Nous pouvons également ajuster la position de la barre de couleur à l'aide de `plt.axes`. Cette fonction prend une liste de valeurs `[gauche, bas, largeur, hauteur]` en arguments pour spécifier la position et la taille des axes. Exécutez le code suivant :

```python
cax = plt.axes([0.85, 0.1, 0.075, 0.8])
plt.colorbar(cax=cax)
```
