# Personnaliser les propriétés des graduations et des grilles d'axe

Nous pouvons personnaliser les propriétés des graduations et des grilles d'axe à l'aide des fonctions `grid()` et `tick_params()`. Dans cet exemple, nous allons changer la couleur et la taille des étiquettes de graduation et la largeur et le style des lignes de grille.

```python
ax.grid(True, linestyle='-.', linewidth=0.5, color='gray')
ax.tick_params(axis='both', which='both', labelsize=8, width=1, color='red')
```
