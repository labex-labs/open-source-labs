# Définir les limites et afficher la grille

Dans cette étape, nous allons définir les limites des axes et afficher la grille. Nous utiliserons `set_aspect()` pour définir le rapport d'aspect des axes et `grid()` pour afficher la grille.

```python
# Définir les limites et afficher la grille
ax1.set_aspect(1.)
ax1.set_xlim(-5, 12)
ax1.set_ylim(-5, 10)
ax1.grid(True)
```
