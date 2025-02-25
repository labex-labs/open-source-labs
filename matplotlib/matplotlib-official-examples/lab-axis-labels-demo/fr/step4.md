# Définir la position de l'étiquette de la barre de couleur

Nous pouvons définir la position de l'étiquette de la barre de couleur en utilisant la méthode `colorbar` et la méthode `set_label`. Nous pouvons définir la position sur `'haut'`, `'bas'`, `'gauche'` ou `'droite'`. Dans cet exemple, nous allons définir la position sur `'haut'`.

```python
cbar = fig.colorbar(sc)
cbar.set_label("ZLabel", loc='top')
```
